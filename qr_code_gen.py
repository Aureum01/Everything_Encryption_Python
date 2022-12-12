# Import necessary libraries and modules
import tkinter as tk
from PIL import Image, ImageTk
import qrcode

# Create the main window for the application
window = tk.Tk()
window.title('QR Code Generator')

# Define a function for generating a QR code
def generate_qr_code():
    # Get the text to encode in the QR code from the input field
    text = text_input.get()

    # Generate the QR code using the qrcode library
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code and display it in the window
    img = qr.make_image()
    img = img.resize((250, 250), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    qr_label.config(image=img)
    qr_label.image = img

# Create a text input field for the user to enter the text to encode in the QR code
text_input = tk.Entry(window)
text_input.pack()

# Create a button for the user to click to generate the QR code
generate_button = tk.Button(window, text='Generate QR Code', command=generate_qr_code)
generate_button.pack()

# Create a label for displaying the generated QR code
qr_label = tk.Label(window)
qr_label.pack()

# Run the application
window.mainloop()
