import string

choose = str(input("Welcome, press 'n' to encrypt or 'd' to decrypt your message.\n"))

n = 1
d = 0

def caesar(text, password, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[password:] + alphabet[:password]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    print(final_shifted_alphabet)
    print('password to decrypt is %s' % (len(alphabets[0]) - password))
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

def uncaesar(text, key, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[key:] + alphabet[:key]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    print(final_shifted_alphabet)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

if choose == 'n':
    encrypt = input("Welcome, enter your message.\n")
    password = input("Enter your password to encrypt your message.\n")
    encrypted =(caesar(encrypt, int(password), [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
    print(encrypted)


elif choose == 'd':
    decrypt = input("Welcome, enter your encrypted message.\n")
    key = input("Enter your key to decrypt your message.\n")
    decrypted = (uncaesar(decrypt, int(key), [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))
    print(decrypted)

else:
    print("Incorrect input, try again later.")
