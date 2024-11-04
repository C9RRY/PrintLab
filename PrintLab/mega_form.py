from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogMegaLogin(object):
    def setupUi(self, DialogMegaLogin, main_self):
        self.main_self = main_self
        DialogMegaLogin.setObjectName("DialogMegaLogin")
        DialogMegaLogin.resize(469, 204)
        DialogMegaLogin.setStyleSheet("font-size: 20px;")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DialogMegaLogin.sizePolicy().hasHeightForWidth())
        DialogMegaLogin.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QtWidgets.QGridLayout(DialogMegaLogin)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(parent=DialogMegaLogin)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(parent=self.frame)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEditLogin = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.gridLayout_3.addWidget(self.lineEditLogin, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setMinimumSize(QtCore.QSize(0, 35))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.checkBoxShowPassword = QtWidgets.QCheckBox(parent=self.widget)
        self.checkBoxShowPassword.setObjectName("checkBoxShowPassword")
        self.verticalLayout.addWidget(self.checkBoxShowPassword)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.widget, 1, 1, 2, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.widget_3 = QtWidgets.QWidget(parent=self.frame)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(281, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButtonConfirm = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout.addWidget(self.pushButtonConfirm)
        self.gridLayout.addWidget(self.widget_3, 3, 1, 1, 1)
        self.gridLayout_2.addWidget(self.frame, 0, 0, 1, 1)

        self.is_clear_first = True
        self.real_pass = self.main_self.settings_dict['mega_pass']

        self.lineEditPassword.textChanged.connect(self.check_pass_symbols)
        self.lineEditLogin.textChanged.connect(self.check_login_symbols)
        self.checkBoxShowPassword.stateChanged.connect(self.pass_hide_change)
        self.pushButtonConfirm.clicked.connect(self.confirm_auth)

        self.retranslateUi(DialogMegaLogin)
        QtCore.QMetaObject.connectSlotsByName(DialogMegaLogin)

    def retranslateUi(self, DialogMegaLogin):
        _translate = QtCore.QCoreApplication.translate
        DialogMegaLogin.setWindowTitle(_translate("DialogMegaLogin", "Mega"))
        self.label.setText(_translate("DialogMegaLogin", "Логін"))
        self.label_2.setText(_translate("DialogMegaLogin", "Пароль"))
        self.checkBoxShowPassword.setText(_translate("DialogMegaLogin", "Показати"))
        self.pushButtonConfirm.setText(_translate("DialogMegaLogin", "Увійти"))
        self.paste_if_logged()

    def paste_if_logged(self):
        if self.main_self.settings_dict['mega_user']:
            self.lineEditLogin.setText(self.main_self.settings_dict['mega_user'])
            if self.main_self.settings_dict['mega_pass']:
                self.lineEditPassword.blockSignals(True)
                self.lineEditPassword.setText('*' * len(self.main_self.settings_dict['mega_pass']))
                self.lineEditPassword.blockSignals(False)

    def first_pass_clear(self):
        if self.is_clear_first:
            if len(self.lineEditPassword.text()) >= len(self.main_self.settings_dict['mega_pass']):
                self.lineEditPassword.blockSignals(True)
                self.lineEditPassword.setText('')
                self.lineEditPassword.blockSignals(False)
                self.real_pass = ''
                self.is_clear_first = False

    def pass_hide_change(self):
        if self.checkBoxShowPassword.isChecked():
            self.first_pass_clear()
            self.lineEditPassword.setText(self.real_pass)
        else:
            self.lineEditPassword.setText('*' * len(self.real_pass))

    def check_pass_symbols(self):
        self.lineEditPassword.blockSignals(True)
        bad_symbols = " "
        if any(symbol in self.lineEditPassword.text() for symbol in bad_symbols):
            self.lineEditPassword.setText(''.join([s for s in self.lineEditPassword.text() if s not in bad_symbols]))
        if len(self.lineEditPassword.text()) != len(self.real_pass):
            self.write_the_pass()
        self.lineEditPassword.blockSignals(False)

    def write_the_pass(self):
        self.first_pass_clear()
        if self.lineEditPassword.text() and self.real_pass:
            if len(self.real_pass) > len(self.lineEditPassword.text()) and not self.checkBoxShowPassword.isChecked():
                self.lineEditPassword.setText('')
                self.real_pass = ''
        if self.lineEditPassword.text():
            if not self.checkBoxShowPassword.isChecked():
                self.real_pass += self.lineEditPassword.text()[-1]
                self.lineEditPassword.setText('*' * len(self.lineEditPassword.text()))
            else:
                self.real_pass = self.lineEditPassword.text()
        else:
            self.real_pass = ''
        self.lineEditPassword.blockSignals(False)

    def check_login_symbols(self):
        self.lineEditLogin.blockSignals(True)
        bad_symbols = "!#$%&*+/=?^{|}~,:;<>()[]\\\" "
        if any(symbol in self.lineEditLogin.text() for symbol in bad_symbols):
            self.lineEditLogin.setText(''.join([s for s in self.lineEditLogin.text() if s not in bad_symbols]))
        if len(self.lineEditLogin.text()) != len(self.real_pass):
            self.write_the_pass()
        self.lineEditLogin.blockSignals(False)

    def confirm_auth(self):
        if not self.lineEditLogin.text():
            self.lineEditLogin.setFocus()
        if not self.lineEditPassword.text():
            self.lineEditPassword.setFocus()
        if self.lineEditLogin.text() and self.lineEditPassword.text():
            self.main_self.settings_dict['mega_user'] = self.lineEditLogin.text()
            self.main_self.settings_dict['mega_pass'] = self.real_pass
            self.main_self.auth_has_been_changed = True
            self.main_self.sync_with_cloud()
            self.main_self.mega_window.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogMegaLogin = QtWidgets.QDialog()
    ui = Ui_DialogMegaLogin()
    ui.setupUi(DialogMegaLogin, main_self={})
    DialogMegaLogin.show()
    sys.exit(app.exec())
