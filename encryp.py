from PIL import Image
import numpy as np
import os

def generate_key(shape):
    """Generate a random encryption key matching the image shape."""
    return np.random.randint(0, 256, size=shape, dtype=np.uint8)

def encrypt_image(image_path, key_path, output_path="encrypted_image.png"):
    try:
        img = Image.open(image_path)
        img_array = np.array(img)

        # Generate and save key if it doesn't exist
        if not os.path.exists(key_path):
            key = generate_key(img_array.shape)
            np.save(key_path, key)
        else:
            key = np.load(key_path)

        # Encrypt the image using XOR operation
        encrypted_array = np.bitwise_xor(img_array, key)
        encrypted_img = Image.fromarray(encrypted_array)
        encrypted_img.save(output_path)
        print("Image encrypted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(encrypted_image_path, key_path, output_path="decrypted_image.png"):
    try:
        encrypted_img = Image.open(encrypted_image_path)
        encrypted_array = np.array(encrypted_img)

        # Load the key
        if os.path.exists(key_path):
            key = np.load(key_path)
        else:
            print("Error: Encryption key not found!")
            return

        # Decrypt using XOR operation
        decrypted_array = np.bitwise_xor(encrypted_array, key)
        decrypted_img = Image.fromarray(decrypted_array)
        decrypted_img.save(output_path)
        print("Image decrypted successfully.")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Image Encryption and Decryption using Pixel Manipulation")
    image_path = input("Enter the path to the image file: ")
    key_path = "encryption_key.npy"  # Save key for reuse

    encrypt_image(image_path, key_path)
    decrypt_image("encrypted_image.png", key_path)

if __name__ == "__main__":
    main()
