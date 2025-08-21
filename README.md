# Image-Encryption
PRODIGY_CS_02

This Python script provides a basic image encryption and decryption tool using simple pixel manipulation techniques. It utilizes the Pillow library to open and manipulate images and NumPy for numerical operations and key generation.

The script includes two main functions:

>encrypt_image(image_path, key_path, output_path): Takes an image file path, a path to store or load the encryption key, and an optional output path for the encrypted image. It generates a random key (if one doesn't exist) based on the image's shape, applies a pixel-wise XOR operation with the key to encrypt the image, and saves the encrypted image.

>decrypt_image(encrypted_image_path, key_path, output_path): Takes the path of an encrypted image, the path to the encryption key, and an optional output path for the decrypted image. It loads the key and applies the same pixel-wise XOR operation to the encrypted image to restore the original image, saving the result.


A main() function guides the user to input the image path and then performs both encryption and decryption using a saved key file (encryption_key.npy).

Important Note: This encryption method is very basic and not secure for protecting sensitive information. It is intended solely for educational purposes to demonstrate fundamental concepts of image manipulation and basic cryptographic operations.
