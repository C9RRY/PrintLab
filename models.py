import sqlite3


database_path = 'ling_lab.sqlite3'


def create_clients():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE clients( "
                   "id INTEGER PRIMARY KEY, "
                   "name VARCHAR(50), "
                   "in_date VARCHAR(30), "
                   "brand VARCHAR(30), "
                   "phone_number VARCHAR(30), "
                   "breakage VARCHAR(150), "
                   "device_type VARCHAR(50), "
                   "package VARCHAR(150), "
                   "out_date VARCHAR(40), "
                   "warranty VARCHAR(20) DEFAULT '3 міс.', "
                   "price VARCHAR(20) DEFAULT '0', "
                   "is_fixed BOOLEAN DEFAULT FALSE, "
                   "break_fix VARCHAR(100) DEFAULT '') ")

    conn.commit()


def create_radios():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE radios( "
                   "id INTEGER PRIMARY KEY , "
                   "name VARCHAR(250), "
                   "url VARCHAR(250), "
                   "is_play BOOLEAN )")
    conn.commit()


def create_settings():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE settings( "
                   "id INTEGER PRIMARY KEY , "
                   "user VARCHAR(50), "
                   "settings_dict VARCHAR(250)) ")
    conn.commit()


def save_first_settings(save_dict):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'INSERT INTO settings(user, settings_dict)' \
          f'VALUES ("default", "{save_dict}") '
    cursor.execute(sql)
    conn.commit()


def create_all():
    try:
        create_clients()
        create_radios()
        create_settings()
        setting_dict = {'radio_current_url': 'пусто)', 'radio_is_play': '',
                        'mega_user': '', 'mega_is_enabled': 'True',
                        'mega_pass': '', 'hide_pass': '',
                        'google_api': '', 'google_is_enabled': '', 'auto_sync_time': '30',
                        'auto_print': 'True', 'copies': '2', 'pause_between_copies': '5',
                        'additional_print_line1': '', 'additional_print_line2': '',
                        'additional_print_line3': ''}
        save_first_settings(setting_dict)
    except Exception as ex:
        return ex


if __name__ == "__main__":
    create_all()
