from flask import Flask
from flask import render_template, request
import hashlib
import base64

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
        text_list = list()
        """
        order of values:
        name
        age
        gender

        facebook
        instagram
        snapchat
        twitter

        about me
        """

        text_result = request.form

        for key, value in text_result.items():
            if(value is not ''):
                text_list.append(value)
            else:
                text_list.append('NA')
        #shorthand for text_list
        tl = text_list

        file_result = request.files
        file_result = base64.encodestring(file_result['image'].read()).decode('utf-8')

        return render_template('result.html', name = tl[0], age = tl[1], gender = tl[2], facebook = tl[3], instagram = tl[4], snapchat = tl[5], twitter = tl[6], about_me = tl[7], file_data = file_result)

    return app