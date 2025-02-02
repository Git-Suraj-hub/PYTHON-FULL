import qrcode
import PIL
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import SquareModuleDrawer, RoundedModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, CircleModuleDrawer, VerticalBarsDrawer
from qrcode.image.styles.colormasks import ImageColorMask
from PIL import Image, ImageDraw

if not hasattr(PIL.Image, 'Resampling'):
    PIL.Image.Resampling = PIL.Image


def corners(image_path, rad):
    im = Image.open(image_path).convert("RGBA")
    # im = Image.open(image_path)
    w, h = im.size
    circle = Image.new('L', (rad * 2 , rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2 , rad * 2), fill=255)
    
    alpha = Image.new('L', im.size, 255)
    box1 = (0, 0, rad, rad)
    box2 = (0, rad, rad, rad * 2)
    box3 = (rad, 0, rad * 2, rad)
    box4 = (rad, rad, rad * 2, rad * 2)
    alpha.paste(circle.crop(box1), (0, 0))
    alpha.paste(circle.crop(box2), (0, h - rad))
    alpha.paste(circle.crop(box3), (w - rad, 0))
    alpha.paste(circle.crop(box4), (w - rad, h - rad))
    im.putalpha(alpha)
    return im


qr = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H)
qr1 = qrcode.QRCode(version=2, error_correction=qrcode.constants.ERROR_CORRECT_H)


qr.add_data('MY LINKEDIN ACCOUNT : www.linkedin.com/in/suraj-singh-mehta')
qr1.add_data('To Learn More About Qr Code Visit : https://pypi.org/project/qrcode/')


im = corners('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Logo.png', 200)
im.save('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Logo_Corner.png')
im1 = corners('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Microsoft_Logo.png', 200)
im1.save('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Microsoft_Logo_Corner.png')



qr_img = qr.make_image(image_factory=StyledPilImage,
                       module_drawer=GappedSquareModuleDrawer(),
                       color_mask=ImageColorMask(color_mask_path='C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Bg.jpeg'),
                       embeded_image_path='C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Logo_Corner.png')


qr_img.save('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Qr-Code.png')


qr_img.show()



qr_img1 = qr1.make_image(image_factory=StyledPilImage,
                       module_drawer=RoundedModuleDrawer(),
                       color_mask=ImageColorMask(color_mask_path='C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Microsoft_Bg.jpeg'),
                       embeded_image_path='C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Microsoft_Logo_Corner.png')


qr_img1.save('C:\\Users\\suraj\\OneDrive\\Desktop\\PYTHON1\\PYTHON-FULL\\PYTHON PROJECT\\QR CODE\\Linkedin_Qr-Code.png')


qr_img1.show()




