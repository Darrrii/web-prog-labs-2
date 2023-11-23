from flask import Blueprint, render_template, request, redirect, session, Flaskgit, Flask
from Db import db
from Db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user


lab6=Blueprint("lab6", __name__)
app=Flask(__name__)

@lab6.route("/lab6/check")
def main():
    my_users=users.query.all()
    print(my_users)
    return "result in console!"

@lab6.route("/lab6/checkarticles")
def articl():
    my_articles=articles.query.all()
    print(my_articles)
    return "title-article_text"

@lab6.route("/lab6/register", methods=["GET", "POST"])
def register():
    errors=''
    if request.method =="GET":
        return render_template("register.html")

    username_form= request.form.get("username")
    password_form= request.form.get("password")


    isUserExists=users.query.filter_by(username= username_form).first()

    if isUserExists is not None:
        return render_template("register.html")

    if isUserExists=='':
        errors= 'Пожалуйста, заполните все поля'
        return render_template("register.html", errors=errors) 

    hashedPswd= generate_password_hash(password_form, method='pbkdf2')
    newUser=users(username=username_form, password=hashedPswd)

    db.session.add(newUser)
    db.session.commit()

    return redirect("/lab6/login")

@lab6.route("/lab6/login", methods=["GET", "POST"])
def login():
    errors=''
    if request.method =="GET":
        return render_template("5_login.html")

username_form= request.form.get("username")
password_form= request.form.get("password")

if username_form =='' or password_form == '':
    errors= 'Пожалуйста, заполните все поля'
    cur=conn.cursor()

cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

result= cur.fetchone()

if not result:
    errors='Неправильный логин или пароль'
    dbClose(cur, conn)
    return render_template('5_login.html', errors=errors)

userID,hashPassword= result

my_user= users.query.filter_by(username=username_form).first()

if my_user is not None:
    if check_password_hash(my_user.password, password_form):
        login_user(my_user, remember=False)
        return redirect("/lab6/articles")
return render_template("login.html")



