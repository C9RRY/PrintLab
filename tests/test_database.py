import sqlite3
import pytest
from PrintLab.database import extract_clients_data


# Тестова база даних у пам'яті
@pytest.fixture
def setup_test_db():
    conn = sqlite3.connect(':memory:')  # Створюємо базу даних в пам'яті
    cursor = conn.cursor()

    # Створюємо таблицю clients
    cursor.execute('''
        CREATE TABLE clients (
            id INTEGER PRIMARY KEY,
            name TEXT,
            in_date TEXT
        )''')

    # Вставляємо тестові дані
    cursor.executemany('''
        INSERT INTO clients (name, in_date) VALUES (?, ?)
    ''', [
        ('Client A', '2024-11-01'),
        ('Client B', '2024-11-03'),
        ('Client C', '2024-11-02'),
    ])

    conn.commit()

    yield conn  # Повертаємо підключення до тестової бази для тестів

    # Закриваємо з'єднання після завершення тестів
    conn.close()


# Функція для тестування, яка використовує тестову базу
def test_extract_clients_data(setup_test_db, monkeypatch):
    # Підміняємо шлях до бази на in-memory базу
    def mock_connect(_):
        return setup_test_db

    monkeypatch.setattr(sqlite3, 'connect', mock_connect)  # Мокаємо підключення до бази

    # Викликаємо функцію з тестовими параметрами
    columns = 'name, in_date'
    filters = ''
    result = extract_clients_data(columns, filters)

    # Перевіряємо, чи результат коректний
    assert len(result) == 3  # Ми очікуємо три записи
    assert result[0][0] == 'Client B'  # Перевіряємо, чи правильний клієнт на першому місці
    assert result[1][0] == 'Client C'
    assert result[2][0] == 'Client A'