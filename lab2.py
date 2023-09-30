from flask import Blueprint, redirect, url_for, render_template
lab2=Blueprint('lab2', __name__)

@lab2.route('/lab2/example')
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
    
@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')
        
@lab2.route('/lab2/pictures')
def pictures():
        return render_template('pictures.html')