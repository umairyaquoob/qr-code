# Encoding QR code in Python
import qrcode

data = 'Don\'t forget to subscribe'

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_colour = 'red', back_colour = 'white')

img.save('C:/Users/g_175/Documents/Umair Files/Test/myqrcode.png')
