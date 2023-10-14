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
    return render_template('login.html',errors=errors)



@lab4.route('/lab4/xolod', methods = ['GET','POST'])
def xolodil():
    errors={}
    temp = request.form.get('temp')
    if temp == '':
       errors['temp'] = 'Не задана температура'
    return render_template('xolod.html', errors=errors, temp=temp)


@lab4.route('/lab4/temperatura', methods = ['GET', 'POST'])
def temper():
    errors={}
    temp = request.form.get('temp')

    if temp is not None and int(temp) <= '-12' :
        errors['min']= 'Не удалось установить температуру — слишком низкое значение»'
    if temp is not None and int(temp) >= '-1':
        errors['max']= 'Не удалось установить температуру — слишком высокое значение'
    if temp is not None and int(temp)>= '-12' and temp<= '-9' :
        errors['sr']= f'Установлена температура {{int.(temp)}} ' 
    if temp is not None and int(temp)>= '-8' and temp<= '-5' :
        errors['men']= f'Установлена температура {{temp}}' 
    if temp is not None and int(temp) >= '-4' and temp<= '-1' :
        errors['bol']= f'Установлена температура {{temp}}'

    return render_template('temper.html',temp=temp, errors=errors)