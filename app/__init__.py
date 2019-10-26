from flask import Flask
from flask import render_template, request

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return "nothing"

    @app.route('/form')
    def form():
        return render_template('getuserinput.html')

    @app.route('/result', methods = ['POST'])
    def result():
        result = request.form
        return render_template('result.html', result = result)

    return app