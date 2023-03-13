print('This is Caesar cipher algorithm')


def valid_number():
    while True:
        inp = input()
        if inp.isdigit():
            if int(inp) > 26:
                print('This number is too big! Please try again')
            else:
                return int(inp)
        else:
            print('This is not a number! Please try again')


def english_cipher(text, shift):
    ciphered_text = ''
    for s in text:
        if s.isalpha():
            if s.islower() and ord(s) + shift > 122 or s.isupper() and ord(s) + shift > 90:
                ciphered_text += chr(ord(s) + shift - 26)
            else:
                ciphered_text += chr(ord(s) + shift)
        else:
            ciphered_text += s
    return ciphered_text


def english_decipher(text, shift):
    ciphered_text = ''
    for s in text:
        if s.isalpha():
            if s.islower() and ord(s) - shift < 97 or s.isupper() and ord(s) - shift < 65:
                ciphered_text += chr(ord(s) - shift + 26)
            else:
                ciphered_text += chr(ord(s) - shift)
        else:
            ciphered_text += s
    return ciphered_text


def russian_cipher(text, shift):
    ciphered_text = ''
    for s in text:
        if s.isalpha():
            if s.islower() and ord(s) + shift > 1103 or s.isupper() and ord(s) + shift > 1071:
                ciphered_text += chr(ord(s) + shift - 32)
            else:
                ciphered_text += chr(ord(s) + shift)
        else:
            ciphered_text += s
    return ciphered_text


def russian_decipher(text, shift):
    ciphered_text = ''
    for s in text:
        if s.isalpha():
            if s.islower() and ord(s) - shift < 1072 or s.isupper() and ord(s) - shift < 1040:
                ciphered_text += chr(ord(s) - shift + 32)
            else:
                ciphered_text += chr(ord(s) - shift)
        else:
            ciphered_text += s
    return ciphered_text


def choose_var():
    while True:
        answer = input()
        if answer == '1':
            return True
        elif answer == '2':
            return False
        else:
            print('We do not understand your answer. Please try again')


print("Please choose the language: press 1 for English and 2 for Russian")
language_choice = choose_var()
print("Please choose the shift direction: press 1 for ciphering (a + 3 = d), 2 for deciphering (d - 3 = a)")
direction_choice = choose_var()
print("Please enter the shift size")
user_shift = valid_number()
print("Please enter your text in one line")
initial_text = input()


if direction_choice and language_choice:
    print(english_cipher(initial_text, user_shift))
elif not direction_choice and language_choice:
    print(english_decipher(initial_text, user_shift))
elif direction_choice and not language_choice:
    print(russian_cipher(initial_text, user_shift))
elif not direction_choice and not language_choice:
    print(russian_decipher(initial_text, user_shift))
