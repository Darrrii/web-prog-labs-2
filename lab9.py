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
