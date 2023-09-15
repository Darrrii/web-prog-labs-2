from flask import Flask, redirect 
app= Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
def menu():
    return """
<!doctype html>
<html>
    <head>
        <title> Пушкарева Дарья, Андронова Софья лабораторная 1 </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторные работы, WEB-программирование, 2 часть
        </header>

        <h1> Список лабораторных </h1>
        <menu>
        <a href="lab1" target="_blank">Лабораторная работа 1</a>
        </menu>
        <footer>
            &copy; Пушкарева Дарья, Андронова Софья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

@app.route("/lab1")
def lab1():
    return """
    <!doctype html>
<html>
    <head>
        <title> Пушкарева Дарья, Андронова Софья лабораторная 1 </title>
    </head>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1> web-сервер на flask  </h1>
        <div>
        Flask — фреймворк для создания веб-приложений на языке
программирования Python, использующий набор инструментов
Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
называемых микрофреймворков — минималистичных каркасов
веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>
        <footer>
            &copy; Пушкарева Дарья, Андронова Софья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
""" 

    