import pyrebase
from PrintLab.database import extract_clients_for_firebase


firebaseConfig = {'apiKey': "AIzaSyADCBApSnAZJcIY0EWBd2krywcIJsqEEoY",
  'authDomain': "technolab-67fa2.firebaseapp.com",
  'databaseURL': "https://technolab-67fa2-default-rtdb.europe-west1.firebasedatabase.app",
  'projectId': "technolab-67fa2",
  'storageBucket': "technolab-67fa2.firebasestorage.app",
  'messagingSenderId': "413803291031",
  'appId': "1:413803291031:web:6af9ba8ecf77ce997764d2"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


def signup(email, password):
    user = auth.create_user_with_email_and_password(email, password)

    # Вхід у систему
def login(email, password):
    user = auth.sign_in_with_email_and_password(email, password)
    # Отримання idToken для доступу до бази
    print(user)

    idToken = user['idToken']

    return idToken

    # Зберігання даних у Realtime Database
def save_to_firebase(idToken, data, table_name):
    db.child(table_name).set(data, idToken)


def update_firebase(idToken, data, table_name):
    db.update(data, idToken)
    

    # Отримання даних з Realtime Database
def get_from_firebase(idToken, table_name):
    data = db.child(table_name).get(idToken)
    data_list = []
    for line in data.each():
        data_list.append(list(line.val().values()))
    return data_list

def delete_from_firebase(idToken, table_name, id):
    db.child(table_name).child(id).remove(idToken)

def delete_table(idToken, table_name):
    db.child(table_name).remove(idToken)



if __name__ == "__main__":
    try:
        tok = login('ivan.lisovenko93@gmail.com', '93uranos')

        # get_from_firebase(tok, table_name)
        # data = extract_clients_for_firebase(table_name)
        # update_firebase(tok, data, table_name)
        delete_table(tok, 'clients')
        delete_table(tok, 'radios')
    except Exception as e:
        print(f"Error: {e}")



