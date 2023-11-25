import cv2
import os
import time

def create_mapping_dicts():
    d = {chr(i): i for i in range(255)}
    c = {i: chr(i) for i in range(255)}
    return d, c

def encrypt_image(img, message, mapping_dict):
    n, m, z = 0, 0, 0
    for char in message:
        img[n, m, z] = mapping_dict[char]
        n, m, z = n + 1, m + 1, (z + 1) % 3
    return img

def save_and_display_image(image, output_filename="Encryptedmsg.jpeg"):
    # Resize image for better display in IDLE
    resized_image = cv2.resize(image, (300, 300))
    cv2.imwrite(output_filename, resized_image)
    os.system(f"start {output_filename}")
    time.sleep(2)  # Add a delay for user readability

def decrypt_message(image, mapping_dict, message_length):
    n, m, z = 0, 0, 0
    decrypted_message = ""
    for _ in range(message_length):
        decrypted_message += mapping_dict[image[n, m, z]]
        n, m, z = n + 1, m + 1, (z + 1) % 3
    return decrypted_message

def main():
    img = cv2.imread("mypic.jpeg")

    msg = input("Enter secret message: ")
    password = input("Enter password: ")

    d, c = create_mapping_dicts()

    img = encrypt_image(img, msg, d)
    save_and_display_image(img)

    pas = input("Enter passcode for Decryption: ")

    if password == pas:
        decrypted_message = decrypt_message(img, c, len(msg))
        print("Decryption message:", decrypted_message)
    else:
        print("Not a valid key")

if _name_ == "_main_":
    main()
