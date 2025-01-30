import qrcode
from PIL import Image

def create_pikachu_qr_code(filename="C:/Users/suraj/OneDrive/Desktop/PYTHON1/PYTHON-FULL/PYTHON PROJECT/PDF/OIP.jpeg"):
    """
    Generates a QR code with a Pikachu image overlaid.

    Args:
        filename: The filename to save the generated QR code image.
    """

    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Adjust version for desired size
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Adjust box size for image resolution
        border=4,
    )

    # Add data to the QR code
    qr.add_data("https://www.pokemon.com/us/pokemon/pikachu/")  # Link to Pikachu's page

    # Make the QR code
    qr.make(fit=True)

    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

    # Load the Pikachu image
    pikachu_img = Image.open(filename).convert("RGBA")  # Replace "pikachu.png" with the actual image path

    # Resize the Pikachu image to match the QR code size
    pikachu_img = pikachu_img.resize(qr_img.size, Image.LANCZOS)

    # Merge the QR code and Pikachu image
    combined_img = Image.alpha_composite(qr_img, pikachu_img)

    # Save the combined image
    combined_img.save("custom_qr_with_pikachu.png")
    combined_img.show()

if __name__ == "__main__":
    create_pikachu_qr_code()
