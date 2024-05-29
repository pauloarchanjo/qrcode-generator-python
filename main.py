import qrcode
from PIL import Image

class QRCodeGenerator:
    def __init__(self, version=15, box_size=10, border=5):
        self.qr = qrcode.QRCode(
            version=version,
            box_size=box_size,
            border=border
        )

    def generate_qr_code(self, data):
        self.qr.add_data(data)
        self.qr.make(fit=True)
        return self.qr.make_image(fill="black", back_color="white")

class QRCodeService:
    def __init__(self, generator: QRCodeGenerator):
        self.generator = generator

    def create_and_save_qr_code(self, data, file_path):
        img = self.generator.generate_qr_code(data)
        img.save(file_path)
        print(f"QR-Code saved in: {file_path}")

class UserInputHandler:
    def get_user_input(self, prompt):
        return input(prompt)

def main():
    print("QR-CODE GENERATOR")
    
    user_input_handler = UserInputHandler()
    link = user_input_handler.get_user_input("Enter the link you want to generate a QR-Code:")
    
    qr_generator = QRCodeGenerator()
    qr_service = QRCodeService(qr_generator)
    
    qr_service.create_and_save_qr_code(link, "QrCodeImage.png")

if __name__ == "__main__":
    main()
