# Caesar Cipher Encryption-Decryption Tool

# Encrypt message using the given shift value
def encrypt(message, shift):
    encrypted_message = ""

    for char in message:

        if char.isupper():
            new = ord(char) + shift

            while new > ord('Z'):
                new -= 26

            encrypted_message += chr(new)

        elif char.islower():
            new = ord(char) + shift

            while new > ord('z'):
                new -= 26

            encrypted_message += chr(new)

        else:
            encrypted_message += char

    return encrypted_message


# Decrypt message using the given shift value
def decrypt(message, shift):
    decrypted_message = ""

    for char in message:

        if char.isupper():
            new = ord(char) - shift

            while new < ord('A'):
                new += 26

            decrypted_message += chr(new)

        elif char.islower():
            new = ord(char) - shift

            while new < ord('a'):
                new += 26

            decrypted_message += chr(new)

        else:
            decrypted_message += char

    return decrypted_message


def main():

    print("Welcome to Caesar Cipher Tool")

    while True:

        print("\n===== MENU =====")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:

            message = input("Enter message: ")

            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("Shift value must be a number.")
                continue

            encrypted = encrypt(message, shift)

            print("Encrypted Message:", encrypted)

        elif choice == 2:

            message = input("Enter message: ")

            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("Shift value must be a number.")
                continue

            decrypted = decrypt(message, shift)

            print("Decrypted Message:", decrypted)

        elif choice == 3:
            print("Thank you for using Caesar Cipher Tool.")
            break

        else:
            print("Invalid choice.")


# Run the application only when this file is executed directly
if __name__ == "__main__":
    main()