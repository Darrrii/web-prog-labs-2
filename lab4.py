from flask import Blueprint, render_template, request
lab4=Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')

@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    errors={}
    if request.method == 'GET':
        return render_template("login.html", errors=errors)

    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123' :
        return render_template('success.html', username = username)

    errors["cred"]= 'Неверные логин и/или пароль' 
    #username= request.args.get('username')
    print(f"pass = {password}")
    if username == '':
        errors['username']= 'Не введен логин'
    if password == '':
        errors['password']= 'Не введен пароль'
    return render_template('login.html', username=username, password=password, errors=errors)


@lab4.route('/lab4/success')
def order():
    return render_template('login.html')



@lab4.route('/lab4/xolod', methods = ['GET','POST'])
def xolodil():
    if request.method== 'GET':
        return render_template('xolod.html')

    temp = request.form.get('temp')
    error= ''

    if temp == '':
       error = 'Не задана температура'
    else:
        if temp:
            temp=int(temp)
            if (temp> -13) and 0>temp:
                if (temp> -13) and (-8>temp):
                    snow=''
                elif (temp>-9) and (-4>temp):
                    snow = 'snow'
                elif (temp>-5) and (0> temp):
                    snow= 'snow'
                return render_template('temper.html',temp=temp,snow=snow)
            
            if temp< -12:
                error='не удалось установить температуру — слишком низкое значение'
            if temp > -1:
                error='не удалось установить температуру — слишком высокое значение'
    return render_template('xolod.html', error=error, temp=temp)
            


@lab4.route('/lab4/zerno',methods = ['GET', 'POST'] )
def zerno():
    if request.method =='GET':
        return render_template('zerno.html')
    grain=request.form.get('grain')
    weight=request.form.get('weight')
    error=''

    if weight=='':
        error='Не ввели вес'
    else:
        weight=int(weight)

        if weight>50:
            sale=0.9
            message='Применена скидка за большой объем'
        else:
            sale=1
            message=''

    if grain =='ячмень':
        price= 12000*weight*sale
    elif grain=='овёс':
        price= 8500*weight*sale
    elif grain=='пшеница':
        price=8700*weight*sale
    else:
        price=14000*weight*sale
    if (weight>0) and (501>weight):
        return render_template('formazerna.html',grain=grain, weight=weight,
                                   price=price, message=message)
    if (weight<0) or weight==0:
        error = 'Неверное значение веса'
    elif weight> 500:
        error = 'Объем отстутствует в магазине'
    return render_template('zerno.html', grain=grain, weight=weight, error=error)


@lab4.route('/lab4/cookies', methods=['GET', 'POST'])
def cookies():
    if request.method=='GET':
        return render_template('cookies.html')
    
    color=request.form.get('color')
    background =request.form.get('background')
    text==request.form.get('text')

    if color == request.cookies.get('background'):
            return 'Цвет текста не должен совпадать с цветом фона'
    
    if not (5 <= int(text) <= 30):
            return 'Размер текста должен быть от 5px до 30px'
    headers= {
        'Set=Cookie': 'color='+color+'; path/',
        'Location': '/lab4/cookies'
    }
    return '', 303, headers