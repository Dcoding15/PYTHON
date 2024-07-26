import qrcode
from enum import Enum

class ColorPalette(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    MAGENTA = (255, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GRAY = (128, 128, 128)
    LIGHT_GRAY = (192, 192, 192)
    DARK_GRAY = (64, 64, 64)
    ORANGE = (255, 165, 0)
    PURPLE = (128, 0, 128)
    BROWN = (165, 42, 42)

# Function to generate and modify QR code colors
def generate_and_modify_qr(data, fg_color=ColorPalette.BLACK.value, bg_color=ColorPalette.WHITE.value):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    qr_pil = qr_img.convert('RGB')
    return qr_pil




URL = "https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl"

qr_pil = generate_and_modify_qr(URL, fg_color=ColorPalette.BLACK.value, bg_color=ColorPalette.GREEN.value)

qr_pil.save("QR IMAGE.png")