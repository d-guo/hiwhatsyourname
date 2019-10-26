from flask import render_template, request

@app.route('/', methods = ['GET', 'POST'])
def index():
    return "nothing"

@app.route('/home', methods = ['GET', 'POST'])
def home():
	return render_template('getuserinput.html')

@app.route('/result', methods = ['GET', 'POST'])
def result():
	result = request.form
	for key, item in result:
		print(item)
	return render_template('result.html', result = result)