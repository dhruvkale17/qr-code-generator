import os
from flask import Flask, render_template, redirect, url_for, request, send_file
import validators
import qrcodegenerator

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

#Creart
@app.route('/createQR', methods=['GET', 'POST'])
def createQR():
	if request.method == 'POST':
		url = request.form['url']
		
		if validators.url(url):
			qrcodegenerator.generate(url)
			print(url)
			url = request.args.get('url')
			filename = "MyQRC.png"
			path = os.path.join(os.getcwd(), filename)
			return send_file(path, mimetype='image/png')
		return redirect(url_for('createQR'))
	return render_template('createQR.html')

		

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
