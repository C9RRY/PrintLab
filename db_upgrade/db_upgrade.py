import sqlite3
import pathlib

dir_path = pathlib.Path(__file__).parent.resolve()
old_db_name = 'old_ling_lab.sqlite3'
db_name = 'ling_lab.sqlite3'
database_path = './ling_lab.sqlite3'


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
                   "warranty VARCHAR(20) DEFAULT '0 міс.', "
                   "price VARCHAR(20) DEFAULT '0', "
                   "is_fixed VARCHAR(10) DEFAULT '0', "
                   "break_fix VARCHAR(100) DEFAULT '', "
                   "client_rate VARCHAR(10) DEFAULT 'normal' )")

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
        setting_dict = {'radio_current_url': '', 'radio_current_name': '',
                        'radio_is_playing': '0', 'radio_volume_level': '50',
                        'mega_user': '', 'mega_is_enabled': '1',
                        'mega_pass': '', 'hide_pass': '',
                        'google_api': '', 'google_is_enabled': '', 'auto_sync_time': '120',
                        'auto_print': '1', 'copies': '2', 'pause_between_copies': '5',
                        'additional_print_line1': '', 'additional_print_line2': '',
                        'additional_print_line3': ''}
        save_first_settings(setting_dict)
    except Exception as ex:
        return ex


def extract_from_backup(dir_path, old_db_name, db_name):
    conn = sqlite3.connect(str(dir_path) + '/' + old_db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT brand, package, breakage, name, phone_number, in_date, '
                   'break_fix, price, warranty, out_date, is_fixed, device_type '
                   'FROM clients ')
    data = cursor.fetchall()
    conn.commit()

    cursor.execute('SELECT id, name, url '
                   'FROM radios ')
    radios_data = cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()

    for client in data:
        conn = sqlite3.connect(str(dir_path) + '/' + db_name)
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO clients (brand, package, breakage, name, phone_number, in_date, '
                       f'break_fix, price, warranty, out_date, is_fixed, device_type) '
                       f'SELECT * FROM (SELECT "{client[0]}" AS brand, "{client[1]}" AS package, '
                       f'"{client[2]}" AS breakage, "{client[3]}" AS name, "{client[4]}" AS phone_number, '
                       f'"{client[5]}" AS in_date, "{client[6]}" AS break_fix, "{client[7]}" AS price, '
                       f'"{client[8]}" AS warranty, "{client[9]}" AS out_date, "{client[10]}" AS is_fixed, '
                       f'"{client[11]}" AS device_type'
                       f') AS temp '
                       f'WHERE NOT EXISTS ('
                       f'  SELECT in_date FROM clients WHERE in_date = "{client[5]}" '  
                       f') LIMIT 1')
        conn.commit()

    for radio in radios_data:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO radios (name, url)  '
                       f'SELECT * FROM (SELECT "{radio[1]}" AS name, "{radio[2]}" AS url'
                       f') AS temp '
                       f'WHERE NOT EXISTS ('
                       f'  SELECT name FROM clients WHERE name = "{radio[1]}" '  
                       f') LIMIT 1')
        conn.commit()
        cursor.close()
    try:
        cursor = conn.cursor()
        cursor.execute('UPDATE clients '
                       'SET is_fixed = "1" '
                       'WHERE is_fixed = "True" or is_fixed = "TRUE"')
        conn.commit()

        cursor = conn.cursor()
        cursor.execute('UPDATE clients '
                       'SET is_fixed = "0" '
                       'WHERE is_fixed = "False" or is_fixed = "FALSE"')
        conn.commit()
    except Exception as ex:
        print(ex)
    cursor.close()


if __name__ == '__main__':
    create_all()
    extract_from_backup(dir_path, old_db_name, db_name)
