from flask import Flask, redirect, url_for, render_template
from lab1 import lab1
from lab2 import lab2
from lab3 import lab3
from lab4 import lab4

app= Flask(__name__)
app.register_blueprint(lab1)
app.register_blueprint(lab2)
app.register_blueprint(lab3)
app.register_blueprint(lab4)

@app.route('/lab2/zadanie')
def zadanie():
    A,B,C,N,K,G,H,summa = 1,2,3,10,6,2,3,0
    if A<B<C:
        A=A*2
        B=B*2
        C=C*2
        result= str(N)*K

        for i in range(1, H+1):
            summa += i**G
        slov= [{'A': A, 'B':B, 'C': C, 'summa': summa, 'result': result}]
        return render_template('zadanie.html',slov=slov)


