import psycopg2
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
connection = psycopg2.connect(database="logins_db",
                              user="postgres",
                              password="12345678",
                              host="localhost", port="5432")
cursor = connection.cursor()


@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template('login.html')

    login = request.form.get('login')
    password = request.form.get('password')
    cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(login), str(password)))
    records = list(cursor.fetchall())
    if records:
        return render_template("account.html", fullname=records[0][1], login=login, password=password)

    return render_template("error.html", login=login, password=password)


@app.route("/registration/", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    fullname = request.form.get('fullname')
    login = request.form.get('login')
    password = request.form.get('password')

#   Пустой ввод
    if not(fullname and login and password):
        return render_template("error.html", onReg=1)

    cursor.execute(f"SELECT * FROM service.users WHERE login='{str(login)}'")
    records = list(cursor.fetchall())

#   Такой пользователь уже есть
    if records:
        return render_template("error.html", onReg=1, login=login)

    cursor.execute("INSERT INTO service.users (full_name, login, password) VALUES (%s, %s, %s)",
                   (str(fullname), str(login), str(password)))
    connection.commit()
    return redirect("/")
