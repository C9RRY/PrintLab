import os
import pathlib
import shutil
import sqlite3
from PyQt5 import QtCore
import asyncio
from mega import Mega


dir_path = pathlib.Path(__file__).parent.resolve()
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
        await asyncio.gather(self.radio_pl(), self.auto_sync(), self.db_sync(),
                             self.print_coupons(), self.print_warranty())

    async def radio_pl(self):
        while True:
            if self.mainwindow.radio_is_play:
                try:
                    radio_player = vlc.MediaPlayer(self.mainwindow.radio_current_url)
                    radio_player.play()
                    self.mainwindow.add_to_log(f"Радіо стрім \n {self.mainwindow.radio_current_url}")
                    old_url = self.mainwindow.radio_current_url
                    while old_url == self.mainwindow.radio_current_url and self.mainwindow.radio_is_play:
                        await asyncio.sleep(0.8)
                    radio_player.stop()
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                    break
            await asyncio.sleep(0.1)

    async def db_sync(self):
        while True:
            if self.mainwindow.db_ready_to_sync:
                self.mainwindow.db_ready_to_sync = False
                self.mainwindow.add_to_log('Cинхронізація')
                try:
                    mega = Mega()
                    m = mega.login('ivan.lisovenko93@gmail.com', '93uranos')
                    details = m.get_user()
                    self.mainwindow.add_to_log(f"З'єднано \n {details['email']} ")
                    file = m.find(old_db_name)
                    self.mainwindow.add_to_log('Завантажую файли')
                    m.download(file)
                except Exception as ex:
                    self.mainwindow.user_login_status = False
                    self.mainwindow.add_to_log(f"З'єднання розірвано \n {ex}")
                    shutil.copy(db_name, old_db_name)

                conn = sqlite3.connect(str(dir_path) + '/' + old_db_name)
                cursor = conn.cursor()
                cursor.execute(f'SELECT brand, package, breakage, name, phone_number, in_date, '
                               f'break_fix, price, warranty, out_date, is_fixed, device_type '
                               f'FROM clients ')
                data = cursor.fetchall()
                conn.commit()
                cursor.close()
                conn.close()
                for client in data:
                    conn = sqlite3.connect(str(dir_path) + '/' + db_name)
                    cursor = conn.cursor()
                    cursor.execute(f'INSERT INTO clients (brand, package, breakage, name, phone_number, in_date, '
                                   f'break_fix, price, warranty, out_date, is_fixed, device_type) '
                                   f'SELECT * FROM (SELECT "{client[0]}" AS brand, "{client[1]}" AS package, '
                                   f'"{client[2]}" AS breakage, "{client[3]}" AS name, "{client[4]}" AS phone_number, '
                                   f'"{client[5]}" AS in_date, "{client[6]}" AS break_fix, "{client[7]}" AS price, '
                                   f'"{client[8]}" AS warranty, "{client[9]}" AS out_date, "{client[10]}" AS is_fixed, '
                                   f'"{client[11]}" AS device_type'
                                   f') AS temp '
                                   f'WHERE NOT EXISTS ('
                                   f'  SELECT in_date FROM clients WHERE in_date = "{client[5]}" '  # need to add AND name =
                                   f') LIMIT 1')
                    conn.commit()
                self.mainwindow.add_to_log('Оновлення бази даних')
                try:
                    mega = Mega()
                    m = mega.login('ivan.lisovenko93@gmail.com', '93uranos')
                    for _ in range(2):
                        file = m.find(old_db_name)
                        if file:
                            resp = m.delete(file[0])
                    shutil.copy(db_name, old_db_name)
                    m.upload(old_db_name)
                    self.mainwindow.add_to_log('Синхронізовано')
                except Exception as ex:
                    self.mainwindow.add_to_log(f"З'єднання розірвано \n {ex}")
                self.mainwindow.add_to_log('Очистка тимчасових файлів')
                try:
                    os.remove(old_db_name)
                    self.mainwindow.add_to_log('Видалено')
                except Exception as ex:
                    self.mainwindow.add_to_log(ex)
                self.mainwindow.progress_bar_status = False

                self.mainwindow.paste_in_clients_table()
            await asyncio.sleep(1)

    async def auto_sync(self):
        while True:
            await asyncio.sleep(self.mainwindow.spinBox_autosync.value() * 60)
            if self.mainwindow.checkBox.isChecked():
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
                await asyncio.sleep(self.mainwindow.spinBox_2.value())
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
