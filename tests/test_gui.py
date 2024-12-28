import pytest
from PyQt6 import QtWidgets
from PrintLab.gui import Ui_MyWindow


class MainWindowGuiTest(QtWidgets.QMainWindow, Ui_MyWindow):
    """Клас для тестування, що поєднує QMainWindow та інтерфейс Ui_MainWindow."""
    def __init__(self):
        super().__init__()
        self.setupUi(self)  # Налаштовуємо інтерфейс


@pytest.fixture
def gui_window(qtbot):
    """Фікстура, що створює екземпляр MainWindowTest для тестування."""
    window = MainWindowGuiTest()
    qtbot.addWidget(window)
    window.show()  # Показуємо вікно під час тестування
    return window


def test_window_title(gui_window):
    """Тест перевіряє, чи правильно встановлюється заголовок вікна."""
    expected_title = "TechnoLab(v2.4)"
    assert gui_window.windowTitle() == expected_title


def test_table_clients_column_widths(gui_window):
    """Тест перевіряє, чи правильно встановлені ширини колонок у tableWidgetClients."""
    expected_widths = [55, 90, 140, 160, 105, 200]
    for col, expected_width in enumerate(expected_widths):
        assert gui_window.tableWidgetClients.columnWidth(col) == expected_width


def test_table_radio_column_widths(gui_window):
    """Тест перевіряє, чи правильно встановлені ширини колонок у tableWidgetRadioStations."""
    expected_widths = [180, 510, 50, 0]
    for col, expected_width in enumerate(expected_widths):
        assert gui_window.tableWidgetRadioStations.columnWidth(col) == expected_width


def test_table_previous_orders_column_widths(gui_window):
    """Тест перевіряє, чи правильно встановлені ширини колонок у tableWidget."""
    expected_widths = [85, 110, 270, 270]
    for col, expected_width in enumerate(expected_widths):
        assert gui_window.tableWidget.columnWidth(col) == expected_width

