# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 18:59:15 2020

@author: prath
"""


import qrcode

input_URL = "https://www.linkedin.com/in/parth-panchal-7ab626172/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save("url_qrcode.png")

print(qr.data_list)