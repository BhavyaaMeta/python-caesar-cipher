# Caesar Cipher Tool

A menu-driven Caesar Cipher Tool built using Python. The application allows users to encrypt and decrypt messages using a custom shift value while preserving spaces, numbers, and special characters.

## Features

* Encrypt messages using Caesar Cipher
* Decrypt encrypted messages
* Custom shift value support
* Preserves spaces and special characters
* Handles both uppercase and lowercase letters
* Input validation using exception handling
* Menu-driven interface

## Technologies Used

* Python
* Functions
* Loops
* String Manipulation
* ASCII Operations (`ord()` and `chr()`)
* Exception Handling

## What I Learned

* Working with character encoding
* Using ASCII values for text processing
* Building encryption and decryption algorithms
* Creating reusable functions
* Handling user input safely
* Implementing menu-driven applications

## Project Structure

```text
python-caesar-cipher/
│
├── caesar_cipher.py
└── README.md
```

## How to Run

1. Make sure Python is installed on your system.
2. Download or clone the repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python caesar_cipher.py
```

## Sample Menu

```text
===== MENU =====
1. Encrypt Message
2. Decrypt Message
3. Exit
```

## Example

### Encryption

```text
Message: HELLO WORLD
Shift Value: 3
Encrypted Message: KHOOR ZRUOG
```

### Decryption

```text
Message: KHOOR ZRUOG
Shift Value: 3
Decrypted Message: HELLO WORLD
```

## How Caesar Cipher Works

The Caesar Cipher shifts each alphabet character by a fixed number of positions.

Example with shift value 3:

```text
A → D
B → E
C → F
...
X → A
Y → B
Z → C
```

## Future Improvements

* File encryption support
* Multiple encryption algorithms
* GUI using Tkinter
* Password-protected encryption
