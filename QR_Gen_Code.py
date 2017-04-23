from qrcode import *
message = input ("Enter a message here: ")
qr = QRCode(version=1)
qr.add_data(message)
qr.make() # Generate the QRCode itself

# im contains a PIL.Image.Image object
im = qr.make_image()

# To save it
im.save("%s.png" % (message))
