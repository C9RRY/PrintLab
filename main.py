from datetime import datetime
from coupon_print import paste_to_order, paste_to_warranty
from database import (extract_clients_data, save_new_order, save_warranty, get_must_use, save_settings, del_station,
                      save_radio_choice, save_new_station, extract_settings, extract_radios_data, extract_from_backup)
import calendar
import pathlib
import shutil
from additional_thread import RadioAndAutoprintThread
from models import create_all
from mega_form import Ui_DialogMegaLogin
from confirm_form import Ui_MainWindowConfirmForm
from PyQt6 import QtCore, QtGui, QtWidgets


dir_path = pathlib.Path(__file__).parent.resolve()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 663)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.labelLog = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.labelLog.setFont(font)
        self.labelLog.setObjectName("labelLog")
        self.gridLayout_2.addWidget(self.labelLog, 1, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tab = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tab.setObjectName("tab")
        self.tabClientTable = QtWidgets.QWidget()
        self.tabClientTable.setObjectName("tabClientTable")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.tabClientTable)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.tabClientTable)
        self.label_2.setObjectName("label_2")
        self.gridLayout_4.addWidget(self.label_2, 1, 3, 1, 1)
        self.comboBoxGadgetType = QtWidgets.QComboBox(parent=self.tabClientTable)
        self.comboBoxGadgetType.setMinimumSize(QtCore.QSize(200, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBoxGadgetType.setFont(font)
        self.comboBoxGadgetType.setStyleSheet("")
        self.comboBoxGadgetType.setObjectName("comboBoxGadgetType")
        self.gridLayout_4.addWidget(self.comboBoxGadgetType, 1, 1, 1, 1)
        self.comboBoxIsFixed = QtWidgets.QComboBox(parent=self.tabClientTable)
        self.comboBoxIsFixed.setMinimumSize(QtCore.QSize(200, 0))
        self.comboBoxIsFixed.setObjectName("comboBoxIsFixed")
        self.gridLayout_4.addWidget(self.comboBoxIsFixed, 1, 5, 1, 1)
        self.label_31 = QtWidgets.QLabel(parent=self.tabClientTable)
        self.label_31.setObjectName("label_31")
        self.gridLayout_4.addWidget(self.label_31, 1, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidgetClients = QtWidgets.QTableWidget(parent=self.tabClientTable)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidgetClients.sizePolicy().hasHeightForWidth())
        self.tableWidgetClients.setSizePolicy(sizePolicy)
        self.tableWidgetClients.setMaximumSize(QtCore.QSize(16000, 16000))
        self.tableWidgetClients.setObjectName("tableWidgetClients")
        self.tableWidgetClients.setColumnCount(7)
        self.tableWidgetClients.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetClients.setHorizontalHeaderItem(6, item)
        self.tableWidgetClients.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidgetClients)
        self.gridLayout_5.addLayout(self.verticalLayout, 1, 0, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(235, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_5.addItem(spacerItem1, 2, 0, 1, 1)
        self.widget_18 = QtWidgets.QWidget(parent=self.tabClientTable)
        self.widget_18.setObjectName("widget_18")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.widget_18)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label = QtWidgets.QLabel(parent=self.widget_18)
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label)
        self.comboBoxSearchFilter = QtWidgets.QComboBox(parent=self.widget_18)
        self.comboBoxSearchFilter.setMinimumSize(QtCore.QSize(140, 0))
        self.comboBoxSearchFilter.setObjectName("comboBoxSearchFilter")
        self.horizontalLayout_7.addWidget(self.comboBoxSearchFilter)
        self.lineEditSearch = QtWidgets.QLineEdit(parent=self.widget_18)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(250, 0))
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.horizontalLayout_7.addWidget(self.lineEditSearch)
        self.gridLayout_5.addWidget(self.widget_18, 2, 1, 1, 1)
        self.tab.addTab(self.tabClientTable, "")
        self.tabCreate = QtWidgets.QWidget()
        self.tabCreate.setObjectName("tabCreate")
        self.gridLayout_18 = QtWidgets.QGridLayout(self.tabCreate)
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.widget_2 = QtWidgets.QWidget(parent=self.tabCreate)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEditCreateTabPhoneNum = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditCreateTabPhoneNum.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEditCreateTabPhoneNum.setObjectName("lineEditCreateTabPhoneNum")
        self.gridLayout.addWidget(self.lineEditCreateTabPhoneNum, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.comboBoxCreateTabPackage = QtWidgets.QComboBox(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCreateTabPackage.sizePolicy().hasHeightForWidth())
        self.comboBoxCreateTabPackage.setSizePolicy(sizePolicy)
        self.comboBoxCreateTabPackage.setObjectName("comboBoxCreateTabPackage")
        self.gridLayout.addWidget(self.comboBoxCreateTabPackage, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEditCreateTabModel = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditCreateTabModel.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEditCreateTabModel.setObjectName("lineEditCreateTabModel")
        self.gridLayout.addWidget(self.lineEditCreateTabModel, 3, 1, 1, 1)
        self.comboBoxCreateTabModel = QtWidgets.QComboBox(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCreateTabModel.sizePolicy().hasHeightForWidth())
        self.comboBoxCreateTabModel.setSizePolicy(sizePolicy)
        self.comboBoxCreateTabModel.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxCreateTabModel.setObjectName("comboBoxCreateTabModel")
        self.gridLayout.addWidget(self.comboBoxCreateTabModel, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)
        self.lineEditCreateTabAdditionalPack = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditCreateTabAdditionalPack.setMinimumSize(QtCore.QSize(300, 0))
        self.lineEditCreateTabAdditionalPack.setObjectName("lineEditCreateTabAdditionalPack")
        self.gridLayout.addWidget(self.lineEditCreateTabAdditionalPack, 4, 1, 1, 1)
        self.comboBoxCreateTabAdditionalPack = QtWidgets.QComboBox(parent=self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxCreateTabAdditionalPack.sizePolicy().hasHeightForWidth())
        self.comboBoxCreateTabAdditionalPack.setSizePolicy(sizePolicy)
        self.comboBoxCreateTabAdditionalPack.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxCreateTabAdditionalPack.setObjectName("comboBoxCreateTabAdditionalPack")
        self.gridLayout.addWidget(self.comboBoxCreateTabAdditionalPack, 4, 2, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 0, 1, 1)
        self.lineEditCreateTabName = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditCreateTabName.setObjectName("lineEditCreateTabName")
        self.gridLayout.addWidget(self.lineEditCreateTabName, 1, 1, 1, 1)
        self.lineEditCreateTabBreakage = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEditCreateTabBreakage.setObjectName("lineEditCreateTabBreakage")
        self.gridLayout.addWidget(self.lineEditCreateTabBreakage, 5, 1, 1, 2)
        self.comboBoxCreateTabBreakage = QtWidgets.QComboBox(parent=self.widget_2)
        self.comboBoxCreateTabBreakage.setObjectName("comboBoxCreateTabBreakage")
        self.gridLayout.addWidget(self.comboBoxCreateTabBreakage, 6, 1, 1, 2)
        self.gridLayout_18.addWidget(self.widget_2, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(parent=self.tabCreate)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.pushButtonCreateTabPreviousOrders = QtWidgets.QPushButton(parent=self.frame_2)
        self.pushButtonCreateTabPreviousOrders.setObjectName("pushButtonCreateTabPreviousOrders")
        self.gridLayout_20.addWidget(self.pushButtonCreateTabPreviousOrders, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(552, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_20.addItem(spacerItem2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frame_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.gridLayout_20.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.gridLayout_18.addWidget(self.frame_2, 1, 0, 1, 1)
        self.widget = QtWidgets.QWidget(parent=self.tabCreate)
        self.widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.MinimumExpanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButtonCreateTabClear = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonCreateTabClear.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButtonCreateTabClear.setObjectName("pushButtonCreateTabClear")
        self.horizontalLayout_2.addWidget(self.pushButtonCreateTabClear)
        self.pushButtonCreateTabSave = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonCreateTabSave.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButtonCreateTabSave.setObjectName("pushButtonCreateTabSave")
        self.horizontalLayout_2.addWidget(self.pushButtonCreateTabSave)
        self.gridLayout_18.addWidget(self.widget, 2, 0, 1, 1)
        self.tab.addTab(self.tabCreate, "")
        self.tabOutCheck = QtWidgets.QWidget()
        self.tabOutCheck.setObjectName("tabOutCheck")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tabOutCheck)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.widget_8 = QtWidgets.QWidget(parent=self.tabOutCheck)
        self.widget_8.setObjectName("widget_8")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.widget_8)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.widget_9 = QtWidgets.QWidget(parent=self.widget_8)
        self.widget_9.setObjectName("widget_9")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.widget_9)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.label_18 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_18.setObjectName("label_18")
        self.gridLayout_12.addWidget(self.label_18, 0, 0, 1, 1)
        self.lineEditCouponPhoneNum = QtWidgets.QLineEdit(parent=self.widget_9)
        self.lineEditCouponPhoneNum.setObjectName("lineEditCouponPhoneNum")
        self.gridLayout_12.addWidget(self.lineEditCouponPhoneNum, 0, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_19.setObjectName("label_19")
        self.gridLayout_12.addWidget(self.label_19, 1, 0, 1, 1)
        self.lineEditCouponName = QtWidgets.QLineEdit(parent=self.widget_9)
        self.lineEditCouponName.setObjectName("lineEditCouponName")
        self.gridLayout_12.addWidget(self.lineEditCouponName, 1, 1, 1, 1)
        self.label_20 = QtWidgets.QLabel(parent=self.widget_9)
        self.label_20.setObjectName("label_20")
        self.gridLayout_12.addWidget(self.label_20, 2, 0, 1, 1)
        self.lineEditCouponModel = QtWidgets.QLineEdit(parent=self.widget_9)
        self.lineEditCouponModel.setObjectName("lineEditCouponModel")
        self.gridLayout_12.addWidget(self.lineEditCouponModel, 2, 1, 1, 1)
        self.gridLayout_15.addWidget(self.widget_9, 0, 0, 1, 1)
        self.widget_10 = QtWidgets.QWidget(parent=self.widget_8)
        self.widget_10.setObjectName("widget_10")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.widget_10)
        self.gridLayout_14.setObjectName("gridLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_14.addItem(spacerItem4, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 47, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_14.addItem(spacerItem5, 2, 0, 1, 1)
        self.label_CouponDate = QtWidgets.QLabel(parent=self.widget_10)
        self.label_CouponDate.setMinimumSize(QtCore.QSize(150, 0))
        self.label_CouponDate.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_CouponDate.setObjectName("label_CouponDate")
        self.gridLayout_14.addWidget(self.label_CouponDate, 1, 0, 1, 1)
        self.gridLayout_15.addWidget(self.widget_10, 0, 1, 1, 1)
        self.widget_11 = QtWidgets.QWidget(parent=self.widget_8)
        self.widget_11.setObjectName("widget_11")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.widget_11)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.label_21 = QtWidgets.QLabel(parent=self.widget_11)
        self.label_21.setObjectName("label_21")
        self.gridLayout_13.addWidget(self.label_21, 0, 0, 1, 1)
        self.lineEditCouponPackage = QtWidgets.QLineEdit(parent=self.widget_11)
        self.lineEditCouponPackage.setObjectName("lineEditCouponPackage")
        self.gridLayout_13.addWidget(self.lineEditCouponPackage, 0, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(parent=self.widget_11)
        self.label_23.setMinimumSize(QtCore.QSize(120, 0))
        self.label_23.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_23.setObjectName("label_23")
        self.gridLayout_13.addWidget(self.label_23, 0, 2, 1, 1)
        self.lineEditCouponAdditionalPack = QtWidgets.QLineEdit(parent=self.widget_11)
        self.lineEditCouponAdditionalPack.setObjectName("lineEditCouponAdditionalPack")
        self.gridLayout_13.addWidget(self.lineEditCouponAdditionalPack, 0, 3, 1, 1)
        self.label_22 = QtWidgets.QLabel(parent=self.widget_11)
        self.label_22.setObjectName("label_22")
        self.gridLayout_13.addWidget(self.label_22, 1, 0, 1, 1)
        self.lineEditCouponBreakage = QtWidgets.QLineEdit(parent=self.widget_11)
        self.lineEditCouponBreakage.setObjectName("lineEditCouponBreakage")
        self.gridLayout_13.addWidget(self.lineEditCouponBreakage, 1, 1, 1, 3)
        self.gridLayout_15.addWidget(self.widget_11, 1, 0, 1, 2)
        self.gridLayout_6.addWidget(self.widget_8, 0, 0, 1, 2)
        self.line_3 = QtWidgets.QFrame(parent=self.tabOutCheck)
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_6.addWidget(self.line_3, 1, 0, 1, 2)
        self.widget_12 = QtWidgets.QWidget(parent=self.tabOutCheck)
        self.widget_12.setObjectName("widget_12")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.widget_12)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.label_24 = QtWidgets.QLabel(parent=self.widget_12)
        self.label_24.setObjectName("label_24")
        self.gridLayout_16.addWidget(self.label_24, 0, 0, 1, 1)
        self.lineEditCouponBreakFix = QtWidgets.QLineEdit(parent=self.widget_12)
        self.lineEditCouponBreakFix.setObjectName("lineEditCouponBreakFix")
        self.gridLayout_16.addWidget(self.lineEditCouponBreakFix, 0, 1, 1, 1)
        self.comboBoxCouponBreakFix = QtWidgets.QComboBox(parent=self.widget_12)
        self.comboBoxCouponBreakFix.setObjectName("comboBoxCouponBreakFix")
        self.gridLayout_16.addWidget(self.comboBoxCouponBreakFix, 1, 1, 1, 1)
        self.widget_13 = QtWidgets.QWidget(parent=self.widget_12)
        self.widget_13.setObjectName("widget_13")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.widget_13)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem6)
        self.label_25 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_25.setMinimumSize(QtCore.QSize(90, 0))
        self.label_25.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_25.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.label_25.setObjectName("label_25")
        self.horizontalLayout_5.addWidget(self.label_25)
        self.spinBoxCouponPrice = QtWidgets.QSpinBox(parent=self.widget_13)
        self.spinBoxCouponPrice.setMinimumSize(QtCore.QSize(80, 0))
        self.spinBoxCouponPrice.setMaximum(1000000)
        self.spinBoxCouponPrice.setSingleStep(50)
        self.spinBoxCouponPrice.setObjectName("spinBoxCouponPrice")
        self.horizontalLayout_5.addWidget(self.spinBoxCouponPrice)
        self.label_27 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_27.setObjectName("label_27")
        self.horizontalLayout_5.addWidget(self.label_27)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem7)
        self.label_26 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_26.setMinimumSize(QtCore.QSize(110, 0))
        self.label_26.setObjectName("label_26")
        self.horizontalLayout_5.addWidget(self.label_26)
        self.spinBoxCouponWarranty = QtWidgets.QSpinBox(parent=self.widget_13)
        self.spinBoxCouponWarranty.setSingleStep(3)
        self.spinBoxCouponWarranty.setObjectName("spinBoxCouponWarranty")
        self.horizontalLayout_5.addWidget(self.spinBoxCouponWarranty)
        self.label_28 = QtWidgets.QLabel(parent=self.widget_13)
        self.label_28.setObjectName("label_28")
        self.horizontalLayout_5.addWidget(self.label_28)
        self.gridLayout_16.addWidget(self.widget_13, 2, 0, 1, 2)
        self.pushButtonOpenClientFile = QtWidgets.QPushButton(parent=self.widget_12)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonOpenClientFile.sizePolicy().hasHeightForWidth())
        self.pushButtonOpenClientFile.setSizePolicy(sizePolicy)
        self.pushButtonOpenClientFile.setMinimumSize(QtCore.QSize(30, 30))
        self.pushButtonOpenClientFile.setMaximumSize(QtCore.QSize(50, 40))
        self.pushButtonOpenClientFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonOpenClientFile.setIcon(icon)
        self.pushButtonOpenClientFile.setCheckable(True)
        self.pushButtonOpenClientFile.setObjectName("pushButtonOpenClientFile")
        self.gridLayout_16.addWidget(self.pushButtonOpenClientFile, 1, 0, 1, 1)
        self.gridLayout_6.addWidget(self.widget_12, 2, 0, 1, 2)
        self.widget_14 = QtWidgets.QWidget(parent=self.tabOutCheck)
        self.widget_14.setObjectName("widget_14")
        self.gridLayout_17 = QtWidgets.QGridLayout(self.widget_14)
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.label_29 = QtWidgets.QLabel(parent=self.widget_14)
        self.label_29.setObjectName("label_29")
        self.gridLayout_17.addWidget(self.label_29, 0, 0, 2, 1)
        self.widget_15 = QtWidgets.QWidget(parent=self.widget_14)
        self.widget_15.setMinimumSize(QtCore.QSize(140, 90))
        self.widget_15.setObjectName("widget_15")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_15)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radioButtonClientRateBlack = QtWidgets.QRadioButton(parent=self.widget_15)
        self.radioButtonClientRateBlack.setMinimumSize(QtCore.QSize(150, 30))
        self.radioButtonClientRateBlack.setObjectName("radioButtonClientRateBlack")
        self.verticalLayout_2.addWidget(self.radioButtonClientRateBlack)
        self.radioButtonClientRateNorm = QtWidgets.QRadioButton(parent=self.widget_15)
        self.radioButtonClientRateNorm.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButtonClientRateNorm.setChecked(True)
        self.radioButtonClientRateNorm.setObjectName("radioButtonClientRateNorm")
        self.verticalLayout_2.addWidget(self.radioButtonClientRateNorm)
        self.radioButtonClientRatePerfect = QtWidgets.QRadioButton(parent=self.widget_15)
        self.radioButtonClientRatePerfect.setMinimumSize(QtCore.QSize(0, 30))
        self.radioButtonClientRatePerfect.setObjectName("radioButtonClientRatePerfect")
        self.verticalLayout_2.addWidget(self.radioButtonClientRatePerfect)
        self.gridLayout_17.addWidget(self.widget_15, 2, 1, 1, 1)
        self.gridLayout_6.addWidget(self.widget_14, 3, 0, 2, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout_6.addItem(spacerItem8, 3, 1, 1, 1)
        self.widget_16 = QtWidgets.QWidget(parent=self.tabOutCheck)
        self.widget_16.setObjectName("widget_16")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget_16)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem9 = QtWidgets.QSpacerItem(169, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.pushButtonCouponSave = QtWidgets.QPushButton(parent=self.widget_16)
        self.pushButtonCouponSave.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButtonCouponSave.setObjectName("pushButtonCouponSave")
        self.horizontalLayout_6.addWidget(self.pushButtonCouponSave)
        self.pushButtonCouponPrint = QtWidgets.QPushButton(parent=self.widget_16)
        self.pushButtonCouponPrint.setMinimumSize(QtCore.QSize(110, 0))
        self.pushButtonCouponPrint.setObjectName("pushButtonCouponPrint")
        self.horizontalLayout_6.addWidget(self.pushButtonCouponPrint)
        self.gridLayout_6.addWidget(self.widget_16, 4, 1, 1, 1)
        self.tab.addTab(self.tabOutCheck, "")
        self.tabSettings = QtWidgets.QWidget()
        self.tabSettings.setObjectName("tabSettings")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.tabSettings)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.widget_3 = QtWidgets.QWidget(parent=self.tabSettings)
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_9 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_7.addWidget(self.label_9, 0, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem10, 0, 2, 1, 1)
        self.frame_6 = QtWidgets.QFrame(parent=self.widget_3)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_25 = QtWidgets.QGridLayout(self.frame_6)
        self.gridLayout_25.setObjectName("gridLayout_25")
        self.labelMegaLogin = QtWidgets.QLabel(parent=self.frame_6)
        self.labelMegaLogin.setMinimumSize(QtCore.QSize(350, 0))
        self.labelMegaLogin.setText("")
        self.labelMegaLogin.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.labelMegaLogin.setObjectName("labelMegaLogin")
        self.gridLayout_25.addWidget(self.labelMegaLogin, 0, 0, 1, 1)
        self.pushButtonMegaLogout = QtWidgets.QPushButton(parent=self.frame_6)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButtonMegaLogout.setFont(font)
        self.pushButtonMegaLogout.setStyleSheet("")
        self.pushButtonMegaLogout.setObjectName("pushButtonMegaLogout")
        self.gridLayout_25.addWidget(self.pushButtonMegaLogout, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.frame_6, 0, 3, 1, 4)
        self.pushButtonSyncToMega = QtWidgets.QPushButton(parent=self.widget_3)
        self.pushButtonSyncToMega.setObjectName("pushButtonSyncToMega")
        self.gridLayout_7.addWidget(self.pushButtonSyncToMega, 1, 0, 1, 1)
        self.toolButtonAuth = QtWidgets.QToolButton(parent=self.widget_3)
        self.toolButtonAuth.setObjectName("toolButtonAuth")
        self.gridLayout_7.addWidget(self.toolButtonAuth, 1, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(272, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem11, 1, 2, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_7.addItem(spacerItem12, 1, 3, 1, 1)
        self.checkBoxAutobackup = QtWidgets.QCheckBox(parent=self.widget_3)
        self.checkBoxAutobackup.setObjectName("checkBoxAutobackup")
        self.gridLayout_7.addWidget(self.checkBoxAutobackup, 1, 4, 1, 1)
        self.spinBoxBackupTime = QtWidgets.QSpinBox(parent=self.widget_3)
        self.spinBoxBackupTime.setMinimum(15)
        self.spinBoxBackupTime.setMaximum(720)
        self.spinBoxBackupTime.setSingleStep(30)
        self.spinBoxBackupTime.setProperty("value", 120)
        self.spinBoxBackupTime.setObjectName("spinBoxBackupTime")
        self.gridLayout_7.addWidget(self.spinBoxBackupTime, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_7.addWidget(self.label_11, 1, 6, 1, 1)
        self.gridLayout_19.addWidget(self.widget_3, 0, 0, 1, 2)
        self.line = QtWidgets.QFrame(parent=self.tabSettings)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_19.addWidget(self.line, 1, 0, 1, 2)
        self.widget_4 = QtWidgets.QWidget(parent=self.tabSettings)
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_10 = QtWidgets.QLabel(parent=self.widget_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_8.addWidget(self.label_10, 0, 0, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(318, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem13, 1, 0, 1, 1)
        self.pushButtonImportBase = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButtonImportBase.setObjectName("pushButtonImportBase")
        self.gridLayout_8.addWidget(self.pushButtonImportBase, 1, 1, 1, 1)
        self.pushButtonExportBase = QtWidgets.QPushButton(parent=self.widget_4)
        self.pushButtonExportBase.setObjectName("pushButtonExportBase")
        self.gridLayout_8.addWidget(self.pushButtonExportBase, 1, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(381, 25, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_8.addItem(spacerItem14, 0, 1, 1, 3)
        self.gridLayout_19.addWidget(self.widget_4, 2, 0, 1, 2)
        self.line_2 = QtWidgets.QFrame(parent=self.tabSettings)
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_19.addWidget(self.line_2, 3, 0, 1, 2)
        self.widget_5 = QtWidgets.QWidget(parent=self.tabSettings)
        self.widget_5.setObjectName("widget_5")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.widget_5)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_12 = QtWidgets.QLabel(parent=self.widget_5)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 0, 0, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(666, 17, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem15, 0, 1, 1, 3)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem16, 1, 0, 1, 2)
        self.widget_6 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBoxAutoprint = QtWidgets.QCheckBox(parent=self.widget_6)
        self.checkBoxAutoprint.setObjectName("checkBoxAutoprint")
        self.horizontalLayout.addWidget(self.checkBoxAutoprint)
        spacerItem17 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem17)
        self.label_13 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout.addWidget(self.label_13)
        self.spinBoxPrintCopyAmount = QtWidgets.QSpinBox(parent=self.widget_6)
        self.spinBoxPrintCopyAmount.setMaximum(5)
        self.spinBoxPrintCopyAmount.setProperty("value", 2)
        self.spinBoxPrintCopyAmount.setObjectName("spinBoxPrintCopyAmount")
        self.horizontalLayout.addWidget(self.spinBoxPrintCopyAmount)
        spacerItem18 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem18)
        self.label_14 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout.addWidget(self.label_14)
        self.spinBoxPauseBetweenCopies = QtWidgets.QSpinBox(parent=self.widget_6)
        self.spinBoxPauseBetweenCopies.setMaximum(30)
        self.spinBoxPauseBetweenCopies.setProperty("value", 5)
        self.spinBoxPauseBetweenCopies.setObjectName("spinBoxPauseBetweenCopies")
        self.horizontalLayout.addWidget(self.spinBoxPauseBetweenCopies)
        self.label_35 = QtWidgets.QLabel(parent=self.widget_6)
        self.label_35.setObjectName("label_35")
        self.horizontalLayout.addWidget(self.label_35)
        self.gridLayout_9.addWidget(self.widget_6, 1, 2, 1, 2)
        spacerItem19 = QtWidgets.QSpacerItem(459, 46, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_9.addItem(spacerItem19, 2, 0, 1, 3)
        self.label_15 = QtWidgets.QLabel(parent=self.widget_5)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.gridLayout_9.addWidget(self.label_15, 2, 3, 1, 1)
        self.widget_7 = QtWidgets.QWidget(parent=self.widget_5)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_7)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEditAdditional_info1 = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEditAdditional_info1.setObjectName("lineEditAdditional_info1")
        self.horizontalLayout_3.addWidget(self.lineEditAdditional_info1)
        self.lineEditAdditional_info2 = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEditAdditional_info2.setObjectName("lineEditAdditional_info2")
        self.horizontalLayout_3.addWidget(self.lineEditAdditional_info2)
        self.lineEditAdditional_info3 = QtWidgets.QLineEdit(parent=self.widget_7)
        self.lineEditAdditional_info3.setObjectName("lineEditAdditional_info3")
        self.horizontalLayout_3.addWidget(self.lineEditAdditional_info3)
        self.gridLayout_9.addWidget(self.widget_7, 3, 0, 1, 4)
        self.gridLayout_19.addWidget(self.widget_5, 4, 0, 1, 2)
        spacerItem20 = QtWidgets.QSpacerItem(600, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_19.addItem(spacerItem20, 6, 0, 1, 1)
        self.pushButtonSettingsSave = QtWidgets.QPushButton(parent=self.tabSettings)
        self.pushButtonSettingsSave.setMinimumSize(QtCore.QSize(120, 0))
        self.pushButtonSettingsSave.setObjectName("pushButtonSettingsSave")
        self.gridLayout_19.addWidget(self.pushButtonSettingsSave, 6, 1, 1, 1)
        self.widget_17 = QtWidgets.QWidget(parent=self.tabSettings)
        self.widget_17.setObjectName("widget_17")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.widget_17)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.comboBoxColorTheme = QtWidgets.QComboBox(parent=self.widget_17)
        self.comboBoxColorTheme.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxColorTheme.setLayoutDirection(QtCore.Qt.LayoutDirection.RightToLeft)
        self.comboBoxColorTheme.setObjectName("comboBoxColorTheme")
        self.gridLayout_10.addWidget(self.comboBoxColorTheme, 1, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(361, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem21, 1, 2, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(361, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem22, 0, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_10.addItem(spacerItem23, 1, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(parent=self.widget_17)
        self.label_30.setObjectName("label_30")
        self.gridLayout_10.addWidget(self.label_30, 0, 0, 1, 1)
        self.gridLayout_19.addWidget(self.widget_17, 5, 0, 1, 2)
        self.tab.addTab(self.tabSettings, "")
        self.tabRadio = QtWidgets.QWidget()
        self.tabRadio.setObjectName("tabRadio")
        self.gridLayout_24 = QtWidgets.QGridLayout(self.tabRadio)
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.frame_3 = QtWidgets.QFrame(parent=self.tabRadio)
        self.frame_3.setStyleSheet("QFrame {\n"
"    background: rgb(200, 200, 200);\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 1px solid rgb(100, 100, 100);\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: white;\n"
"    border-radius: 4px;\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: white;\n"
"    background-color: black\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_21 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_21.setObjectName("gridLayout_21")
        self.frame = QtWidgets.QFrame(parent=self.frame_3)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.label_16 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.gridLayout_11.addWidget(self.label_16, 0, 0, 1, 1)
        self.lineEditRadioName = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRadioName.setFont(font)
        self.lineEditRadioName.setStyleSheet("")
        self.lineEditRadioName.setObjectName("lineEditRadioName")
        self.gridLayout_11.addWidget(self.lineEditRadioName, 0, 1, 1, 1)
        spacerItem24 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_11.addItem(spacerItem24, 0, 2, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_11.addWidget(self.label_17, 1, 0, 1, 1)
        self.lineEditRadioUrl = QtWidgets.QLineEdit(parent=self.frame)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEditRadioUrl.setFont(font)
        self.lineEditRadioUrl.setObjectName("lineEditRadioUrl")
        self.gridLayout_11.addWidget(self.lineEditRadioUrl, 1, 1, 1, 2)
        self.gridLayout_21.addWidget(self.frame, 1, 0, 1, 2)
        spacerItem25 = QtWidgets.QSpacerItem(600, 31, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_21.addItem(spacerItem25, 2, 0, 1, 1)
        self.tableWidgetRadioStations = QtWidgets.QTableWidget(parent=self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidgetRadioStations.setFont(font)
        self.tableWidgetRadioStations.setStyleSheet("QHeaderView:section{\n"
"    border-radius: 4px;\n"
"}")
        self.tableWidgetRadioStations.setObjectName("tableWidgetRadioStations")
        self.tableWidgetRadioStations.setColumnCount(4)
        self.tableWidgetRadioStations.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(12)
        item.setFont(font)
        self.tableWidgetRadioStations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRadioStations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRadioStations.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetRadioStations.setHorizontalHeaderItem(3, item)
        self.tableWidgetRadioStations.verticalHeader().setVisible(False)
        self.gridLayout_21.addWidget(self.tableWidgetRadioStations, 0, 0, 1, 2)
        self.pushButtonRadioSave = QtWidgets.QPushButton(parent=self.frame_3)
        self.pushButtonRadioSave.setMinimumSize(QtCore.QSize(120, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonRadioSave.setFont(font)
        self.pushButtonRadioSave.setObjectName("pushButtonRadioSave")
        self.gridLayout_21.addWidget(self.pushButtonRadioSave, 2, 1, 1, 1)
        self.gridLayout_24.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(parent=self.tabRadio)
        self.frame_4.setStyleSheet("QFrame {\n"
"    background-color: rgba(250, 250, 250, 150);\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"    color: white;\n"
"    border-radius: 10px;\n"
"    background-color: rgba(55, 55, 55, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: white;\n"
"    background-color: black\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_23 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.frame_5 = QtWidgets.QFrame(parent=self.frame_4)
        self.frame_5.setStyleSheet("QFrame{\n"
"    background: rgb(220, 220, 220);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_22 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_22.setObjectName("gridLayout_22")
        self.pushButtonRadioPlay = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButtonRadioPlay.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonRadioPlay.setFont(font)
        self.pushButtonRadioPlay.setStyleSheet("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("play.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRadioPlay.setIcon(icon1)
        self.pushButtonRadioPlay.setObjectName("pushButtonRadioPlay")
        self.gridLayout_22.addWidget(self.pushButtonRadioPlay, 0, 0, 1, 1)
        spacerItem26 = QtWidgets.QSpacerItem(97, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_22.addItem(spacerItem26, 0, 4, 1, 1)
        self.label_34 = QtWidgets.QLabel(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet("")
        self.label_34.setObjectName("label_34")
        self.gridLayout_22.addWidget(self.label_34, 0, 5, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout_22.addItem(spacerItem27, 0, 2, 1, 1)
        self.pushButtonRadioStop = QtWidgets.QPushButton(parent=self.frame_5)
        self.pushButtonRadioStop.setMinimumSize(QtCore.QSize(70, 0))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButtonRadioStop.setFont(font)
        self.pushButtonRadioStop.setStyleSheet("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("stop.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pushButtonRadioStop.setIcon(icon2)
        self.pushButtonRadioStop.setObjectName("pushButtonRadioStop")
        self.gridLayout_22.addWidget(self.pushButtonRadioStop, 0, 1, 1, 1)
        self.checkBoxRadioAutoPlay = QtWidgets.QCheckBox(parent=self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBoxRadioAutoPlay.setFont(font)
        self.checkBoxRadioAutoPlay.setObjectName("checkBoxRadioAutoPlay")
        self.gridLayout_22.addWidget(self.checkBoxRadioAutoPlay, 0, 3, 1, 1)
        self.horizontalSliderRadioLoud = QtWidgets.QSlider(parent=self.frame_5)
        self.horizontalSliderRadioLoud.setMinimumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.horizontalSliderRadioLoud.setFont(font)
        self.horizontalSliderRadioLoud.setStyleSheet("QSlider {\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 0px;\n"
"    background: rgb(200, 200, 200);\n"
"    height: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::handle {\n"
"    background: rgb(55, 55, 55);\n"
"    height: 20px;\n"
"    width: 20px;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: rgb(100, 100, 100);\n"
"    border-top-left-radius: 10px;\n"
"    border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"")
        self.horizontalSliderRadioLoud.setProperty("value", 30)
        self.horizontalSliderRadioLoud.setSliderPosition(30)
        self.horizontalSliderRadioLoud.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSliderRadioLoud.setObjectName("horizontalSliderRadioLoud")
        self.gridLayout_22.addWidget(self.horizontalSliderRadioLoud, 0, 6, 1, 1)
        self.gridLayout_23.addWidget(self.frame_5, 5, 0, 1, 3)
        self.label_32 = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_32.sizePolicy().hasHeightForWidth())
        self.label_32.setSizePolicy(sizePolicy)
        self.label_32.setMaximumSize(QtCore.QSize(30, 30))
        self.label_32.setStyleSheet("background-color: rgba(255, 255, 255, 0)")
        self.label_32.setText("")
        self.label_32.setPixmap(QtGui.QPixmap("antenna.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setObjectName("label_32")
        self.gridLayout_23.addWidget(self.label_32, 1, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(parent=self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_33.sizePolicy().hasHeightForWidth())
        self.label_33.setSizePolicy(sizePolicy)
        self.label_33.setMaximumSize(QtCore.QSize(30, 30))
        self.label_33.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_33.setText("")
        self.label_33.setPixmap(QtGui.QPixmap("video.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setObjectName("label_33")
        self.gridLayout_23.addWidget(self.label_33, 3, 0, 1, 1)
        self.labelRadioCurrentSong = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRadioCurrentSong.setFont(font)
        self.labelRadioCurrentSong.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(25, 25, 25);;")
        self.labelRadioCurrentSong.setObjectName("labelRadioCurrentSong")
        self.gridLayout_23.addWidget(self.labelRadioCurrentSong, 3, 1, 1, 2)
        self.labelRadioStationIsPlaying = QtWidgets.QLabel(parent=self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelRadioStationIsPlaying.setFont(font)
        self.labelRadioStationIsPlaying.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(25, 25, 25);")
        self.labelRadioStationIsPlaying.setObjectName("labelRadioStationIsPlaying")
        self.gridLayout_23.addWidget(self.labelRadioStationIsPlaying, 1, 1, 1, 2)
        self.gridLayout_24.addWidget(self.frame_4, 2, 0, 1, 1)
        self.tab.addTab(self.tabRadio, "")
        self.gridLayout_3.addWidget(self.tab, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        create_all()
        self.logs_count = 0
        self.warranty_date = '1111-11-11 11:11:11'
        self.is_previous_orders = False
        self.client_table_filters = ''
        self.settings_dict = extract_settings()
        self.db_ready_to_sync = 0
        self.user_login_status = False
        self.print_list = []
        self.print_path = ''
        self.ready_to_print = 0
        self.ready_to_print_warranty = 0
        self.db_ready_to_upload = False
        self.warrany_print_list = []
        self.radio_current_song = ''
        self.sharing_dict = {}
        self.auth_has_been_changed = False

        self.tableWidgetClients.setColumnWidth(0, 10)
        self.tableWidgetClients.setColumnWidth(1, 110)
        self.tableWidgetClients.setColumnWidth(2, 140)
        self.tableWidgetClients.setColumnWidth(3, 210)
        self.tableWidgetClients.setColumnWidth(4, 120)
        self.tableWidgetClients.setColumnWidth(5, 200)

        self.tableWidgetRadioStations.setColumnWidth(0, 180)
        self.tableWidgetRadioStations.setColumnWidth(1, 510)
        self.tableWidgetRadioStations.setColumnWidth(2, 20)
        self.tableWidgetRadioStations.setColumnWidth(3, 0)

        self.lineEditSearch.textChanged.connect(self.change_search_filter)
        self.comboBoxGadgetType.activated.connect(self.change_search_filter)
        self.comboBoxIsFixed.activated.connect(self.change_search_filter)
        self.tableWidgetClients.cellClicked.connect(self.open_selected)


        self.lineEditCouponBreakFix.textChanged.connect(self.break_fix_input_prediction)
        self.lineEditCouponBreakFix.returnPressed.connect(self.break_fix_return_pressed)
        self.comboBoxCouponBreakFix.textActivated.connect(self.combobox_break_fix_choice)
        self.line_edit_break_fix_old_text = ''

        self.lineEditCreateTabPhoneNum.editingFinished.connect(self.find_previous_orders)
        self.lineEditCreateTabName.returnPressed.connect(self.name_2_return_pressed)

        self.lineEditCreateTabModel.textChanged.connect(self.model_2_input_prediction)
        self.lineEditCreateTabModel.returnPressed.connect(self.model_2_return_pressed)
        self.comboBoxCreateTabModel.textActivated.connect(self.combobox_model_2_choice)
        self.comboBoxCreateTabPackage.textActivated.connect(self.model_type_predict_filter)
        self.line_edit_model_2_old_text = ''

        self.lineEditCreateTabAdditionalPack.textChanged.connect(self.additional_package_input_prediction)
        self.lineEditCreateTabAdditionalPack.returnPressed.connect(self.additional_package_return_pressed)
        self.comboBoxCreateTabAdditionalPack.textActivated.connect(self.combobox_additional_package_choice)
        self.line_edit_additional_package_old_text = ''

        self.lineEditCreateTabBreakage.textChanged.connect(self.phone_breakage_2_input_prediction)
        self.lineEditCreateTabBreakage.returnPressed.connect(self.phone_breakage_2_return_pressed)
        self.comboBoxCreateTabBreakage.textActivated.connect(self.combobox_phone_breakage_2_choice)
        self.line_edit_phone_breakage_2_old_text = ''

        self.tableWidgetRadioStations.cellClicked.connect(self.click_to_play)

        self.pushButtonSyncToMega.clicked.connect(self.sync_with_cloud)
        self.pushButtonCreateTabPreviousOrders.clicked.connect(self.show_previous_orders)
        self.pushButtonCouponSave.clicked.connect(self.save_warranty_or_order_change)
        self.pushButtonCouponPrint.clicked.connect(self.print_warranty)
        self.pushButtonCreateTabSave.clicked.connect(self.new_order_check_all_fields)
        self.pushButtonCreateTabClear.clicked.connect(self.new_order_clean_all)
        self.pushButtonRadioSave.clicked.connect(self.save_new_station)
        self.pushButtonSettingsSave.clicked.connect(self.save_settings)
        self.pushButtonRadioPlay.clicked.connect(self.enable_radio)
        self.pushButtonRadioStop.clicked.connect(self.disable_radio)
        self.pushButtonMegaLogout.clicked.connect(self.mega_logout_confirm)
        self.pushButtonExportBase.clicked.connect(self.open_backup_file)
        self.pushButtonImportBase.clicked.connect(self.save_backup_file)

        self.toolButtonAuth.clicked.connect(lambda: self.open_mega_form())



        self.date_now = datetime.now()
        self.comboBoxCreateTabPackage.addItems(['Телефон', 'Планшет', 'Телевізор',
                                                   'Ноутбук', 'ПК', 'Монітор', 'інше'])
        self.comboBoxGadgetType.addItems(['Всі', 'Телефон', 'Планшет', 'Телевізор',
                                            'Ноутбук', 'ПК', 'Монітор', 'інше'])
        self.comboBoxIsFixed.addItems(['Всі', 'В процесі', 'Видано'])
        self.comboBoxSearchFilter.addItems(['Модель', 'ПІБ'])
        #self.tableWidgetClients.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.comboBoxCouponBreakFix.addItems(get_must_use('break_fix', 'WHERE is_fixed = 1'))
        self.comboBoxCreateTabModel.addItems(get_must_use('brand', ''))
        self.comboBoxCreateTabAdditionalPack.addItems(get_must_use('package', ''))
        self.comboBoxCreateTabBreakage.addItems(get_must_use('breakage', ''))
        self.settings_unpack()
        #self.hide_cloud_user()
        self.radio_thread = RadioAndAutoprintThread(mainwindow=self)
        self.radio_thread.start()
        self.model_2_input_prediction()
        self.add_to_log()

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TechnoLab "))
        self.labelLog.setText(_translate("MainWindow", "Log"))
        self.label_2.setText(_translate("MainWindow", "Статус"))
        self.label_31.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidgetClients.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidgetClients.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidgetClients.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidgetClients.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ПІБ"))
        item = self.tableWidgetClients.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.tableWidgetClients.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Поломка"))
        self.label.setText(_translate("MainWindow", "Пошук по"))
        self.tab.setTabText(self.tab.indexOf(self.tabClientTable), _translate("MainWindow", "Прийомка"))
        self.label_3.setText(_translate("MainWindow", "Тел.Клієнта"))
        self.label_4.setText(_translate("MainWindow", "ПІБ"))
        self.label_5.setText(_translate("MainWindow", "Комплектація"))
        self.label_6.setText(_translate("MainWindow", "Модель"))
        self.label_7.setText(_translate("MainWindow", "Додатково"))
        self.label_8.setText(_translate("MainWindow", "Поломка"))
        self.pushButtonCreateTabPreviousOrders.setText(_translate("MainWindow", "Минулі звернення"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Дата"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Модель"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Поломка"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Проведені роботи"))
        self.pushButtonCreateTabClear.setText(_translate("MainWindow", "Очистити"))
        self.pushButtonCreateTabSave.setText(_translate("MainWindow", "Зберегти"))
        self.tab.setTabText(self.tab.indexOf(self.tabCreate), _translate("MainWindow", "Створити "))
        self.label_18.setText(_translate("MainWindow", "Тел.Клієнта"))
        self.label_19.setText(_translate("MainWindow", "ПІБ"))
        self.label_20.setText(_translate("MainWindow", "Модель"))
        self.label_CouponDate.setText(_translate("MainWindow", "22 July 2024"))
        self.label_21.setText(_translate("MainWindow", "Комплектація"))
        self.label_23.setText(_translate("MainWindow", "Додатково"))
        self.label_22.setText(_translate("MainWindow", "Поломка"))
        self.label_24.setText(_translate("MainWindow", "Проведений ремонт"))
        self.label_25.setText(_translate("MainWindow", "Ціна"))
        self.label_27.setText(_translate("MainWindow", "грн."))
        self.label_26.setText(_translate("MainWindow", "Строк гарантії"))
        self.label_28.setText(_translate("MainWindow", "міс."))
        self.label_29.setText(_translate("MainWindow", "Оцінка клієнта"))
        self.radioButtonClientRateBlack.setText(_translate("MainWindow", "Чорний список"))
        self.radioButtonClientRateNorm.setText(_translate("MainWindow", "Норм"))
        self.radioButtonClientRatePerfect.setText(_translate("MainWindow", "Чудово"))
        self.pushButtonCouponSave.setText(_translate("MainWindow", "Зберегти"))
        self.pushButtonCouponPrint.setText(_translate("MainWindow", "Друк"))
        self.tab.setTabText(self.tab.indexOf(self.tabOutCheck), _translate("MainWindow", "Талон"))
        self.pushButtonSyncToMega.setText(_translate("MainWindow", "Синхронізувати"))
        self.checkBoxAutobackup.setText(_translate("MainWindow", "Автозбереження у хмару"))
        self.label_9.setText(_translate("MainWindow", "Mega"))
        self.pushButtonMegaLogout.setText(_translate("MainWindow", "Logout"))
        self.label_11.setText(_translate("MainWindow", "хв."))
        self.toolButtonAuth.setText(_translate("MainWindow", "..."))
        self.label_10.setText(_translate("MainWindow", "Локальний backup"))
        self.pushButtonExportBase.setText(_translate("MainWindow", "Завантажити файл бази"))
        self.pushButtonImportBase.setText(_translate("MainWindow", "Створити резервну копію"))
        self.label_12.setText(_translate("MainWindow", "Друк"))
        self.checkBoxAutoprint.setText(_translate("MainWindow", "Автодрук"))
        self.label_13.setText(_translate("MainWindow", "Кількість копій"))
        self.label_14.setText(_translate("MainWindow", "Пауза між копіями"))
        self.label_35.setText(_translate("MainWindow", "сек."))
        self.label_15.setText(_translate("MainWindow", "Додаткові відомості(компанія, контакти, загальна інформація)"))
        self.pushButtonSettingsSave.setText(_translate("MainWindow", "Зберегти"))
        self.label_30.setText(_translate("MainWindow", "Тема"))
        self.tab.setTabText(self.tab.indexOf(self.tabSettings), _translate("MainWindow", "Налаштування"))
        self.pushButtonRadioSave.setText(_translate("MainWindow", "Додати"))
        self.label_16.setText(_translate("MainWindow", "Назва"))
        self.label_17.setText(_translate("MainWindow", "URL"))
        item = self.tableWidgetRadioStations.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Станція"))
        item = self.tableWidgetRadioStations.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "URL"))
        self.checkBoxRadioAutoPlay.setText(_translate("MainWindow", "Автозапуск"))
        self.label_34.setText(_translate("MainWindow", "Гучність"))
        self.pushButtonRadioStop.setText(_translate("MainWindow", "Stop"))
        self.pushButtonRadioPlay.setText(_translate("MainWindow", "Play"))
        self.tab.setTabText(self.tab.indexOf(self.tabRadio), _translate("MainWindow", "Радіо"))

        self.paste_in_clients_table()
        self.tab.setTabVisible(2, False)
        self.comboBoxCreateTabAdditionalPack.setCurrentIndex(1)
        self.paste_in_radios_table()
        self.check_mega_login()
        if self.radio_is_playing:
            self.enable_radio()
        self.db_ready_to_sync = True

    def settings_unpack(self):
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

    def check_mega_login(self):
        if self.user_login_status:
            self.pushButtonMegaLogout.show()
            self.labelMegaLogin.setText(self.settings_dict['mega_user'])
        else:
            self.pushButtonMegaLogout.hide()
            self.labelMegaLogin.setText('')

    def mega_logout_confirm(self):
        self.open_confirm_form(f'Вийти з {self.settings_dict["mega_user"]}?', self.mega_logout)

    def mega_logout(self):
        self.settings_dict['mega_user'] = ''
        self.settings_dict['mega_pass'] = ''
        self.user_login_status = False
        self.check_mega_login()

    def open_mega_form(self):
        self.mega_window = QtWidgets.QDialog()
        self.ui = Ui_DialogMegaLogin()
        self.ui.setupUi(self.mega_window, self)
        self.mega_window.show()

    def open_backup_file(self):
        old_db_path = QtWidgets.QFileDialog.getOpenFileName(filter='*.sqlite3')[0]
        print(old_db_path)
        db_path = str(dir_path) + '/' + 'ling_lab.sqlite3'
        extract_from_backup(old_db_path, db_path)
        self.paste_in_clients_table()
        self.tab.setCurrentIndex(0)

    def save_backup_file(self):
        file_path = QtWidgets.QFileDialog.getSaveFileName(filter='*.sqlite3')[0]
        print(file_path)
        shutil.copy('./ling_lab.sqlite3', file_path)

    def hide_cloud_user(self):
        if self.checkBox_hide_pass.isChecked():
            self.label_8.hide()
            self.lineEdit_mega_user.hide()
            self.label_9.hide()
            self.lineEdit_mega_pass.hide()
        else:
            self.label_8.show()
            self.lineEdit_mega_user.show()
            self.label_9.show()
            self.lineEdit_mega_pass.show()

    def paste_in_clients_table(self):
        columns = 'in_date, brand, name, phone_number, breakage, id'
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
        self.paste_in_clients_table()

    def open_selected(self, row, col):
        self.selected_user_id = int(self.tableWidgetClients.item(row, 0).text())
        self.tab.setTabVisible(2, True)
        columns = 'device_type, package, break_fix, price, warranty, in_date'
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
        self.break_fix_input_prediction()
        self.tab.setCurrentIndex(2)

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
        self.lineEditCreateTabName.clear()
        self.lineEditCreateTabModel.clear()
        self.lineEditCreateTabAdditionalPack.clear()
        self.lineEditCreateTabBreakage.clear()
        self.is_previous_orders = False
        self.line_edit_model_2_old_text = ''
        self.line_edit_additional_package_old_text = ''
        self.line_edit_phone_breakage_2_old_text = ''
        self.model_2_input_prediction()
        self.additional_package_input_prediction()
        self.phone_breakage_2_input_prediction()

    def show_previous_orders(self):
        if self.is_previous_orders:
            self.comboBox.setCurrentText('ПІБ')
            self.lineEditSearch.setText(self.lineEditCreateTabName.text())
            self.change_search_filter()
            self.paste_in_clients_table()
            self.tabWidget.setCurrentIndex(0)

    def find_previous_orders(self):
        columns = 'in_date, brand, name, phone_number, breakage, id'
        phone_number = self.lineEditCreateTabPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        search_line = f'WHERE phone_number = "{phone_number}" '
        previous_orders = extract_clients_data(columns, search_line)
        if len(previous_orders) > 0:
            self.lineEditCreateTabName.setText(previous_orders[0][2].title())
            self.lineEditCreateTabModel.setFocus()
            self.is_previous_orders = True
        elif len(phone_number) == 10:
            self.lineEditCreateTabName.setFocus()
            self.is_previous_orders = False
        else:
            self.is_previous_orders = False

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
            self.add_to_log(f'Друк прийомка \n {self.lineEditCreateTabName.text()}')
        self.paste_in_clients_table()
        self.tab.setCurrentIndex(0)
        self.new_order_clean_all()

    def save_warranty_or_order_change(self):
        columns = ('phone_number, name, brand, device_type, package, '
                   'breakage, break_fix, price, out_date, is_fixed, warranty')
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
        order_string += f'"{str(self.spinBoxCouponWarranty.value())} міс." '
        save_warranty(columns, order_string, self.selected_user_id)
        self.tab.setTabVisible(2, False)
        self.add_to_log('Збережено ' + self.lineEditCouponName.text())
        self.paste_in_clients_table()
        self.tab.setCurrentIndex(0)

    def print_warranty(self):
        out_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        phone_number = self.lineEditCouponPhoneNum.text()
        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) > 10:
            phone_number = phone_number[-10:]
        if self.lineEditCouponBreakFix.text():
            self.warrany_print_list = [self.lineEditCouponModel.text(), self.lineEditCouponName.text().title(),
                                       phone_number, "", self.lineEditCouponBreakFix.text(),
                                       str(self.spinBoxCouponPrice.value()),
                                       f'{str(self.spinBoxCouponWarranty.value())} міс.']
            self.add_to_log(f'Друк гарантійний талон {self.warrany_print_list[1]}')
            self.print_path = paste_to_warranty(self.warrany_print_list)
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

    def break_fix_input_prediction(self):
        self.comboBoxCouponBreakFix.clear()
        if self.lineEditCouponBreakFix.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE break_fix LIKE "%{self.lineEditCouponBreakFix.text().lower()}%" '
        self.comboBoxCouponBreakFix.addItems(get_must_use(
            'break_fix', line_edit_text))

    def combobox_break_fix_choice(self):
        self.lineEditCouponBreakFix.setText(self.comboBoxCouponBreakFix.currentText())

    def break_fix_return_pressed(self):
        if self.line_edit_break_fix_old_text > self.lineEditCouponBreakFix.text() or\
                self.lineEditCouponBreakFix.text() == self.comboBoxCouponBreakFix.currentText():
            self.spinBox_price.setFocus()
        else:
            self.lineEditCouponBreakFix.setText(self.comboBoxCouponBreakFix.currentText())
        self.line_edit_break_fix_old_text = self.lineEditCouponBreakFix.text()

    def name_2_return_pressed(self):
        self.comboBoxCreateTabPackage.setFocus()

    def model_type_predict_filter(self):
        self.model_2_input_prediction()
        self.additional_package_input_prediction()
        self.phone_breakage_2_input_prediction()

    def model_2_input_prediction(self):
        self.comboBoxCreateTabModel.clear()
        if self.lineEditCreateTabModel.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE brand LIKE "%{self.lineEditCreateTabModel.text().lower()}%" '
        self.comboBoxCreateTabModel.addItems(get_must_use(
            'brand', line_edit_text))

    def combobox_model_2_choice(self):
        self.lineEditCreateTabModel.setText(self.comboBoxCreateTabModel.currentText())

    def model_2_return_pressed(self):
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
                self.lineEditCreateTabAdditionalPack.text() == self.comboBoxCreateTabAdditionalPack.currentText()or\
                self.comboBoxCreateTabAdditionalPack.currentText() == '':
            self.lineEditCreateTabBreakage.setFocus()
        else:
            self.lineEditCreateTabAdditionalPack.setText(self.comboBoxCreateTabAdditionalPack.currentText())
        self.line_edit_additional_package_old_text = self.lineEditCreateTabAdditionalPack.text()

    def phone_breakage_2_input_prediction(self):
        self.comboBoxCreateTabBreakage.clear()
        if self.lineEditCreateTabBreakage.text() == '':
            line_edit_text = f'WHERE device_type = "{self.comboBoxCreateTabPackage.currentText().lower()}"'
        else:
            line_edit_text = f'WHERE breakage LIKE "%{self.lineEditCreateTabBreakage.text().lower()}%" '
        self.comboBoxCreateTabBreakage.addItems(get_must_use(
            'breakage', line_edit_text))

    def combobox_phone_breakage_2_choice(self):
        self.lineEditCreateTabBreakage.setText(self.comboBoxCreateTabBreakage.currentText())

    def phone_breakage_2_return_pressed(self):
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
        self.db_ready_to_upload = True

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

    def save_new_station(self):
        name = self.lineEditRadioName.text()
        url = self.lineEditRadioUrl.text()
        if name != '' and url != '':
            save_new_station(name, url)
            self.paste_in_radios_table()

    def save_settings(self):
        # if self.lineEdit_mega_user.text() and self.lineEdit_mega_pass.text():
        #     self.settings_dict['mega_user'] = self.lineEdit_mega_user.text()
        #     self.settings_dict['mega_pass'] = self.lineEdit_mega_pass.text()

        self.settings_dict['auto_sync_time'] = str(self.spinBoxBackupTime.value())
        # self.settings_dict['mega_is_enabled'] = str(self.checkBox.isChecked())

        if self.checkBoxAutobackup.isChecked():
            self.settings_dict['auto_print'] = 'True'
        else:
            self.settings_dict['auto_print'] = ''
        self.settings_dict['copies'] = str(self.spinBoxPrintCopyAmount.value())
        self.settings_dict['pause_between_copies'] = str(self.spinBoxPauseBetweenCopies.value())
        # if self.lineEdit_mega_pass.text() == '' and self.lineEdit_mega_user.text() == '':
        #     self.settings_dict['hide_pass'] = ''
        # else:
        #     self.settings_dict['hide_pass'] = 'True'
        self.settings_dict['radio_current_name'] = self.radio_current_name

        self.settings_dict['radio_is_playing'] = str(int(self.checkBoxRadioAutoPlay.isChecked()))
        self.settings_dict['radio_volume_level'] = str(self.horizontalSliderRadioLoud.value())
        self.settings_dict['additional_print_line1'] = self.lineEditAdditional_info1.text()
        self.settings_dict['additional_print_line2'] = self.lineEditAdditional_info2.text()
        self.settings_dict['additional_print_line3'] = self.lineEditAdditional_info3.text()
        save_settings(self.settings_dict)

    def sync_with_cloud(self):
        if self.settings_dict['mega_user'] and self.settings_dict['mega_pass']:
            self.db_ready_to_sync = True
        else:
            self.open_mega_form()

    def add_to_log(self, item=False):  # функція запису у лог
        if item:
            self.current_log = str(item)
            self.labelLog.setText(str(datetime.now())[11: 19] + ' ' + self.current_log)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        ui.save_settings()


