from flask import Flask, redirect, url_for, render_template
app= Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route('/lab2/example')
def example():
    name, lab_num, group, course = 'Пушкарева Дарья', 2, 'ФБИ-12', 3
    fruits= [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321},
    ]
    books= [
        {'name': 'Шоколад', 'autor': 'Харрис Джоанн', 'janr': 'Роман', 'str':400},
        {'name': 'Изгои', 'autor': 'С.Э.Хинтон', 'janr': 'Роман', 'str':388},
        {'name': 'Звук и ярость', 'autor': 'У.Фолкнер', 'janr': 'Роман', 'str':416},
        {'name': 'Книжный вор', 'autor': 'З.Маркус', 'janr': 'Роман', 'str':608},
        {'name': 'Дом,в котором...', 'autor': 'М.Петросян', 'janr': 'Роман', 'str':960},
        {'name': 'о мышах и людях', 'autor': 'Д.Стейнбек', 'janr': 'Повесть' , 'str':256},
        {'name': 'С волками жить', 'autor': 'С.Райт', 'janr': 'Роман', 'str':519},
        {'name': 'Жизненный план', 'autor': 'Лори Н. Спилман', 'janr': 'Детективный роман', 'str':352},
        {'name': 'Великий Гетсби', 'autor': 'Ф.С.Фицджеральд', 'janr': 'Роман', 'str':224},
        {'name': 'Одинокая звезда', 'autor': 'Д.Чиаверини', 'janr': 'Роман', 'str':352}
    ]
    return render_template('example.html', 
                            name=name , lab_num=lab_num ,
                            group=group , course=course, fruits=fruits, books=books )
    
@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')
        
@app.route('/lab2/pictures')
def pictures():
        return render_template('pictures.html')

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
    <link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
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
          <a href="http://127.0.0.1:5000/menu" target="_blank">Меню</a>
            <h2>Реализованные роуты</h2>
            <li><a href="http://127.0.0.1:5000/lab1/oak" target="_blank">Дуб</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/student" target="_blank">Студент</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/python" target="_blank">Python</a></li>
            <li><a href="http://127.0.0.1:5000/lab1/cats" target="_blank">Котик</a></li>
        <footer>
            &copy; Пушкарева Дарья, Андронова Софья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
""" 
@app.route('/lab1/oak')
def oak():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <h1>Дуб</h1>
        <img src="''' +url_for('static', filename='oak.jpg') + '''">
    </body>
</html>
'''
@app.route('/lab1/student')
def student():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Андронова Софья Пушкарёва Дарья</h1>
        <img src="''' +  url_for('static', filename='logo_ngtu.png') + '''">
        <footer>
            &copy; Андронова Софья Пушкарёва Дарья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/python')
def python():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <main>
            <h1>Python</h1>
            <div>
            Python — это язык программирования, который широко 
            используется в интернет-приложениях, разработке программного 
            обеспечения, науке о данных и машинном обучении (ML). 
            Разработчики используют Python, потому что он эффективен, 
            прост в изучении и работает на разных платформах. Программы 
            на языке Python можно скачать бесплатно, они совместимы со 
            всеми типами систем и повышают скорость разработки.
            </div>
            <h2>Где применяется Python?</h2>
            
            <li>Веб-разработка на стороне сервера</li>
            <li>Автоматизация с помощью скриптов Python</li>
            <li>Разработка программного обеспечения</li>
            <li>Автоматизация тестирования программного обеспечения</li>
            
        </main>
        
        <img src="''' +  url_for('static', filename='python.png') + '''">
        <footer>
            &copy; Андронова Софья Пушкарёва Дарья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route('/lab1/cats')
def cats():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' +  url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <header>
            НГТУ, ФБ, Лабораторная работа 1
        </header>
        <h1>Кто такие кошки и что им нужно от людей?</h1>
        <div>
        Раскрыта главная тайна кошек! Уже очень давно многих заботливых 
        хозяев остро беспокоит один вопрос - почему кошки ни в какую не хотят 
        точить свои коготки на когтеточках и даже самые изощрённые подобные 
        приспособления так и остаются нетронутыми? И сколько ни спрашивали об 
        этом самих котов, никто из них так в этом и не признался.
        </div>
        <div>
        Но зоологи раскрыли эту тайну, и теперь умалчивать об этом больше 
        нет смысла. Сейчас вы узнаете важную новость. Оказывается, что 
        коты вовсе не точат ногти, как думали люди, а ставят метки на 
        выбранных предметах, тем самым обозначая зону своего влияния.
        </div>
        <img src="''' +  url_for('static', filename='cat.jpg') + '''">


        <footer>
            &copy; Андронова Софья Пушкарёва Дарья, ФБИ-12, 3 курс, 2023
        </footer>
    </body>
</html>
'''    