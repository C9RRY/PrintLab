import time
from datetime import datetime
from PrintLab.coupon_print import paste_to_order, paste_to_warranty
from PrintLab.database import (extract_clients_data, save_new_order, save_warranty, get_must_use, save_settings, del_station,
                      save_radio_choice, save_new_station, extract_settings, extract_radios_data, extract_from_backup,
                      get_previous_price)
from PrintLab.themes import MyThemes
import calendar
import shutil
import os
from PrintLab.additional_thread import RadioAndAutoprintThread
from PrintLab.user_form import Ui_DialogMegaLogin
from PrintLab.confirm_form import Ui_MainWindowConfirmForm
from PyQt6 import QtCore, QtWidgets
from PrintLab.ui_main_window import Ui_MainWindow
from PrintLab.firebase_conn import get_from_firebase, login
import sys


dir_path = os.path.dirname(os.path.abspath(__file__))


class Ui_MyWindow(Ui_MainWindow):
    def __init__(self):
        self.logs_count = 0
        self.warranty_date = '0000-00-00 00:00:00'
        self.is_previous_orders = False
        self.client_table_filters = ''
        self.settings_dict = extract_settings()
        self.db_ready_to_sync = 0
        self.user_login_status = False
        self.print_list = []
        self.print_path = ''
        self.ready_to_print = 0
        self.ready_to_print_warranty = 0
        self.db_ready_to_upload = 0
        self.warranty_print_list = []
        self.radio_current_song = ''
        self.sharing_dict = {}
        self.auth_has_been_changed = False
        self.line_edit_break_fix_old_text = ''
        self.line_edit_model_2_old_text = ''
        self.line_edit_additional_package_old_text = ''
        self.line_edit_phone_breakage_2_old_text = ''
        self.current_client_rate = 'normal'
        self.date_now = datetime.now()
        self.radio_is_playing = False
        self.radio_current_url = ''
        self.radio_current_name = ''
        self.radio_thread = RadioAndAutoprintThread(mainwindow=self)
        self.cloud_radio_num = 0
        self.last_backup_datetime = '0000-00-00 00:00:00'

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.tableWidgetClients.setColumnWidth(0, 55)
        self.tableWidgetClients.setColumnWidth(1, 90)
        self.tableWidgetClients.setColumnWidth(2, 140)
        self.tableWidgetClients.setColumnWidth(3, 160)
        self.tableWidgetClients.setColumnWidth(4, 105)
        self.tableWidgetClients.setColumnWidth(5, 200)

        self.tableWidgetRadioStations.setColumnWidth(0, 180)
        self.tableWidgetRadioStations.setColumnWidth(1, 510)
        self.tableWidgetRadioStations.setColumnWidth(2, 50)
        self.tableWidgetRadioStations.setColumnWidth(3, 0)

        self.tableWidget.setColumnWidth(0, 85)
        self.tableWidget.setColumnWidth(1, 110)
        self.tableWidget.setColumnWidth(2, 270)
        self.tableWidget.setColumnWidth(3, 270)

        self.comboBoxCreateTabPackage.addItems(['Телефон', 'Планшет', 'Телевізор',
                                                   'Ноутбук', 'ПК', 'Монітор', 'інше'])
        self.comboBoxGadgetType.addItems(['Всі', 'Телефон', 'Планшет', 'Телевізор',
                                            'Ноутбук', 'ПК', 'Монітор', 'інше'])
        self.comboBoxIsFixed.addItems(['Всі', 'В процесі', 'Видано'])
        self.comboBoxSearchFilter.addItems(['Модель', 'ПІБ', 'Телефон'])
        self.comboBoxColorTheme.addItems(['Світла', 'Темна'])

        self.comboBoxCouponBreakFix.addItems(get_must_use('break_fix', 'WHERE is_fixed = 1'))
        self.comboBoxCreateTabModel.addItems(get_must_use('brand', ''))
        self.comboBoxCreateTabAdditionalPack.addItems(get_must_use('package', ''))
        self.comboBoxCreateTabBreakage.addItems(get_must_use('breakage', ''))
        self.settings_unpack()

        self.lineEditSearch.textChanged.connect(self.change_search_filter)
        self.comboBoxGadgetType.currentTextChanged.connect(self.change_search_filter)
        self.comboBoxIsFixed.currentTextChanged.connect(self.change_search_filter)
        self.comboBoxSearchFilter.currentTextChanged.connect(lambda: self.lineEditSearch.setText(''))
        self.tableWidgetClients.cellClicked.connect(self.open_selected)

        self.lineEditCouponBreakFix.textChanged.connect(self.break_fix_input_prediction)
        self.lineEditCouponBreakFix.returnPressed.connect(self.break_fix_return_pressed)
        self.comboBoxCouponBreakFix.textActivated.connect(self.combobox_break_fix_choice)

        self.lineEditCreateTabPhoneNum.editingFinished.connect(self.find_previous_orders)
        self.lineEditCreateTabName.returnPressed.connect(self.create_name_return_pressed)

        self.lineEditCreateTabModel.textChanged.connect(self.create_tab_input_prediction)
        self.lineEditCreateTabModel.returnPressed.connect(self.create_tab_return_pressed)
        self.comboBoxCreateTabModel.textActivated.connect(self.create_tab_combobox_model_activated)
        self.comboBoxCreateTabPackage.textActivated.connect(self.model_type_predict_filter)

        self.lineEditCreateTabAdditionalPack.textChanged.connect(self.additional_package_input_prediction)
        self.lineEditCreateTabAdditionalPack.returnPressed.connect(self.additional_package_return_pressed)
        self.comboBoxCreateTabAdditionalPack.textActivated.connect(self.combobox_additional_package_choice)

        self.lineEditCreateTabBreakage.textChanged.connect(self.create_tab_phone_breakage_prediction)
        self.lineEditCreateTabBreakage.returnPressed.connect(self.create_tab_phone_breakage_return_pressed)
        self.comboBoxCreateTabBreakage.textActivated.connect(self.create_tab_combobox_breakage_activated)

        self.comboBoxColorTheme.blockSignals(True)
        self.comboBoxColorTheme.currentTextChanged.connect(self.change_color_theme)
        self.comboBoxColorTheme.blockSignals(False)

        self.tab.tabBarClicked.connect(self.clean_filters)

        self.tableWidgetRadioStations.cellClicked.connect(self.click_to_play)

        self.pushButtonSyncToFirebase.clicked.connect(self.sync_with_cloud)
        self.pushButtonCouponSave.clicked.connect(self.save_warranty_or_order_change)
        self.pushButtonCouponPrint.clicked.connect(self.print_warranty)
        self.pushButtonCreateTabSave.clicked.connect(self.new_order_check_all_fields)
        self.pushButtonCreateTabClear.clicked.connect(self.new_order_clean_all)
        self.pushButtonRadioSave.clicked.connect(self.save_new_station)
        self.pushButtonSettingsSave.clicked.connect(self.save_settings)
        self.pushButtonRadiosFromCloud.clicked.connect(self.extract_radios_from_cloud)
        self.pushButtonRadioPlay.clicked.connect(self.enable_radio)
        self.pushButtonRadioStop.clicked.connect(self.disable_radio)
        self.pushButtonLogout.clicked.connect(self.user_logout_confirm)
        self.pushButtonExportBase.clicked.connect(self.save_backup_file)
        self.pushButtonImportBase.clicked.connect(self.open_backup_file)
        self.pushButtonOpenClientFile.clicked.connect(self.open_client_xlsx)

        self.toolButtonAuth.clicked.connect(lambda: self.open_sing_up_form())

        self.radio_thread.start()
        self.create_tab_input_prediction()
        self.add_to_log()

        self.paste_in_clients_table()
        self.tab.setTabVisible(2, False)
        self.comboBoxCreateTabAdditionalPack.setCurrentIndex(1)
        self.paste_in_radios_table()
        self.check_login()
        if self.radio_is_playing:
            self.enable_radio()
        self.db_ready_to_sync = True
        self.change_color_theme()
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def settings_unpack(self):
        self.checkBoxAutobackup.setChecked(bool(self.settings_dict['auto_sync']))
        self.checkBoxAutoprint.setChecked(bool(self.settings_dict['auto_print']))
        self.spinBoxPrintCopyAmount.setValue(int(self.settings_dict['copies']))
        self.spinBoxPauseBetweenCopies.setValue(int(self.settings_dict['pause_between_copies']))
        self.radio_is_playing = bool(int(self.settings_dict['radio_is_playing']))
        self.radio_current_url = self.settings_dict['radio_current_url']
        self.radio_current_name = self.settings_dict['radio_current_name']
        self.horizontalSliderRadioLoud.setValue(int(self.settings_dict['radio_volume_level']))
        self.spinBoxBackupTime.setValue(int(self.settings_dict['auto_sync_time']))
        self.checkBoxRadioAutoPlay.setChecked(self.radio_is_playing)
        self.lineEditAdditional_info1.setText(self.settings_dict['additional_print_line1'])
        self.lineEditAdditional_info2.setText(self.settings_dict['additional_print_line2'])
        self.lineEditAdditional_info3.setText(self.settings_dict['additional_print_line3'])
        self.comboBoxColorTheme.setCurrentText(self.settings_dict['theme'])

        # self.last_backup_datetime = datetime.now()
        # print(self.last_backup_datetime)

        self.last_backup_datetime = '20241227121448'
        self.last_backup_datetime = datetime.strptime(self.last_backup_datetime, "%Y%m%d%H%M%S")



    def check_login(self):
        if self.user_login_status:
            self.pushButtonLogout.show()
            self.pushButtonSyncToFirebase.setText('Синхронізувати')
            self.labelMegaLogin.setText(self.settings_dict['mega_user'])
        else:
            self.pushButtonLogout.hide()
            self.pushButtonSyncToFirebase.setText('Увійти')
            self.labelMegaLogin.setText('')

    def user_logout_confirm(self):
        self.open_confirm_form(f'Вийти з {self.settings_dict["mega_user"]}?', self.user_logout)

    def user_logout(self):
        self.settings_dict['mega_user'] = ''
        self.settings_dict['mega_pass'] = ''
        self.user_login_status = False
        self.check_login()

    def open_sing_up_form(self):
        self.sing_up_window = QtWidgets.QDialog()
        self.ui = Ui_DialogMegaLogin()
        self.ui.setupUi(self.sing_up_window, self)
        self.sing_up_window.show()

    def open_backup_file(self):
        old_db_path = QtWidgets.QFileDialog.getOpenFileName(filter='*.sqlite3')[0]
        if old_db_path:
            db_path = str(dir_path) + '/' + 'ling_lab.sqlite3'
            extract_from_backup(old_db_path, db_path)
            self.paste_in_clients_table()
            self.tab.setCurrentIndex(0)

    def save_backup_file(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(filter='*.sqlite3')[0]
        if file_path:
            shutil.copy('ling_lab.sqlite3', file_path)

    def clean_filters(self):
        self.comboBoxGadgetType.setCurrentIndex(0)
        self.comboBoxIsFixed.setCurrentIndex(0)
        self.lineEditSearch.setText('')

    def paste_in_clients_table(self):
        columns = 'in_date, brand, name, phone_number, breakage, id, client_rate'
        data = extract_clients_data(columns, self.client_table_filters)
        self.tableWidgetClients.setRowCount(len(data))
        if data:
            row = 0
            for client in data:
                self.tableWidgetClients.setItem(row, 0, QtWidgets.QTableWidgetItem(str(client[5])))
                str_time = client[0][0:19]
                in_date_datetime = datetime.strptime(str_time, '%Y-%m-%d %H:%M:%S')
                coupon_age = int((self.date_now - in_date_datetime).total_seconds() // 86400)
                if coupon_age < 1:
                    self.tableWidgetClients.setItem(row, 1, QtWidgets.QTableWidgetItem('Сьогодні'))
                elif coupon_age == 1:
                    self.tableWidgetClients.setItem(row, 1, QtWidgets.QTableWidgetItem('Вчора'))
                elif 1 < coupon_age < 30:
                    self.tableWidgetClients.setItem(row, 1, QtWidgets.QTableWidgetItem(f'{coupon_age} дн. тому'))
                elif coupon_age >= 30:
                    self.tableWidgetClients.setItem(row, 1, QtWidgets.QTableWidgetItem(
                        str(in_date_datetime.day) + " " + calendar.month_name[in_date_datetime.month]))
                self.tableWidgetClients.setItem(row, 2, QtWidgets.QTableWidgetItem(client[1].capitalize()))
                self.tableWidgetClients.setItem(row, 3, QtWidgets.QTableWidgetItem(client[2].title()))
                self.tableWidgetClients.setItem(row, 4, QtWidgets.QTableWidgetItem(client[3]))
                self.tableWidgetClients.setItem(row, 5, QtWidgets.QTableWidgetItem(client[4].capitalize()))
                self.tableWidgetClients.setItem(row, 6, QtWidgets.QTableWidgetItem(client[6]))
                row += 1

    def change_search_filter(self):
        self.client_table_filters = 'WHERE '
        if self.comboBoxGadgetType.currentText() == 'Всі':
            self.client_table_filters += 'id > 0 '
        else:
            self.client_table_filters += f'device_type = "{self.comboBoxGadgetType.currentText().lower()}" '

        if self.comboBoxIsFixed == 'Всі':
            self.client_table_filters += ''
        elif self.comboBoxIsFixed.currentText() == 'В процесі':
            self.client_table_filters += 'AND is_fixed = "0" '
        elif self.comboBoxIsFixed.currentText() == 'Видано':
            self.client_table_filters += 'AND is_fixed = "1" '

        if self.comboBoxSearchFilter.currentText() == 'Модель':
            self.client_table_filters += f'AND brand LIKE "%{self.lineEditSearch.text().lower()}%" '
        elif self.comboBoxSearchFilter.currentText() == 'ПІБ':
            self.client_table_filters += f'AND name LIKE "%{self.lineEditSearch.text().lower()}%" '
        elif self.comboBoxSearchFilter.currentText() == 'Телефон':
            self.client_table_filters += f'AND phone_number LIKE "%{self.lineEditSearch.text()}%" '
        self.paste_in_clients_table()

    def open_selected(self, row, col):
        self.selected_user_id = int(self.tableWidgetClients.item(row, 0).text())
        self.tab.setTabVisible(2, True)
        columns = 'device_type, package, break_fix, price, warranty, in_date, client_rate'
        self.client_table_filters = 'WHERE '
        self.client_table_filters += f'id = {self.tableWidgetClients.item(row, 0).text()} '
        data = extract_clients_data(columns, self.client_table_filters)
        in_date_datetime = datetime.strptime(data[0][5], '%Y-%m-%d %H:%M:%S')
        self.lineEditCouponPhoneNum.setText(self.tableWidgetClients.item(row, 4).text())
        self.lineEditCouponName.setText(self.tableWidgetClients.item(row, 3).text())
        self.lineEditCouponModel.setText(self.tableWidgetClients.item(row, 2).text())
        self.lineEditCouponBreakage.setText(self.tableWidgetClients.item(row, 5).text())
        if data:
            self.lineEditCouponPackage.setText(data[0][0])
            self.lineEditCouponAdditionalPack.setText(data[0][1])
            self.lineEditCouponBreakFix.setText(data[0][2])
            self.spinBoxCouponPrice.setValue(int(data[0][3]))
            self.spinBoxCouponWarranty.setValue(int(data[0][4][0:-4]))
            self.label_CouponDate.setText(f"{str(in_date_datetime.day)} "
                                          f"{calendar.month_name[in_date_datetime.month]} "
                                          f"{data[0][5][0:4]} ")
            if data[0][6] == 'blacklist':
                self.radioButtonClientRateBlack.setChecked(True)
            elif data[0][6] == 'normal':
                self.radioButtonClientRateNorm.setChecked(True)
            elif data[0][6] == 'perfect':
                self.radioButtonClientRatePerfect.setChecked(True)

        self.line_edit_break_fix_old_text = ''
        self.break_fix_input_prediction()
        self.tab.setCurrentIndex(2)
        self.lineEditCouponBreakFix.setFocus()

    def new_order_check_all_fields(self):
        if len(self.lineEditCreateTabPhoneNum.text()) < 10:
            self.lineEditCreateTabPhoneNum.setFocus()
            return
        if self.lineEditCreateTabName.text() == '':
            self.lineEditCreateTabName.setFocus()
            return
        if self.lineEditCreateTabModel.text() == '':
            self.lineEditCreateTabModel.setFocus()
            return
        if self.lineEditCreateTabBreakage.text() == '':
            self.lineEditCreateTabBreakage.setFocus()
            return
        self.save_new_order()

    def new_order_clean_all(self):
        self.lineEditCreateTabPhoneNum.clear()
        self.new_order_clean()

    def new_order_clean(self):
        self.lineEditCreateTabName.clear()
        self.lineEditCreateTabModel.clear()
        self.lineEditCreateTabAdditionalPack.clear()
        self.lineEditCreateTabBreakage.clear()
        self.is_previous_orders = False
        self.line_edit_model_2_old_text = ''
        self.line_edit_additional_package_old_text = ''
        self.line_edit_phone_breakage_2_old_text = ''
        self.create_tab_input_prediction()
        self.additional_package_input_prediction()
        self.create_tab_phone_breakage_prediction()
        self.tableWidget.clear()
        self.current_client_rate = 'normal'
        self.label_InBlackList.setText('')

    def show_previous_orders(self):
        if self.is_previous_orders:
            self.comboBoxSearchFilter.setCurrentText('ПІБ')
            self.lineEditSearch.setText(self.lineEditCreateTabName.text())
            self.change_search_filter()
            self.paste_in_clients_table()
            self.tab.setCurrentIndex(0)

    def find_previous_orders(self):
        self.current_client_rate = 'normal'
        columns = 'in_date, brand, name, phone_number, breakage, id, client_rate, break_fix, client_rate'
        phone_number = self.lineEditCreateTabPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        search_line = f'WHERE phone_number = "{phone_number}" '
        previous_orders = extract_clients_data(columns, search_line)
        if previous_orders:
            self.lineEditCreateTabName.setText(previous_orders[0][2].title())
            self.lineEditCreateTabModel.setFocus()
            self.is_previous_orders = True
            row = 0
            self.tableWidget.setRowCount(len(previous_orders))
            for order in previous_orders:
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(order[0][0:10])))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(order[1].capitalize()))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(order[4].title()))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(order[7].title()))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(order[8].title()))
                row += 1
                if order[8] == 'blacklist':
                    self.current_client_rate = 'blacklist'
                if self.current_client_rate != 'blacklist' and order[8] == 'perfect':
                    self.current_client_rate = 'perfect'
                if self.current_client_rate == 'blacklist' and order[8] == 'perfect':
                    self.current_client_rate = 'normal'
        elif len(phone_number) == 10:
            self.lineEditCreateTabName.setFocus()
            self.is_previous_orders = False
        else:
            self.is_previous_orders = False
        self.label_InBlackList.setText('')
        if self.current_client_rate == 'perfect':
            self.label_InBlackList.setText('Почесний Клієнт  ')
        elif len(previous_orders) > 5:
            self.label_InBlackList.setText('Постійний клієнт')

    def save_new_order(self):
        columns = 'phone_number, name, brand, device_type, package, breakage, in_date'
        order_string = ''
        in_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phone_number = self.lineEditCreateTabPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        order_string += f'"{phone_number}", '
        order_string += f'"{self.lineEditCreateTabName.text().lower()}", '
        order_string += f'"{self.lineEditCreateTabModel.text().lower()}", '
        order_string += f'"{self.comboBoxCreateTabPackage.currentText().lower()}", '
        order_string += f'"{self.lineEditCreateTabAdditionalPack.text().lower()}", '
        order_string += f'"{self.lineEditCreateTabBreakage.text().lower()}", '
        order_string += f'"{in_date}" '
        save_new_order(columns, order_string)
        self.add_to_log('Збережено ' + self.lineEditCreateTabName.text())
        if self.checkBoxAutoprint.isChecked():
            self.print_list = [self.lineEditCreateTabModel.text(), self.comboBoxCreateTabPackage.currentText() + ' ' +
                               self.lineEditCreateTabAdditionalPack.text().lower(), self.lineEditCreateTabBreakage.text(),
                               self.lineEditCreateTabName.text().title(), phone_number,
                               self.settings_dict['additional_print_line1'],
                               self.settings_dict['additional_print_line2'],
                               self.settings_dict['additional_print_line3']]
            self.print_path = paste_to_order(self.print_list)
            self.ready_to_print = self.spinBoxPrintCopyAmount.value()
            self.add_to_log(f'Друк прийомка {self.lineEditCreateTabName.text()}')
        self.paste_in_clients_table()
        self.tab.setCurrentIndex(0)
        self.new_order_clean_all()

    def save_warranty_or_order_change(self):
        columns = ('phone_number, name, brand, device_type, package, '
                   'breakage, break_fix, price, out_date, is_fixed, warranty, client_rate')
        order_string = ''
        out_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phone_number = self.lineEditCouponPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        order_string += f'"{phone_number}", '
        order_string += f'"{self.lineEditCouponName.text().lower()}", '
        order_string += f'"{self.lineEditCouponModel.text().lower()}", '
        order_string += f'"{self.lineEditCouponPackage.text().lower()}", '
        order_string += f'"{self.lineEditCouponAdditionalPack.text().lower()}", '
        order_string += f'"{self.lineEditCouponBreakage.text().lower()}", '
        order_string += f'"{self.lineEditCouponBreakFix.text().lower()}", '
        order_string += f'{str(self.spinBoxCouponPrice.value())}, '
        order_string += f'"{out_date}", '
        if self.lineEditCouponBreakFix.text():
            order_string += '1, '
        else:
            order_string += '0, '
        order_string += f'"{str(self.spinBoxCouponWarranty.value())} міс.", '
        if self.radioButtonClientRateBlack.isChecked():
            order_string += '"blacklist"'
        elif self.radioButtonClientRatePerfect.isChecked():
            order_string += '"perfect"'
        elif self.radioButtonClientRateNorm.isChecked():
            order_string += '"normal"'
        save_warranty(columns, order_string, self.selected_user_id)
        self.add_to_log('Збережено ' + self.lineEditCouponName.text())
        self.client_table_filters = ''
        self.paste_in_clients_table()
        self.tab.setCurrentIndex(0)
        self.tab.setTabVisible(2, False)

    def print_warranty(self):
        out_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phone_number = self.lineEditCouponPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        if self.lineEditCouponBreakFix.text():
            self.warranty_print_list = [self.lineEditCouponModel.text(), self.lineEditCouponName.text().title(),
                                        phone_number, "", self.lineEditCouponBreakFix.text(),
                                        str(self.spinBoxCouponPrice.value()),
                                       f'{str(self.spinBoxCouponWarranty.value())} міс.']
            self.add_to_log(f'Друк гарантійний талон {self.warranty_print_list[1]}')
            self.print_path = paste_to_warranty(self.warranty_print_list)
            self.ready_to_print_warranty = 1
        else:
            self.print_list = [self.lineEditCouponModel.text(), self.lineEditCouponPackage.text() + ' ' +
                               self.lineEditCouponAdditionalPack.text().lower(), self.lineEditCouponBreakage.text(),
                               self.lineEditCouponName.text().title(), phone_number,
                               self.settings_dict['additional_print_line1'],
                               self.settings_dict['additional_print_line2'],
                               self.settings_dict['additional_print_line3']]
            self.add_to_log(f'Друк {self.lineEditCreateTabName.text()}')
            self.print_path = paste_to_order(self.print_list)
            self.ready_to_print = self.spinBoxPrintCopyAmount.value()
        columns = 'out_date, is_fixed'
        warranty_string = ''
        warranty_string += f'"{out_date}", '
        warranty_string += f'1'
        save_warranty(columns, warranty_string, self.selected_user_id)
        self.save_warranty_or_order_change()

    def open_client_xlsx(self):
        filter_name = self.lineEditCouponName.text().title().replace(' ', '_')
        default_dir = '../excel_files/saved_xlsx'
        matching_files = [f for f in os.listdir(default_dir) if filter_name in f]
        filter_line = " ".join(matching_files)
        file_path = ''
        if matching_files:
            file_path = QtWidgets.QFileDialog.getOpenFileName(None, "Open File", default_dir, f"({filter_line})")[0]
        if file_path:
            os.startfile(file_path)

    def break_fix_input_prediction(self):
        self.comboBoxCouponBreakFix.clear()
        if self.lineEditCouponBreakFix.text() == '':
            line_edit_text = f'WHERE breakage = "{self.lineEditCouponBreakage.text().lower()}" '
        else:
            line_edit_text = f'WHERE break_fix LIKE "%{self.lineEditCouponBreakFix.text().lower()}%" '
        self.comboBoxCouponBreakFix.addItems(get_must_use('break_fix', line_edit_text))
        latest_price = get_previous_price(line_edit_text)
        if latest_price:
            self.spinBoxCouponPrice.setValue(int(latest_price[0]))
        else:
            self.spinBoxCouponPrice.setValue(0)
        latest_warranty = get_must_use('warranty', line_edit_text)
        if latest_warranty:
            self.spinBoxCouponWarranty.setValue(int(latest_warranty[0][:-5]))
        else:
            self.spinBoxCouponWarranty.setValue(0)

    def combobox_break_fix_choice(self):
        self.lineEditCouponBreakFix.setText(self.comboBoxCouponBreakFix.currentText())

    def break_fix_return_pressed(self):
        if self.line_edit_break_fix_old_text > self.lineEditCouponBreakFix.text() or\
                self.lineEditCouponBreakFix.text() == self.comboBoxCouponBreakFix.currentText():
            self.spinBoxCouponPrice.setFocus()
        else:
            self.lineEditCouponBreakFix.setText(self.comboBoxCouponBreakFix.currentText())
        self.line_edit_break_fix_old_text = self.lineEditCouponBreakFix.text()

    def create_name_return_pressed(self):
        self.comboBoxCreateTabPackage.setFocus()

    def model_type_predict_filter(self):
        self.create_tab_input_prediction()
        self.additional_package_input_prediction()
        self.create_tab_phone_breakage_prediction()

    def create_tab_input_prediction(self):
        self.comboBoxCreateTabModel.clear()
        if self.lineEditCreateTabModel.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE brand LIKE "%{self.lineEditCreateTabModel.text().lower()}%" '
        self.comboBoxCreateTabModel.addItems(get_must_use(
            'brand', line_edit_text))

    def create_tab_combobox_model_activated(self):
        self.lineEditCreateTabModel.setText(self.comboBoxCreateTabModel.currentText())

    def create_tab_return_pressed(self):
        if self.line_edit_model_2_old_text > self.lineEditCreateTabModel.text() or\
                self.lineEditCreateTabModel.text() == self.comboBoxCreateTabModel.currentText():
            self.lineEditCreateTabAdditionalPack.setFocus()
        else:
            self.lineEditCreateTabModel.setText(self.comboBoxCreateTabModel.currentText())
        self.line_edit_model_2_old_text = self.lineEditCreateTabModel.text()

    def additional_package_input_prediction(self):
        self.comboBoxCreateTabAdditionalPack.clear()
        if self.lineEditCreateTabAdditionalPack.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE package LIKE "%{self.lineEditCreateTabAdditionalPack.text().lower()}%" '
        self.comboBoxCreateTabAdditionalPack.addItems(get_must_use(
            'package', line_edit_text))

    def combobox_additional_package_choice(self):
        self.lineEditCreateTabAdditionalPack.setText(self.comboBoxCreateTabAdditionalPack.currentText())

    def additional_package_return_pressed(self):
        if self.line_edit_additional_package_old_text > self.lineEditCreateTabAdditionalPack.text() or\
                self.lineEditCreateTabAdditionalPack.text() == self.comboBoxCreateTabAdditionalPack.currentText() or\
                self.comboBoxCreateTabAdditionalPack.currentText() == '':
            self.lineEditCreateTabBreakage.setFocus()
        else:
            self.lineEditCreateTabAdditionalPack.setText(self.comboBoxCreateTabAdditionalPack.currentText())
        self.line_edit_additional_package_old_text = self.lineEditCreateTabAdditionalPack.text()

    def create_tab_phone_breakage_prediction(self):
        self.comboBoxCreateTabBreakage.clear()
        if self.lineEditCreateTabBreakage.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE breakage LIKE "%{self.lineEditCreateTabBreakage.text().lower()}%" '
        self.comboBoxCreateTabBreakage.addItems(get_must_use(
            'breakage', line_edit_text))

    def create_tab_combobox_breakage_activated(self):
        self.lineEditCreateTabBreakage.setText(self.comboBoxCreateTabBreakage.currentText())

    def create_tab_phone_breakage_return_pressed(self):
        if self.line_edit_phone_breakage_2_old_text > self.lineEditCreateTabBreakage.text() or\
                self.lineEditCreateTabBreakage.text() == self.comboBoxCreateTabBreakage.currentText() or\
                self.comboBoxCreateTabBreakage.currentText() == '':
            self.pushButtonCreateTabSave.setFocus()
        else:
            self.lineEditCreateTabBreakage.setText(self.comboBoxCreateTabBreakage.currentText())
        self.line_edit_phone_breakage_2_old_text = self.lineEditCreateTabBreakage.text()

    def paste_in_radios_table(self):
        columns = 'id, name, url, is_play'
        data = extract_radios_data(columns)
        self.tableWidgetRadioStations.setRowCount(len(data))
        if data:
            row = 0
            for radio in data:
                self.tableWidgetRadioStations.setItem(row, 0, QtWidgets.QTableWidgetItem(radio[1].title()))
                self.tableWidgetRadioStations.setItem(row, 1, QtWidgets.QTableWidgetItem(radio[2]))
                self.tableWidgetRadioStations.setItem(row, 2, QtWidgets.QTableWidgetItem('DEL'))
                self.tableWidgetRadioStations.setItem(row, 3, QtWidgets.QTableWidgetItem(str(radio[0])))
                row += 1
                if radio[3]:
                    self.radio_current_url = radio[2]
        self.lineEditRadioUrl.clear()
        self.lineEditRadioName.clear()

    def click_to_play(self, row, col):
        radio_url = self.tableWidgetRadioStations.item(row, 1).text()
        if col == 2:
            self.radio_del_candidate_id = self.tableWidgetRadioStations.item(row, 3).text()
            self.radio_del_candidate_name = self.tableWidgetRadioStations.item(row, 0).text()
            self.open_confirm_form(f'Видалити {self.radio_del_candidate_name}?',
                                   self.del_station)
            self.paste_in_radios_table()
        else:
            self.radio_current_name = self.tableWidgetRadioStations.item(row, 0).text()
            save_radio_choice('is_play', '"0"', f'WHERE url <> "{radio_url}" ')
            save_radio_choice('is_play', '"1"', f'WHERE url = "{radio_url}" ')
            self.paste_in_radios_table()
            self.settings_dict['radio_current_url'] = radio_url
            self.settings_dict['radio_current_name'] = self.radio_current_name
            self.enable_radio()

    def del_station(self):
        del_station(self.radio_del_candidate_id)
        self.paste_in_radios_table()

    def open_confirm_form(self, header, function):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindowConfirmForm()
        self.ui.setupUi(self.window, header, self.window.close, function)
        self.window.show()

    def enable_radio(self):
        self.radio_is_playing = True
        self.labelRadioStationIsPlaying.setText(f'Станція {self.radio_current_name}')


    def disable_radio(self):
        if self.radio_is_playing:
            self.add_to_log('Радіо стоп')
        self.radio_is_playing = False
        self.labelRadioStationIsPlaying.setText('')
        self.labelRadioCurrentSong.setText('')

    def show_current_song(self):
        self.labelRadioCurrentSong.setText(self.radio_current_song)

    def extract_radios_from_cloud(self):
        if self.cloud_radio_num < 1:
            token = login(self.settings_dict['mega_user'],
                          self.settings_dict['mega_pass'])
            self.radios_data = get_from_firebase(token, 'radios')
            self.cloud_radio_num = len(self.radios_data) - 1
            print(self.radios_data[self.cloud_radio_num])
            self.lineEditRadioUrl.setText(self.radios_data[self.cloud_radio_num]['url'])
            self.lineEditRadioName.setText(self.radios_data[self.cloud_radio_num]['name'])
        else:
            self.lineEditRadioUrl.setText(self.radios_data[self.cloud_radio_num]['url'])
            self.lineEditRadioName.setText(self.radios_data[self.cloud_radio_num]['name'])
        self.cloud_radio_num -= 1




    def save_new_station(self):
        name = self.lineEditRadioName.text()
        url = self.lineEditRadioUrl.text()
        if name != '' and url != '':
            save_new_station(name, url)
            self.paste_in_radios_table()


    def save_settings(self):
        self.settings_dict['auto_sync_time'] = str(self.spinBoxBackupTime.value())
        if self.checkBoxAutobackup.isChecked():
            self.settings_dict['auto_sync'] = 'True'
        else:
            self.settings_dict['auto_sync'] = ''
        if self.checkBoxAutoprint.isChecked():
            self.settings_dict['auto_print'] = 'True'
        else:
            self.settings_dict['auto_print'] = ''
        self.settings_dict['copies'] = str(self.spinBoxPrintCopyAmount.value())
        self.settings_dict['pause_between_copies'] = str(self.spinBoxPauseBetweenCopies.value())

        self.settings_dict['radio_current_name'] = self.radio_current_name

        self.settings_dict['radio_is_playing'] = str(int(self.checkBoxRadioAutoPlay.isChecked()))
        self.settings_dict['radio_volume_level'] = str(self.horizontalSliderRadioLoud.value())
        self.settings_dict['additional_print_line1'] = self.lineEditAdditional_info1.text()
        self.settings_dict['additional_print_line2'] = self.lineEditAdditional_info2.text()
        self.settings_dict['additional_print_line3'] = self.lineEditAdditional_info3.text()
        self.settings_dict['theme'] = self.comboBoxColorTheme.currentText()
        save_settings(self.settings_dict)

    def sync_with_cloud(self):
        if self.settings_dict['mega_user'] and self.settings_dict['mega_pass']:
            self.db_ready_to_sync = True
        else:
            self.open_sing_up_form()

    def change_color_theme(self):
        if self.comboBoxColorTheme.currentText() == 'Світла':
            self.centralwidget.setStyleSheet(MyThemes.white_central_widget)
            self.widget_18.setStyleSheet(MyThemes.white_widget_18)
            self.frame_4.setStyleSheet(MyThemes.white_frame_4)
        elif self.comboBoxColorTheme.currentText() == 'Темна':
            self.centralwidget.setStyleSheet(MyThemes.black_central_widget)
            self.widget_18.setStyleSheet(MyThemes.black_widget_18)
            self.frame_4.setStyleSheet(MyThemes.black_frame_4)

    def add_to_log(self, item=False):
        item = str(item)[:156]
        if item:
            if len(str(item)) > 80:
                item = f'{str(item)[0: 78]} \n {str(item)[78:-1]}'
            self.current_log = str(item)
            self.labelLog.setText(str(datetime.now())[11: 19] + ' ' + self.current_log)


def run_gui():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        ui.save_settings()
