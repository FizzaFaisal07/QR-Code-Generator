import qrcode

data=input("Enter the text or URL to generate the code:")

qr=qrcode.QRCode(
    version=1,   #controls size of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_L, #error correction
    box_size=10,  # size of each box in pixels
    border=4,  # thickness of border

)

qr.add_data(data)
qr.make(fit=True)

#img=qr.make_image(fill_color="black", back_color="white")
img = qr.make_image(fill_color="darkblue", back_color="lightyellow")
img.save("myqrcode.png")

print("QR Code generated and saved as myqrcode.png")