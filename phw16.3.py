text_input = input("Введите текст: ")
shift_input = int(input("Введите сдвиг: "))


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            durov = ord(char) + shift
            final_char = chr(durov)

    encrypted_text += final_char
    return (encrypted_text, shift)


print(caesar_cipher(text_input, shift_input))
