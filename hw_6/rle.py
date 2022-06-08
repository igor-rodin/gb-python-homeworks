# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги,
# а втором файлике — сжатая версия этого текста).

def read_data(file_name: str) -> str:
    with open(file_name, 'r') as fdata:
        text = fdata.read()
    return text


def write_data(file_name: str, data: str):
    with open(file_name, 'w') as fdata:
        fdata.write(data)


def rle_encode(data: str) -> str:
    encoded_text = []
    count_of_equal = 0
    prev_char = data[0]
    for char in data:
        if char == prev_char:
            count_of_equal += 1
        else:
            encoded_text.append(str(count_of_equal))
            encoded_text.append(prev_char)
            prev_char = char
            count_of_equal = 1
    encoded_text.append(str(count_of_equal))
    encoded_text.append(prev_char)
    return "".join(encoded_text)


def rle_decode(data: str) -> str:
    decoded_text = []

    idx = 0
    number_start = 0
    while idx < len(data):
        count = []
        if not data[idx].isdigit():
            count = data[number_start:idx]
            number_start = idx+1
            for _ in range(int(count)):
                decoded_text.append(data[idx])
        idx += 1

    return "".join(decoded_text)


data_file = 'data.txt'
encoded_data_file = 'encode_data.txt'

text = read_data(data_file)
encoded = rle_encode(text)
write_data(encoded_data_file, encoded)

encoded_text = read_data(encoded_data_file)
write_data(data_file, rle_decode(encoded))
