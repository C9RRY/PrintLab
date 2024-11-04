import pytest
from PyQt6 import QtWidgets, QtCore
from PrintLab.ui_main_window import Ui_MainWindow
from PrintLab.gui import Ui_MyWindow


class MainWindowGuiTest(QtWidgets.QMainWindow, Ui_MyWindow):
    """Клас для тестування, що поєднує QMainWindow та інтерфейс Ui_MainWindow."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Налаштовуємо інтерфейс

# class MainWindowGuiTest(QtWidgets.QMainWindow):
#     """Клас для тестування, що поєднує QMainWindow та два інтерфейси."""
#     def __init__(self):
#         super().__init__()
#         self.ui_main = Ui_MainWindow()
#         self.ui_mywindow = Ui_MyWindow()
#
#         # Налаштовуємо обидва інтерфейси
#         self.ui_main.setupUi(self)
#         self.ui_mywindow.setupUi(self)


@pytest.fixture
def gui_window(qtbot):
    """Фікстура, що створює екземпляр MainWindowTest для тестування."""
    window = MainWindowGuiTest()
    qtbot.addWidget(window)
    window.show()  # Показуємо вікно під час тестування
    return window


def test_window_title(gui_window):
    """Тест перевіряє, чи правильно встановлюється заголовок вікна."""
    expected_title = "TechnoLab(v2.2)"
    assert gui_window.windowTitle() == expected_title


def test_tableWidgetClients_column_widths(gui_window, qtbot):
    """Тест перевіряє, чи правильно встановлені ширини колонок у tableWidgetClients."""
    expected_widths = [55, 90, 140, 160, 105, 200]
    for col, expected_width in enumerate(expected_widths):
        assert gui_window.tableWidgetClients.columnWidth(col) == expected_width

# def test_tableWidgetClients_column_widths(gui_window):
#     """Тест перевіряє, чи правильно встановлені ширини колонок у tableWidgetClients."""
#     # Перевіряємо, чи setupUi налаштував tableWidgetClients через екземпляр ui_main
#     gui_window.ui_mywindow.setupUi(gui_window)
#
#     # Тепер перевіряємо ширину колонок через self.ui_main
#     expected_widths = [12, 90, 140, 160, 105, 200]
#
#     for col, expected_width in enumerate(expected_widths):
#         assert gui_window.ui_mywindow.tableWidgetClients.columnWidth(col) == expected_width