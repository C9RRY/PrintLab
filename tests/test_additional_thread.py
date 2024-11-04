import pytest
from PyQt6 import QtCore, QtWidgets
from PrintLab.gui import Ui_MyWindow
from PrintLab.additional_thread import RadioAndAutoprintThread  # Замініть your_module на реальне ім'я модуля


class MainWindowGuiTest(QtWidgets.QMainWindow, Ui_MyWindow):
    """Клас для тестування, що поєднує QMainWindow та інтерфейс Ui_MainWindow."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Налаштовуємо інтерфейс


@pytest.fixture
def mainwindow(qtbot):
    """Фікстура, що створює екземпляр MainWindowTest для тестування."""
    window = MainWindowGuiTest()
    qtbot.addWidget(window)
    window.show()  # Показуємо вікно під час тестування
    return window


def test_radio_and_autoprint_thread_init(mainwindow):
    thread = RadioAndAutoprintThread(mainwindow)
    assert thread.isRunning() == False  # Потік ще не запущено


