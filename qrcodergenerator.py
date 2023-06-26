import qrcode
import image 
qr = qrcode.QRCode(
 
    version = 15, #15means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10,
    border = 5
)

data = "https://www.youtube.com/"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("test.png")