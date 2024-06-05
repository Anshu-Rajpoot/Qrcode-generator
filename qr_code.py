# #Basic qr code to genereate output
# import qrcode as qr
# img=qr.make("https://www.youtube.com/")
# img.save("yt.png")

#Advanced 
import qrcode
from PIL import Image
qr=qrcode.QRCode(#version=1,
          error_correction=qrcode.constants.ERROR_CORRECT_H,
          box_size=12,border=5)
qr.add_data("https://www.youtube.com/")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="black")
img.save("ytlink.png")
