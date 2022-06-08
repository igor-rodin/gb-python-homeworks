# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее в алфавите.
# ROT13 является примером шифра Цезаря. Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
#  Если в строку включены числа или специальные символы, они должны быть возвращены как есть.
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.

def rot13(text: str, decode=False) -> str:
    text = text.upper()
    abc = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    dict = [""]*len(abc)
    shift = 13
    for i in range(len(abc)):
        dict[i] = abc[(i + shift) % len(abc)]
    encoded_text = [""]*len(text)
    for i in range(len(text)):
        if not text[i] in abc:
            encoded_text[i] = text[i]
        else:
            encoded_text[i] = abc[dict.index(
                text[i])] if decode else dict[abc.index(text[i])]

    return "".join(encoded_text)


text = "123курс__ант"
text_2 = "123НЦУФ__ГРХ"

encoded_text = rot13(text)
print(f"Закодированное сообщение: {encoded_text}")

decoded_text = rot13(encoded_text, decode=True)
print(f"Исходное сообщение: {decoded_text}")
