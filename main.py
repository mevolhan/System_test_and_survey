from flask import Flask, render_template, url_for, request, redirect
import os
from dotenv import load_dotenv
import pymysql

class MyDB():
    def __init__(self, host='localhost', port=3036, user='user', password='mypassword', dbname='mydb'):
        self.host = host
        self.port = int(port)
        self.user = user
        self.password = password
        self.dbname = dbname
        self.connect_myBD()

    def connect_myBD(self):
        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.dbname,
                cursorclass=pymysql.cursors.DictCursor
                )
            print("Connection successful ...")
        except Exception as e:
            print("Connection error", e)

load_dotenv()
host_bd = os.getenv('host')
port_bd = os.getenv('port')
user_bd = os.getenv('user')
password_bd = os.getenv('password')
dbname_bd = os.getenv('dbname')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-test', methods=['POST', 'GET'])
def create_test():
    if request.method == "POST":
        title_test = request.form['input__title__create__test']
        description_test = request.form['input__description__create__test']
        print(title_test, description_test)
        return redirect('/create-test/questions')
    else:
        return render_template('create-test.html')

@app.route('/create-test/questions', methods=['POST', 'GET'])
def questions_test_create():
    return 'work'

if __name__ == '__main__':
    my_bd = MyDB(host=host_bd, port=port_bd, user=user_bd, password=password_bd, dbname=dbname_bd)
    app.run(debug=True)