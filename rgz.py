from flask import Blueprint, render_template, request,redirect 
import psycopg2

rgz=Blueprint('rgz', __name__)

def dbConnect():
    conn= psycopg2.connect(
        host="127.0.0.1",
        database="rgz",
        user="dasha_rgz",
        password="123")
    
    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@rgz.route("/rgz")
def main():
    conn=dbConnect()
    cur=conn.cursor()

    cur.execute("SELECT * FROM users;")

    result= cur.fetchall()

    print(result)

    dbClose(cur,conn)
    return "go to console"

@rgz.route("/rgz/register", methods=['GET', 'POST'])
def registerpage():
    errors=[]
    if request.method =="GET":
        return render_template("rgz_register.html", errors=errors)

    username= request.form.get("username")
    password= request.form.get("password")

    if username =='' or password =='':
        errors="Пожалуйста заполните все поля"
        return render_template("rgz_register.html", errors=errors)
    

    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с таким именем уже существует")

        dbClose(cur,conn)
        return render_template("rgz_register.html", errors=errors)
    
    cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/login")