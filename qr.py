# barcode_generator_Python
import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr=pyqrcode.create("Welcome To Python")
qr.png('mycode.png',scale=8)


d=decode(Image.open('mycode.png'))
print(d[0].data.decode('ascii'))
