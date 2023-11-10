import os
from flask import Flask, render_template, request
import validators
import qrcodegenerator

app = Flask(__name__)

#Creart
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'POST':
		url = request.form['url']
		
		if validators.url(url):
			qrcodegenerator.generate(url)
			print(url)
			#url = request.args.get('url')
			#filename = "MyQRC.png"
			#path = os.path.join(os.getcwd(), filename)
			#return send_file(path, mimetype='image/png')
		return render_template('home.html')
	return render_template('home.html')

		

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
