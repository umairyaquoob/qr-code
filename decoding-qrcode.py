# Decoding QR code in Python
from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('C:/Users/g_175/Documents/Umair Files/Test/myqrcode.png')

result = decode(img)

print(result)
