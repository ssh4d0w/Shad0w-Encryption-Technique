import base64
import random

# Key
encryption_key = "secret_key"

def encrypt_text(text):
    encrypted_text = []
    character_count = len(text)
    
    for i in range(character_count):
        character = text[i]
        key_character = encryption_key[i % len(encryption_key)]
        encrypted_character = chr(ord(character) ^ ord(key_character))
        encrypted_text.append(encrypted_character)
    
    encrypted_text = "".join(encrypted_text).encode()
    encrypted_text = base64.b64encode(encrypted_text).decode()
    
    return encrypted_text

def decrypt_text(encrypted_text):
    encrypted_text = base64.b64decode(encrypted_text).decode()
    character_count = len(encrypted_text)
    
    text = []
    for i in range(character_count):
        character = encrypted_text[i]
        key_character = encryption_key[i % len(encryption_key)]
        original_character = chr(ord(character) ^ ord(key_character))
        text.append(original_character)
    
    return "".join(text)

while True:
    choice = input("1: Encrypt\n2: Decrypt\n3: Exit\nYour choice: ")
    
    if choice == '1':
        text = input("Enter the text you want to encrypt: ")
        encrypted_text = encrypt_text(text)
        print("Encrypted Text:", encrypted_text)
    elif choice == '2':
        encrypted_text = input("Enter the encrypted text you want to decrypt: ")
        text = decrypt_text(encrypted_text)
        print("Decrypted Text:", text)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
