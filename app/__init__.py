from flask import Flask
from flask import render_template, request

def create_app():
    app = Flask(__name__)

    #from app import routes
    @app.route('/', methods = ['GET', 'POST'])
    def index():
        return "nothing"

    @app.route('/home', methods = ['GET', 'POST'])
    def home():
	    return render_template('getuserinput.html')

    @app.route('/result', methods = ['GET', 'POST'])
    def result():
	    result = request.form
	    return render_template('result.html', result = result)

    return app