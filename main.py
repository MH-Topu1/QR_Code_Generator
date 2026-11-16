import qrcode
import os

# 1. Create output folder
output_folder = "generated_qr"
os.makedirs(output_folder, exist_ok=True)


# 2. Take user input
print("================================")
print("       QR CODE GENERATOR")
print("================================")

user_input = input("Enter text or URL: ").strip()

# Check empty input
if not user_input:
    print("Error: Input cannot be empty!")

else:

    # 3. Available colors
    valid_colors = [
        "red","blue","green","black","white","yellow","purple","orange"
    ]

    # 4. QR color validation
    qr_color = input("Enter QR color: ").strip().lower()

    while qr_color not in valid_colors:
        print("Invalid color! Try again.")
        qr_color = input("Enter QR color: ").strip().lower()


    # 5. Background color validation
    bg_color = input("Enter background color: ").strip().lower()

    while bg_color not in valid_colors:
        print("Invalid color! Try again.")
        bg_color = input("Enter background color: ").strip().lower()

    # 6. Generate QR Code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(user_input)
    qr.make(fit=True)

    img = qr.make_image(
        fill_color=qr_color,
        back_color=bg_color
    )

    # 7. File name
    filename = input("Enter file name: ").strip()

    if not filename:
        filename = "my_qr_code"

    if not filename.lower().endswith(".png"):
        filename += ".png"


    # 8. Save QR Code
    file_path = os.path.join(output_folder, filename)
    img.save(file_path)

    print("\nQR Code Generated Successfully!")
    print("Saved at:", file_path)