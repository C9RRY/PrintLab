import pytest
from PyQt6 import QtWidgets, QtCore
from PrintLab.gui import Ui_MyWindow
from PrintLab.ui_main_window import Ui_MainWindow


class MainWindowGuiTest(QtWidgets.QMainWindow, Ui_MainWindow):
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


def test_label_texts(gui_window):
    """Тест перевіряє, чи правильно встановлені тексти для міток."""
    assert gui_window.label.text() == "Пошук по"
    assert gui_window.label_2.text() == "Статус"
    assert gui_window.label_3.text() == "Тел.Клієнта"
    assert gui_window.label_4.text() == "ПІБ"
    assert gui_window.label_5.text() == "Комплектація"
    assert gui_window.label_6.text() == "Модель"
    assert gui_window.label_7.text() == "Додатково"
    assert gui_window.label_8.text() == "Поломка"
    assert gui_window.label_9.text() == "Користувач"
    assert gui_window.label_10.text() == "Локальний backup"
    assert gui_window.label_11.text() == "хв."
    assert gui_window.label_12.text() == "Друк"
    assert gui_window.label_13.text() == "Кількість копій"
    assert gui_window.label_14.text() == "Пауза між копіями"
    assert gui_window.label_15.text() == "Додаткові відомості(компанія, контакти, загальна інформація)"
    assert gui_window.label_16.text() == "Назва"
    assert gui_window.label_17.text() == "URL"
    assert gui_window.label_18.text() == "Тел.Клієнта"
    assert gui_window.label_19.text() == "ПІБ"
    assert gui_window.label_20.text() == "Модель"
    assert gui_window.label_21.text() == "Комплектація"
    assert gui_window.label_22.text() == "Поломка"
    assert gui_window.label_23.text() == "Додатково"
    assert gui_window.label_24.text() == "Проведений ремонт"
    assert gui_window.label_25.text() == "Ціна"
    assert gui_window.label_26.text() == "Строк гарантії"
    assert gui_window.label_27.text() == "грн."
    assert gui_window.label_28.text() == "міс."
    assert gui_window.label_29.text() == "Оцінка клієнта"
    assert gui_window.label_30.text() == "Тема"
    assert gui_window.label_31.text() == "Тип"
    assert gui_window.label_34.text() == "Гучність"
    assert gui_window.label_35.text() == "сек."
    assert gui_window.label_36.text() == "Минулі звернення"
    assert gui_window.label_CouponDate.text() == "22 July 2024"
    assert gui_window.labelRadioCurrentSong.text() == "Current Song"
    assert gui_window.labelRadioStationIsPlaying.text() == "Radiostation"


def test_table_widget_clients_headers(gui_window):
    headers = ["id", "Дата", "Модель", "ПІБ", "Номер", "Поломка"]
    for col, expected_text in enumerate(headers):
        item = gui_window.tableWidgetClients.horizontalHeaderItem(col)
        assert item.text() == expected_text


def test_table_widget_headers(gui_window):
    table_clients_headers = ["Дата", "Модель", "Поломка", "Проведені роботи", "Оцінка"]
    for col, expected_text in enumerate(table_clients_headers):
        item = gui_window.tableWidget.horizontalHeaderItem(col)
        assert item.text() == expected_text


def test_table_widget_radio_stations_headers(gui_window):
    assert gui_window.tableWidgetRadioStations.horizontalHeaderItem(0).text() == "Станція"
    assert gui_window.tableWidgetRadioStations.horizontalHeaderItem(3).text() == "ID"


def test_button_texts(gui_window):
    assert gui_window.pushButtonCreateTabClear.text() == "Очистити"
    assert gui_window.pushButtonCreateTabSave.text() == "Зберегти"
    assert gui_window.pushButtonCouponSave.text() == "Зберегти"
    assert gui_window.pushButtonCouponPrint.text() == "Друк"
    assert gui_window.pushButtonSettingsSave.text() == "Зберегти"
    assert gui_window.pushButtonImportBase.text() == "Завантажити файл бази"
    assert gui_window.pushButtonExportBase.text() == "Створити резервну копію"
    assert gui_window.pushButtonLogout.text() == "Logout"
    assert gui_window.pushButtonSyncToFirebase.text() == "Увійти"
    assert gui_window.pushButtonRadioSave.text() == "Додати"
    assert gui_window.pushButtonRadioPlay.text() == "Play"
    assert gui_window.pushButtonRadioStop.text() == "Stop"


def test_tool_button_texts(gui_window):
    assert gui_window.toolButtonAuth.text() == "..."


def test_tab_texts(gui_window):
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabClientTable)) == "Прийомка"
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabCreate)) == "Створити "
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabOutCheck)) == "Талон"
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabSettings)) == "Налаштування"
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabRadio)) == "Радіо"


def test_radiobuttons(gui_window):
    assert gui_window.radioButtonClientRateBlack.text() == "Чорний список"
    assert gui_window.radioButtonClientRateNorm.text() == "Норм"
    assert gui_window.radioButtonClientRatePerfect.text() == "Чудово"


def test_checkbox_text(gui_window):
    assert gui_window.checkBoxAutoprint.text() == "Автодрук"
    assert gui_window.checkBoxAutobackup.text() == "Автозбереження у хмару"
    assert gui_window.checkBoxRadioAutoPlay.text() == "Автозапуск"


def test_settings_tab_texts(gui_window):
    assert gui_window.pushButtonSettingsSave.text() == "Зберегти"
    assert gui_window.label_10.text() == "Локальний backup"
    assert gui_window.pushButtonImportBase.text() == "Завантажити файл бази"
    assert gui_window.pushButtonExportBase.text() == "Створити резервну копію"
    assert gui_window.label_9.text() == "Користувач"
    assert gui_window.pushButtonLogout.text() == "Logout"
    assert gui_window.pushButtonSyncToFirebase.text() == "Увійти"
    assert gui_window.toolButtonAuth.text() == "..."
    assert gui_window.checkBoxAutobackup.text() == "Автозбереження у хмару"
    assert gui_window.label_11.text() == "хв."
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabSettings)) == "Налаштування"


def test_radio_tab_texts(gui_window):
    assert gui_window.pushButtonRadioSave.text() == "Додати"
    assert gui_window.label_16.text() == "Назва"
    assert gui_window.label_17.text() == "URL"
    assert gui_window.tableWidgetRadioStations.horizontalHeaderItem(0).text() == "Станція"
    assert gui_window.tableWidgetRadioStations.horizontalHeaderItem(3).text() == "ID"
    assert gui_window.pushButtonRadioPlay.text() == "Play"
    assert gui_window.label_34.text() == "Гучність"
    assert gui_window.pushButtonRadioStop.text() == "Stop"
    assert gui_window.checkBoxRadioAutoPlay.text() == "Автозапуск"
    assert gui_window.labelRadioCurrentSong.text() == "Current Song"
    assert gui_window.labelRadioStationIsPlaying.text() == "Radiostation"
    assert gui_window.tab.tabText(gui_window.tab.indexOf(gui_window.tabRadio)) == "Радіо"



