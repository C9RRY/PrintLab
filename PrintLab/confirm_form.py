from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindowConfirmForm(object):
    def setupUi(self, MainWindowConfirmForm, header, self_close, function):
        self.header = header
        self.close_app = self_close
        self.function = function
        MainWindowConfirmForm.setObjectName("MainWindowConfirmForm")
        MainWindowConfirmForm.resize(417, 138)
        MainWindowConfirmForm.setStyleSheet("font-size: 20px;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindowConfirmForm)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=self.frame)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QtCore.QSize(0, 35))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(212, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonConfirm = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonConfirm.setObjectName("pushButtonConfirm")
        self.horizontalLayout.addWidget(self.pushButtonConfirm)
        self.pushButtonCancel = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)
        MainWindowConfirmForm.setCentralWidget(self.centralwidget)

        self.pushButtonConfirm.clicked.connect(self.main_function)
        self.pushButtonCancel.clicked.connect(self.cancel_deleting)

        self.retranslateUi(MainWindowConfirmForm)
        QtCore.QMetaObject.connectSlotsByName(MainWindowConfirmForm)

    def retranslateUi(self, MainWindowConfirmForm):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("MainWindowConfirmForm",
                                      self.header))
        self.pushButtonConfirm.setText(_translate("MainWindowConfirmForm", "Так"))
        self.pushButtonCancel.setText(_translate("MainWindowConfirmForm", "Скасувати"))

    def main_function(self):
        self.function()
        self.close_app()

    def cancel_deleting(self):
        self.close_app()

