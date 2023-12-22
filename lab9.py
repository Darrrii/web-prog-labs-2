from flask import Blueprint, render_template, request, abort, jsonify

lab9= Blueprint('lab9', __name__)

@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')

@lab9.app_errorhandler(404)
def not_found(e):
    return "нет такой страницы",404

@lab9.route('/lab9/404')
def error_404():
    return render_template('lab9/error404.html')

if __name__ == '__main__':
    lab9.run()

@lab9.route('/lab9/500')
def error_500():
    abort(500)

if __name__ == '__main__':
    lab9.run(debug=False)

@lab9.route('/lab9/gift', methods=['GET', 'POST'])
def gift():
    if request.method == 'POST':
        recipient_name = request.form.get('recipient_name')
        recipient_gender = request.form.get('recipient_gender')
        sender_name = request.form.get('sender_name')
        return render_template('lab9/card.html', recipient_name=recipient_name,
                                recipient_gender=recipient_gender,
                                  sender_name=sender_name)
    else:
        return render_template('lab9/form.html')

if __name__ == '__main__':
    lab9.run()