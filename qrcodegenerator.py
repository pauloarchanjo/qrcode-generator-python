import qrcode
import image
print("GERADOR DE QR-CODE")
a= input("Insira o link que deseja transformar em QR-Code:")

qr = qrcode.QRCode(
    version = 15,
    box_size = 10,
    border = 5
)
data = a

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black",back_color = "white")
img.save("QrCodeImage.png")