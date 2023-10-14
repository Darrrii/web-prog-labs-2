from flask import Blueprint, redirect, url_for, render_template, request
lab3=Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors={}
    user= request.args.get('user')
    if user == '':
        errors['user']= 'Заполните поле!'

    age= request.args.get('age')
    if age == '':
        errors['age']= 'Заполните поле!'
    sex= request.args.get('sex')
    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors)

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price=0
    drink= request.args.get('drink')
    if drink =='coffee':
        price= 120
    elif drink=='black-tea':
        price= 80
    else:
        price=70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':   
        price += 10 

    return render_template('pay.html', price=price)

@lab3.route('/lab3/success')
def success():
        return render_template('Spasibo.html')

@lab3.route('/lab3/ticket')
def ticket():
    errors={}
    FIO= request.args.get('FIO')
    if FIO == '':
        errors['FIO']= 'Заполните поле!'
    
    data= request.args.get('data')
    if data == '':
        errors['data']= 'Заполните поле!'

    age= request.args.get('age')
    if age == '':
        errors['age']= 'Заполните поле!'

    arr= request.args.get('arr')
    if arr == '':
        errors['arr']= 'Заполните поле!'

    naznach= request.args.get('naznach')
    if arr == '':
        errors['naznach']= 'Заполните поле!'

    FIO=request.args.get('FIO')
    ticket=request.args.get('ticket')
    polka=request.args.get('polka')
    bagg=request.args.get('bagg')
    return render_template('ticket.html',FIO=FIO, data=data, age=age, arr=arr,naznach=naznach,ticket=ticket,
                           polka=polka,bagg=bagg, errors=errors)

@lab3.route('/lab3/forma')
def forma():
            pay= 0
            ticket = request.args.get('ticket')
            if ticket == 'children':
                 pay= 'Детский билет'
            else :
                 pay='Взрослый билет'

            pol=0
            polka= request.args.get('polka')
            if polka== 'up':
                 pol= 'Верхняя полка'
            elif polka== 'down':
                 pol='Нижняя полка'
            elif polka=='side-up':
                 pol='Верхняя полка'
            else :
                 pol='Нижняя полка'

            bag=0
            bagg= request.args.get('bagg')
            if bagg=='yes':
                 bag='Багаж включен'
            else:
                 bag='Без багажа'
            FIO= request.args.get('FIO')
            age= request.args.get('age')
            arr= request.args.get('arr')
            naznach= request.args.get('naznach')
            data1=request.args.get('data1')
            return render_template('forma.html',FIO=FIO, pay=pay, pol=pol, bag=bag,age=age, arr=arr, naznach=naznach, data1=data1 )






