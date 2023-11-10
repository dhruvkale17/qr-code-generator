import os
from flask import Flask, render_template, request
import validators
import qrcodegenerator
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route('/', methods=['POST'])
def generateQr():
	url = request.form.get('url')
	
	if validators.url(url):
		memory = BytesIO()
		img = qrcodegenerator.generate(url)
		print(url)
		img.save(memory)
		memory.seek(0)

		base64_img = "data:image/png;base64," + b64encode(memory.getvalue()).decode('ascii')
		return render_template('home.html', data = base64_img)
		
	return render_template('home.html')

# main driver function
if __name__ == '__main__':
    app.run(debug=True)
