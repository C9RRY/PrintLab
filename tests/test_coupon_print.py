from PrintLab.coupon_print import paste_to_order, paste_to_warranty, static_path

from freezegun import freeze_time



# Простий тест для перевірки, чи повертається правильний шлях
@freeze_time("2024-01-01 12:00:00")
def test_paste_to_order_returns_correct_path():
    # Створюємо тестові дані
    data = [
        "TestModel", "TestPackage", "TestBreakage", "TestName",
        "1234567890", "AddInfo1", "AddInfo2", "AddInfo3"
    ]

    # Викликаємо функцію
    result = paste_to_order(data)

    # Очікуваний шлях до збереженого файлу
    expected_path = f"{static_path}/excel_files/saved_xlsx/TestName_2024-01-01_12.00.00.xlsx".replace(" ", "_")

    # Перевіряємо, чи повертається правильний шлях
    assert result == expected_path


@freeze_time("2024-01-01 12:00:00")
def test_paste_to_warranty_returns_correct_path():
    # Створюємо тестові дані
    data = [
        "TestModel", "TestName", "1234567890", "slug",
        "BreakFix", "100", "12 міс."
    ]

    # Викликаємо функцію
    result = paste_to_warranty(data)

    # Очікуваний шлях до збереженого файлу
    expected_path = f"{static_path}/excel_files/saved_xlsx/warr_TestName_2024-01-01_12.00.00.xlsx".replace(" ", "_")

    # Перевіряємо, чи повертається правильний шлях
    assert result == expected_path
