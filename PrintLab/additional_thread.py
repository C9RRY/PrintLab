import os
from PyQt6 import QtCore
import asyncio
import urllib.request
import json
import re
from PrintLab.database import extract_from_backup, extract_clients_for_firebase
from PrintLab.firebase_conn import login, update_firebase, get_list_from_firebase


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
        self._is_running = True

    def run(self):
        loop = asyncio.new_event_loop()
        loop.run_until_complete(self.run_all())

    async def run_all(self):
        await asyncio.gather(self.radio_pl(), self.auto_sync(), self.db_sync(), self.blink_timer(),
                             self.print_coupons(), self.print_warranty(), self.check_current_song())

    async def blink_timer(self):
        blink_flag = 1
        while self._is_running:
            if self.mainwindow.current_client_rate == 'blacklist':
                if blink_flag:
                    self.mainwindow.label_InBlackList.setText("У ЧОРНОМУ СПИСКУ!!!")
                    blink_flag = 0
                else:
                    self.mainwindow.label_InBlackList.setText("")
                    blink_flag += 1
            await asyncio.sleep(0.7)

    async def radio_pl(self):
        while self._is_running:
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
        while self._is_running:
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
                    json_part = re.search(r'\{.*\}', str(ex), re.DOTALL).group()
                    self.mainwindow.add_to_log(json.loads(json_part)['error']['errors'][0]['message'])
            await asyncio.sleep(5)

    async def db_sync(self):
        while self._is_running:
            if self.mainwindow.db_ready_to_upload and self.mainwindow.tableWidgetClients.rowCount():
                self.mainwindow.db_ready_to_upload = False
                self.mainwindow.add_to_log('Оновлення бази даних')
                try:
                    self.token = login(self.mainwindow.settings_dict['mega_user'],
                                       self.mainwindow.settings_dict['mega_pass'])
                    clients_data = extract_clients_for_firebase()
                    update_firebase(self.token, clients_data, 'clients')
                    self.mainwindow.add_to_log('Клієнти - оновлено')

                except Exception as ex:
                    self.mainwindow.add_to_log(ex)


            if self.mainwindow.db_ready_to_sync:
                self.mainwindow.db_ready_to_sync = False
                self.mainwindow.add_to_log('Cинхронізація')
                try:
                    self.token = login(self.mainwindow.settings_dict['mega_user'],
                                       self.mainwindow.settings_dict['mega_pass'])
                    self.mainwindow.add_to_log(f"З'єднано {self.mainwindow.settings_dict['mega_user']} ")
                    self.mainwindow.user_login_status = True
                    self.mainwindow.check_login()
                    self.mainwindow.db_ready_to_upload = True

                    backup_data = get_list_from_firebase(self.token, 'clients')
                    extract_from_backup(backup_data)
                    self.mainwindow.paste_in_radios_table()
                    self.mainwindow.paste_in_clients_table()
                except Exception as ex:
                    print(ex)

                    self.mainwindow.user_login_status = False

                    if self.mainwindow.auth_has_been_changed:
                        self.mainwindow.auth_has_been_changed = False

            await asyncio.sleep(1)

    async def auto_sync(self):
        while self._is_running:
            await asyncio.sleep(self.mainwindow.spinBoxBackupTime.value() * 60)
            if self.mainwindow.checkBoxAutobackup.isChecked():
                self.mainwindow.db_ready_to_sync = True

    async def print_coupons(self):
        while self._is_running:
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
        while self._is_running:
            if self.mainwindow.ready_to_print_warranty > 0:
                try:
                    os.startfile(self.mainwindow.print_path, "print")
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                self.mainwindow.ready_to_print_warranty -= 1
            await asyncio.sleep(1)

    def stop_all(self):
        self._is_running = False
