from app import app

@app.route('/')
@app.route('/home')
def home():
	return "this page will get user input"

