import sqlite3
import os


project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_path = project_dir + '\ling_lab.sqlite3'


def extract_clients_data(columns, filters):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute(f'SELECT {columns} '
                          f'FROM clients '
                          f'{filters} '
                          f'ORDER BY in_date DESC')
    data = [item for item in data]
    conn.commit()
    return data


def save_new_order(columns, order_string):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'INSERT INTO clients({columns})' \
          f'VALUES ({order_string}) '
    cursor.execute(sql)
    conn.commit()


def save_warranty(columns, order_string, client_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'UPDATE clients ' \
          f'SET ({columns}) = ({order_string}) ' \
          f'WHERE id = {client_id}' \

    cursor.execute(sql)
    conn.commit()


def get_must_use(column, filters=''):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute(f'SELECT {column},  COUNT(*) as c '
                          f'FROM clients {filters} '
                          f'GROUP BY {column} '
                          f'ORDER BY c DESC '
                          f'LIMIT 20')
    out_data = []
    for item in data:
        if item[0] != '':
            out_data.append(item[0])
    return out_data


def get_previous_price(filters=''):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute(f'SELECT price, in_date FROM clients  '
                          f' {filters} '
                          f'ORDER BY in_date DESC '
                          f'LIMIT 1')
    out_data = []
    for item in data:
        if item[0] != '':
            out_data.append(item[0])
    return out_data


def extract_radios_data(columns):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute(f'SELECT {columns} '
                          f'FROM radios '
                          f'ORDER BY id DESC')
    data = [item for item in data]
    conn.commit()
    return data


def save_radio_choice(columns, values, filters):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'UPDATE radios ' \
          f'SET ({columns}) = ({values}) {filters}'

    cursor.execute(sql)
    conn.commit()


def save_new_station(name, url):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'INSERT INTO radios(name, url) ' \
          f'VALUES ("{name}", "{url}") '
    cursor.execute(sql)
    conn.commit()


def del_station(station_id):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'DELETE FROM radios '
                   f'WHERE id = {int(station_id)} ')
    conn.commit()


def extract_settings():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'SELECT settings_dict ' \
          f'FROM settings'
    cursor.execute(sql)
    data = cursor.fetchall()
    data_list = data[0][0][1: -1].split(', ')
    data_list = [items.replace("'", '').split(': ') for items in data_list]
    data_dict = {key: value for key, value in data_list}
    return data_dict


def save_settings(save_dict):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    sql = f'UPDATE settings ' \
          f'SET settings_dict = "{save_dict}"'
    cursor.execute(sql)
    conn.commit()


def custom_sql(query):
    try:
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        result = cursor.fetchall()
        return repr(result)
    except Exception as ex:
        return ex


def extract_to_stat(filters):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute(f'SELECT date(in_date), COUNT(*) as c '
                   f'FROM clients '
                   f'{filters} '
                   f'GROUP BY date(in_date) ')
    data = cursor.fetchall()
    data0 = [item[0] for item in data]
    data1 = []
    for item in range(len(data * 100)):
        data1.append(item)
    data2 = []
    for item in data:
        for _ in range(90):
            data2.append(item[1])
        for _ in range(10):
            data2.append(0)
    return data0, data1, data2


def extract_from_backup(old_db_path, db_path):
    conn = sqlite3.connect(old_db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT brand, package, breakage, name, phone_number, in_date, '
                   'break_fix, price, warranty, out_date, is_fixed, device_type, client_rate '
                   'FROM clients ')
    data = cursor.fetchall()
    conn.commit()

    cursor.execute('SELECT id, name, url '
                   'FROM radios ')
    radios_data = cursor.fetchall()
    conn.commit()

    cursor.close()
    conn.close()
    conn = sqlite3.connect(db_path)
    for client in data:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO clients (brand, package, breakage, name, phone_number, in_date, '
                       f'break_fix, price, warranty, out_date, is_fixed, device_type, client_rate) '
                       f'SELECT * FROM (SELECT "{client[0]}" AS brand, "{client[1]}" AS package, '
                       f'"{client[2]}" AS breakage, "{client[3]}" AS name, "{client[4]}" AS phone_number, '
                       f'"{client[5]}" AS in_date, "{client[6]}" AS break_fix, "{client[7]}" AS price, '
                       f'"{client[8]}" AS warranty, "{client[9]}" AS out_date, "{client[10]}" AS is_fixed, '
                       f'"{client[11]}" AS device_type, "{client[12]}" AS client_rate'
                       f') AS temp '
                       f'WHERE NOT EXISTS ('
                       f'  SELECT in_date FROM clients WHERE in_date = "{client[5]}" '  # need to add AND name =
                       f') LIMIT 1')
    conn.commit()
    for client in data:
        if client[10] == '1':
            cursor = conn.cursor()
            cursor.execute(f'UPDATE clients '
                           f'SET break_fix = "{client[6]}", price = "{client[7]}", warranty = "{client[8]}", '
                           f'out_date = "{client[9]}" , is_fixed = "{client[10]}", client_rate = "{client[12]}"'
                           f'WHERE in_date = "{client[5]}" AND is_fixed = "0" ')
    conn.commit()
    cursor.close()
    for radio in radios_data:
        cursor = conn.cursor()
        cursor.execute(f'INSERT INTO radios (name, url)  '
                       f'SELECT * FROM (SELECT "{radio[1]}" AS name, "{radio[2]}" AS url'
                       f') AS temp '
                       f'WHERE NOT EXISTS ('
                       f'  SELECT name FROM radios WHERE name = "{radio[1]}" '  
                       f') LIMIT 1')
    conn.commit()


if __name__ == '__main__':
    extract_to_stat('WHERE in_date < "2023-04-28 21:50:16" AND in_date > "2022-03-24 09:15:37" ')
