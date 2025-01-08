import qrcode


data = "https://thewebsitecreator244.github.io/garfield-comic/index.html"
qr = qrcode.QRCode(version=5, box_size=15, border=10)
qr.add_data(data)
image = qr.make_image()
image.save("garfield.png")
