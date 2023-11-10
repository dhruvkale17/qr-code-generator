# Importing library
import qrcode

def generate(url):
	# Data to encode

	# Creating an instance of QRCode class
	qr = qrcode.QRCode(version = 1,
					box_size = 10,
					border = 5)

	# Adding data to the instance 'qr'
	qr.add_data(url)

	qr.make(fit = True)
	img = qr.make_image(fill_color = 'red',
						back_color = 'white')

	img.save('MyQRC.png')
