import sqlite3
import pytest
from PrintLab.models import create_clients, create_radios, create_settings, save_first_settings, create_all


# Фікстура для створення бази даних в пам'яті
@pytest.fixture
def setup_test_db():
    conn = sqlite3.connect(':memory:')  # Використовуємо базу даних в пам'яті
    yield conn  # Повертаємо з'єднання для тестів
    conn.close()  # Закриваємо з'єднання після тестів


# Мокаємо шлях до бази даних, щоб не використовувати справжню базу
@pytest.fixture(autouse=True)
def mock_database_path(monkeypatch, setup_test_db):
    def mock_connect(_):
        return setup_test_db

    monkeypatch.setattr(sqlite3, 'connect', mock_connect)


# Тест для функції create_clients
def test_create_clients(setup_test_db):
    create_clients()
    cursor = setup_test_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients';")
    table = cursor.fetchone()
    assert table is not None, "Таблиця clients не створена"


# Тест для функції create_radios
def test_create_radios(setup_test_db):
    create_radios()
    cursor = setup_test_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='radios';")
    table = cursor.fetchone()
    assert table is not None, "Таблиця radios не створена"


# Тест для функції create_settings
def test_create_settings(setup_test_db):
    create_settings()
    cursor = setup_test_db.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='settings';")
    table = cursor.fetchone()
    assert table is not None, "Таблиця settings не створена"


# Тест для функції save_first_settings
def test_save_first_settings(setup_test_db):
    create_settings()  # Спочатку створюємо таблицю settings
    setting_dict = {'radio_current_url': 'url', 'radio_current_name': 'Radio One',
                    'radio_is_playing': '1', 'radio_volume_level': '50'}

    save_first_settings(setting_dict)

    cursor = setup_test_db.cursor()
    cursor.execute("SELECT settings_dict FROM settings WHERE user='default';")
    saved_data = cursor.fetchone()

    assert saved_data is not None, "Налаштування не були збережені"
    assert str(setting_dict) in saved_data[0], "Збережені дані не відповідають очікуваним"


# Тест для функції create_all
def test_create_all(setup_test_db):
    create_all()

    cursor = setup_test_db.cursor()

    # Перевіряємо наявність таблиці clients
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients';")
    clients_table = cursor.fetchone()
    assert clients_table is not None, "Таблиця clients не створена"

    # Перевіряємо наявність таблиці radios
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='radios';")
    radios_table = cursor.fetchone()
    assert radios_table is not None, "Таблиця radios не створена"

    # Перевіряємо наявність таблиці settings
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='settings';")
    settings_table = cursor.fetchone()
    assert settings_table is not None, "Таблиця settings не створена"

    # Перевіряємо, чи збережені початкові налаштування
    cursor.execute("SELECT settings_dict FROM settings WHERE user='default';")
    saved_settings = cursor.fetchone()
    assert saved_settings is not None, "Початкові налаштування не були збережені"
    assert 'radio_current_url' in saved_settings[0], "Збережені налаштування некоректні"