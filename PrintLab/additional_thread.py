import os
import shutil
from PyQt6 import QtCore
import asyncio
from mega import Mega
import urllib.request
import re
from PrintLab.database import extract_from_backup


dir_path = os.getcwd()
old_db_name = 'old_ling_lab.sqlite3'
db_name = 'ling_lab.sqlite3'

try:
    import vlc
except:
    pass


class RadioAndAutoprintThread(QtCore.QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.run_all())

    async def run_all(self):
        await asyncio.gather(self.radio_pl(), self.auto_sync(), self.db_sync(), self.blink_timer(),
                             self.print_coupons(), self.print_warranty(), self.check_current_song())

    async def blink_timer(self):
        blink_flag = 1
        while True:
            if self.mainwindow.current_client_rate == 'blacklist':
                if blink_flag:
                    self.mainwindow.label_InBlackList.setText("У ЧОРНОМУ СПИСКУ!!!")
                    blink_flag = 0
                else:
                    self.mainwindow.label_InBlackList.setText("")
                    blink_flag += 1
            await asyncio.sleep(0.7)

    async def radio_pl(self):
        while True:
            if self.mainwindow.radio_is_playing:
                try:
                    radio_player = vlc.MediaPlayer(self.mainwindow.radio_current_url)
                    radio_player.play()
                    self.mainwindow.add_to_log(f"Радіо стрім  {self.mainwindow.radio_current_url}")
                    old_url = self.mainwindow.radio_current_url
                    self.info_line = '  '
                    self.old_song = ''
                    while old_url == self.mainwindow.radio_current_url and self.mainwindow.radio_is_playing:
                        radio_player.audio_set_volume(self.mainwindow.horizontalSliderRadioLoud.value())
                        if self.old_song != self.mainwindow.radio_current_song:
                            self.old_song = self.mainwindow.radio_current_song
                        self.mainwindow.labelLog.setText(self.mainwindow.radio_current_song)
                        await asyncio.sleep(0.5)
                    radio_player.stop()
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                    break
            await asyncio.sleep(0.1)

    async def check_current_song(self):
        while True:
            if self.mainwindow.radio_is_playing:
                try:
                    request = urllib.request.Request(self.mainwindow.radio_current_url)
                    request.add_header('Icy-MetaData', 1)
                    response = urllib.request.urlopen(request)
                    icy_metaint_header = response.headers.get('icy-metaint')
                    if icy_metaint_header is not None:
                        metaint = int(icy_metaint_header)
                        read_buffer = metaint + 255
                        content = response.read(read_buffer)
                        content = content.decode('latin-1')
                        pattern = r"StreamTitle='(.*?)';"
                        content = re.search(pattern, content)
                        self.mainwindow.radio_current_song = content.group(1)
                        self.mainwindow.show_current_song()
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
            await asyncio.sleep(5)

    async def db_sync(self):
        while True:
            if self.mainwindow.db_ready_to_sync:
                self.mainwindow.db_ready_to_sync = False
                self.mainwindow.add_to_log('Cинхронізація')
                try:
                    mega = Mega()
                    m = mega.login(self.mainwindow.settings_dict['mega_user'],
                                   self.mainwindow.settings_dict['mega_pass'])
                    details = m.get_user()
                    self.mainwindow.add_to_log(f"З'єднано {details['email']} ")
                    file = m.find(old_db_name)
                    self.mainwindow.add_to_log('Завантажую файли')
                    self.mainwindow.user_login_status = True
                    self.mainwindow.check_mega_login()
                    self.mainwindow.db_ready_to_upload = True
                    if file:
                        m.download(file)
                        old_db_path = str(dir_path) + '/' + old_db_name
                        db_path = str(dir_path) + '/' + db_name
                        extract_from_backup(old_db_path, db_path)
                    self.mainwindow.paste_in_radios_table()
                    self.mainwindow.paste_in_clients_table()
                except Exception as ex:
                    if str(ex) == "'NoneType' object is not subscriptable":
                        self.mainwindow.add_to_log(str(ex))
                    else:
                        self.mainwindow.user_login_status = False
                        self.mainwindow.add_to_log(f"З'єднання розірвано  {ex}")
                        if self.mainwindow.auth_has_been_changed:
                            self.mainwindow.mega_logout()
                            self.mainwindow.auth_has_been_changed = False
                        continue

            if self.mainwindow.db_ready_to_upload and self.mainwindow.tableWidgetClients.rowCount():
                self.mainwindow.db_ready_to_upload = False
                self.mainwindow.add_to_log('Оновлення бази даних')
                try:
                    mega = Mega()
                    m = mega.login(self.mainwindow.settings_dict['mega_user'],
                                   self.mainwindow.settings_dict['mega_pass'])
                    for _ in range(2):
                        file = m.find(old_db_name)
                        if file:
                            resp = m.delete(file[0])
                    shutil.copy(db_name, old_db_name)
                    m.upload(old_db_name)
                    self.mainwindow.add_to_log('Синхронізовано')
                except Exception as ex:
                    self.mainwindow.add_to_log(f"З'єднання розірвано  {ex}")
                self.mainwindow.add_to_log('Очистка тимчасових файлів')
                try:
                    os.remove(old_db_name)
                    self.mainwindow.add_to_log('Видалено')
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                self.mainwindow.progress_bar_status = False
                self.mainwindow.paste_in_radios_table()
            await asyncio.sleep(1)

    async def auto_sync(self):
        while True:
            await asyncio.sleep(self.mainwindow.spinBoxBackupTime.value() * 60)
            if self.mainwindow.checkBoxAutobackup.isChecked():
                self.mainwindow.db_ready_to_sync = True

    async def print_coupons(self):
        while True:
            while self.mainwindow.ready_to_print > 0:
                try:
                    os.startfile(self.mainwindow.print_path, "print")
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                    self.mainwindow.ready_to_print -= 1
                self.mainwindow.ready_to_print -= 1
                await asyncio.sleep(self.mainwindow.spinBoxPauseBetweenCopies.value())
            await asyncio.sleep(1)

    async def print_warranty(self):
        while True:
            if self.mainwindow.ready_to_print_warranty > 0:
                try:
                    os.startfile(self.mainwindow.print_path, "print")
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                self.mainwindow.ready_to_print_warranty -= 1
            await asyncio.sleep(1)
