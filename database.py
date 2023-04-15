import sqlite3


database_path = 'ling_lab.sqlite3'


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


def get_must_use(columns, filters=''):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    data = cursor.execute(f'SELECT {columns},  COUNT(*) as c '
                          f'FROM clients {filters} '
                          f'GROUP BY {columns} '
                          f'ORDER BY c DESC '
                          f'LIMIT 20')
    out_data = []
    for item in data:
        if item[0] != '':
            out_data.append(item[0])
    return out_data
    pass


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
    sql = f'INSERT INTO radios(name, url)' \
          f'VALUES ("{name}", "{url}") '
    cursor.execute(sql)
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


if __name__ == '__main__':
    extract_to_stat('WHERE in_date < "2023-04-28 21:50:16" AND in_date > "2022-03-24 09:15:37" ')
