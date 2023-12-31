from werkzeug.security import check_password_hash, generate_password_hash
from flask import Blueprint, render_template, request, redirect, session, Flask
import psycopg2

app=Flask(__name__)
app.secret_key="123"

lab5=Blueprint('lab5', __name__)

def dbConnect():
    conn=psycopg2.connect( host="127.0.0.1",port="5433", database= "knowledge_base", user='daria_knowledge_base', password='Daria123')

    return conn

def dbClose(cursor, connection):
    cursor.close()
    connection.close()

@lab5.route("/lab5")
def main():
    conn= dbConnect()
    cur=conn.cursor()

    cur.execute("select * from users;")

    result= cur.fetchall()

    print(result)
    dbClose(cur,conn)
    return "go to console"

@lab5.route("/lab5/str")
def stran():
    username=session.get("username")
    if username =='':
        visibleUser= "anon"
    else:
        visibleUser=username

    return render_template('laba5.html', username=visibleUser)

@lab5.route("/lab5/register", methods=['GET', 'POST'])
def registerpage():
    errors=[]
    if request.method =="GET":
        return render_template("register.html", errors=errors)

    username= request.form.get("username")
    password= request.form.get("password")

    if username =='' or password =='':
        errors="Пожалуйста заполните все поля"
        return render_template("register.html", errors=errors)
    
    hashPassword= generate_password_hash(password)

    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

    if cur.fetchone() is not None:
        errors.append("Пользователь с таким именем уже существует")

        dbClose(cur,conn)
        return render_template("register.html", errors=errors)
    
    cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

    conn.commit()
    conn.close()
    cur.close()
    return redirect("/lab5/login")

@lab5.route('/lab5/login')
def login():
    errors=''
    if request.method =="GET":
        return render_template("login.html", errors=errors)

    username= request.form.get("username")
    password= request.form.get("password")

    if username =='' or password =='':
        errors="Пожалуйста заполните все поля"
        return render_template("register.html", errors=errors)
    
    conn=dbConnect()
    cur=conn.cursor()

    cur.execute(f"SELECT id, password FROM users WHERE username= '{username}';")

    result= cur.fetchall()

    if not result:
        errors="Неправильный логин или пароль"
        dbClose(cur,conn)
        return render_template("login.html", errors=errors)
    userID= result[0][0]
    hashPassword= result[0][1]

    if check_password_hash(hashPassword, password):
        session['id']=userID
        session['username']=username
        dbClose(cur,conn)
        return redirect(lab5/str)
    else:
        errors=''
        return render_template('login.html', errors=errors)
    
@lab5.route("/lab5/new_article", methods=['GET', 'POST'])
def createArticle():
    errors=[]
    userID= session.get("id")

    if userID is not None:
        if request.method=="GET":
            return render_template('new_article.html')
        if request.method=="POST":
            text_article= request.form.get("text_article")
            title= request.form.get("title_article")

            if len(text_article)==0:
                errors.append("Заполните поле")
                return render_template("new_article.html", errors=errors)
            conn=dbConnect()
            cur=conn.cursor()

            cur.execute(f"insert into articles(user_id, title, article_text) values ({userID}, '{title}','{text_article}') returning id")
            
            new_article_id= cur.fetchone()[0]
            conn.commit()

            dbClose(cur,conn)
            return render_template(f"/lab5/articles/{new_article_id}")
        return redirect("/lab5/login")
    
@lab5.route("/lab5.articles/<int:article_id>")
def getArticle(article_id):
    userID=session.get("id")

    if userID is not None:
        conn=dbConnect()
        cur=conn.cursor()

        cur.execute(f"select title, article_text from articles where  id= %s and user_id=%s", (article_id, userID))

        articleBody= cur.fetchone()
        dbClose(cur,conn)

        if articleBody is None:
            return "Not found"
        text= articleBody[1].splitlines()
        return render_template("article.html", article_text=text, article_title=articleBody[0], username=session.get("username"))





                                   