from flask import Blueprint, render_template, request, redirect
import psycopg2

lab5=Blueprint("lab5", __name__)

def dbConnent():
    conn= psycopg2.connect( host="127.0.0.1", database="knowledge_base", user="daria_knowledge_base", password="Daria123")

    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@lab5.route("/lab5")
def main():
    conn = dbConnent()
    cur=conn.cursor()

    cur.execute("select * from users;")

    result=cur.fetchall()

    print(result)
    dbClose(cur,conn)

    return "go to console"

@lab5.route("/lab5/users")
def use():

    conn= psycopg2.connect( host="127.0.0.1", database="knowledge_base", user="daria_knowledge_base", password="Daria123")

    cur=conn.cursor()

    cur.execute("select * from users;")

    result=cur.fetchall()

    cur.close()
    conn.close()
    print(result)

    return "go to console"



@lab5.route("/lab5/str")
def stran():
    visibleUser= "Anon"

    return render_template('laba5.html',username=visibleUser)

@lab5.route('/lab5/register', methods=['GET','POST'])
def registerPage():
    errors=[]

    if request.method== "GET":
        return render_template('register.html', errors=errors)

    username=request.form.get("username")
    password=request.form.get("password")

    if not (username or password):
        errors.append("Пожалуйста, заполните все поля")
        print(errors)
        return render_template("register.html", errors=errors)

    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"select username from users where username= '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с данным именем уже существует")
        
        dbClose(cur,conn)
        return render_template("register.html", errors=errors)

    cur.execute(f"insert into users (username,password) values ('{username}', '{password}')")

    dbClose(cur,conn)

    return redirect("/lab5/login")