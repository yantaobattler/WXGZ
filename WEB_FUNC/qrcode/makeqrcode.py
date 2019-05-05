import qrcode


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('http://39.107.236.31/WEB_FUNC/mandybirthday/2019/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('E:/123.png')