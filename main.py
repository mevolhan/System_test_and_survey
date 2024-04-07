from flask import Flask, render_template, url_for
import os
from dotenv import load_dotenv

class MyDB():
    def __init__(self):
        self.host = os.getenv('host')
        self.port = os.getenv('port')
        self.user = os.getenv('user')
        self.password = os.getenv('password')
        self.dbname = os.getenv('dbname')

load_dotenv()
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-test')
def create_test():
    return render_template('create-test.html')

if __name__ == '__main__':
    app.run(debug=True)