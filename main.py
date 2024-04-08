from flask import Flask, render_template, url_for, request, redirect, session
from first_power import laad_dotenv_first_power, load_dotenv_SK
from control_BD import MyDB

app = Flask(__name__)
app.config['SECRET_KEY'] = load_dotenv_SK()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create-test', methods=['POST', 'GET'])
def create_test():
    if request.method == "POST":
        title_test = request.form['input__title__create__quiz']
        description_test = request.form['input__description__create__quiz']
        #session["curent_test"] = 1
        isTitleInBD = my_bd.save_title_quiz(title_test, description_test, 'test')
        #print(title_test, description_test)
        if isTitleInBD:
            return redirect('/create-quiz/questions')
        else:
            return render_template('create-quiz-error.html')

    else:
        return render_template('create-quiz.html', type='test')

@app.route('/create-test/questions', methods=['POST', 'GET'])
def questions_test_create():
    return 'work'

if __name__ == '__main__':
    host_bd, port_bd, user_bd, password_bd, dbname_bd = laad_dotenv_first_power()
    my_bd = MyDB(host=host_bd, port=port_bd, user=user_bd, password=password_bd, dbname=dbname_bd)
    app.run(debug=True)