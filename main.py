import pyqrcode
print()
print('Enter your text/link below')
print('___________________________')
print()
text = input()
print()
filename = input('Enter the filename: ')

qr = pyqrcode.create(text)
qr.png(f".//{filename}.png", scale=8)
