def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").upper()
    if choice not in ['E', 'D']:
        print("Invalid choice! Please enter E for encrypt or D for decrypt.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'E':
        result = encrypt(text, shift)
        print(f"Encrypted Text: {result}")
    elif choice == 'D':
        result = decrypt(text, shift)
        print(f"Decrypted Text: {result}")

if __name__ == "__main__":
    main()
