from flask import Flask
from flask import render_template, request
import base64
from flask_sqlalchemy import SQLAlchemy
import qrcode
from io import BytesIO
from random import random
from sqlalchemy import Column, Integer, String 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///userinfo.db'
app.secret_key = 'thisisthesecretkey'

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "userinfo"

    id = db.Column(Integer, primary_key=True)
    hash_val = db.Column(Integer)
    name = db.Column(String)
    age = db.Column(String)
    gender = db.Column(String)
    para = db.Column(String)
    fb = db.Column(String)
    ig = db.Column(String)
    snap = db.Column(String)
    twitter = db.Column(String)
    image = db.Column(String)
    
    def __repr__(self):
        return "{}".format(self.name)

db.create_all()


@app.route('/')
def index():
    return render_template('userinput.html')

@app.route('/about')
def form():
    return "made by snacc overflow 2.0"

@app.route('/qr', methods = ['POST'])
def qr():
    counter = (int) (random() * 10000000)
    print(counter)
    #url = "http://hiwhatsyourna.me/page/{}".format(counter)
    url = "http://localhost:8080/page/{}".format(counter)
    qr_img = qrcode.make(url)

    text_result = request.form

    tl = list()
    """
    order of values:
    name
    age
    gender

    about me

    facebook
    instagram
    snapchat
    twitter
    """
    for key, value in text_result.items():
        if(value is not ''):
            tl.append(value)
        else:
            tl.append('NA')

    file_result = request.files
    file_result = base64.encodestring(file_result['image'].read()).decode('utf-8')

    usr = User(hash_val=counter, name=tl[0], age=tl[1], gender=tl[2], para=tl[3], fb=tl[4], ig=tl[5], snap=tl[6], twitter=tl[7], image=file_result)
    db.session.add(usr)
    db.session.commit()
    
    buffered = BytesIO()
    qr_img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    return render_template('qr.html', file_data=img_str)


@app.route('/page/<hashv>', methods = ['GET', 'POST'])
def result(hashv):
    usr = User.query.filter_by(hash_val = hashv).first()

    tl = list()
    tl.append(usr.name)
    tl.append(usr.age)
    tl.append(usr.gender)
    tl.append(usr.para)
    tl.append(usr.fb)
    tl.append(usr.ig)
    tl.append(usr.snap)
    tl.append(usr.twitter)

    file_result = usr.image

    return render_template('profile.html', name = tl[0], age = tl[1], gender = tl[2], about_me = tl[3], facebook = tl[4], instagram = tl[5], snapchat = tl[6], twitter = tl[7], file_data = file_result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)