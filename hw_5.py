
import enum
from functools import reduce
import math
from random import randint

# Задача 1. Напишите программу, удаляющую из текста все слова содержащие "абв".
# Используйте знания с последней лекции. Выполните ее в виде функции.

text = "абвгдеж рабав копыто мыло фабв Абкн абрыволк аБволк"
pattern = 'абв'


def filter_text(text: str, pattern):
    text_list = list(
        filter(lambda word: pattern not in word.lower(), text.split()))
    return ' '.join(text_list)


print("-------------------------\nЗадача 1")
print(filter_text(text, pattern))

# Задача 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.


class GameMode(enum.Enum):
    human_human = 1
    human_comp = 2


def choose_game_mode() -> enum.Enum:
    game_type = int(
        input("Выберите тип игры:\n1 - Игра с человеком\n2 - Игра с компьютером\n"))
    return GameMode.human_human if game_type == 1 else GameMode.human_comp


def get_players_names(game_mode: GameMode) -> tuple:
    if game_mode == GameMode.human_human:
        print("Введите имена игроков")
        player_1 = input("Имя первого игрока: ")
        player_2 = input("Имя второго игрока: ")

    else:
        print("Введите своё имя")
        player_1 = input("Ваше имя: ")
        player_2 = "Bot"
    return (player_1, player_2)


def get_position() -> tuple:
    pos = tuple(map(int, input("Куда ходим? (вертикаль горизонталь): ").split()))
    return (pos[0] - 1, pos[1] - 1)


def get_bot_position() -> tuple:
    pos_vert = randint(1, 3)
    pos_hor = randint(1, 3)
    return (pos_vert - 1, pos_hor - 1)


def draw_game_board(game_board: list):
    size = int(math.sqrt(len(game_board)))
    print()
    for j in range(size):
        print(f"     {j + 1}", end=' ')
    print()
    for i in range(size):
        print(f"{i+1} ", end=" ")
        for j in range(size):
            print(f"| {game_board[i * size + j]} |", end="  ")
        print()
    print()


def check_winners(board: list, symb: str, pos: tuple) -> bool:
    size = int(math.sqrt(len(board)))

    main_diag = board[::size + 1].count(symb)
    ad_diag = board[size - 1:-2:size - 1].count(symb)
    hor = board[pos[0] * size:pos[0] * size + size].count(symb)
    vert = board[pos[1]:pos[1] + 2 * size + 1:size].count(symb)
    if main_diag == size or ad_diag == size or hor == size or vert == size:
        return True

    return False


def tic_tac_toe():
    print("\tИгра 'крестики-нолики'")

    game_mode = choose_game_mode()
    symbols = ["X", "O"]
    players = get_players_names(game_mode)
    rnd = randint(0, 1)
    if game_mode == GameMode.human_human:
        players_symb = {symbols[0]: players[rnd], symbols[1]: players[1-rnd]}
    else:
        players_symb = {symbols[0]: players[0], symbols[1]: players[1]}

    print(
        f"Играют: {players_symb[symbols[0]]} - '{symbols[0]}' и  {players_symb[symbols[1]]} - '{symbols[1]}'")

    board_size = 3
    turn = 0
    has_winners = False
    game_board = ['.' for _ in range(board_size*board_size)]
    visited_pos = []

    draw_game_board(game_board)

    while (turn < board_size * board_size) and (not has_winners):
        current_symb = symbols[turn % 2]
        print(f"Ход игрока {players_symb[current_symb]} - {current_symb}")
        while True:
            pos = get_position()

            if pos[0] >= board_size or pos[0] < 0 or\
                    pos[1] >= board_size or pos[1] < 0:
                print(f"Диапазон допустимых ходов: (1 - {board_size})")
            else:
                if pos not in visited_pos:
                    visited_pos.append(pos)
                    break
                else:
                    print("Сюда уже ходили")
        game_board[pos[0] * board_size + pos[1]] = current_symb
        draw_game_board(game_board)
        has_winners = check_winners(game_board, current_symb, pos)
        if game_mode == GameMode.human_comp and not has_winners:
            turn += 1
            current_symb = symbols[1]
            print(f"Ход {players_symb[current_symb]} - {current_symb}")
            while True:
                bot_pos = get_bot_position()
                if bot_pos not in visited_pos:
                    visited_pos.append(bot_pos)
                    break
            game_board[bot_pos[0] * board_size + bot_pos[1]] = current_symb
            draw_game_board(game_board)
            has_winners = check_winners(game_board, current_symb, bot_pos)

        turn += 1

    print("Game Over!")
    print(f"Игрок {players_symb[current_symb]} выиграл!") if has_winners else print(
        "Ничья!")


print("-------------------------\nЗадача 2")
tic_tac_toe()


# Задача 3. Вот вам текст:
# Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется.
# Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее.
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень.
# Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче,
# в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил.
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть.
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

trash = ("ну", "короче", "в общем", "эээ", "эээээ…", "ээээ", "ээээ…",
         "ясен пень", "короче говоря", "как бы", "кажется", "кстати")

trash_text = '''
  Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. Ну,эээ, в общем, было лето, кажется.
Как бы тепло. Солнечно, короче. Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее.
И снова вышел, короче, из подъезда. Ясен пень, в магазин. В общем, лето на дворе, жарко, солнечно, птицы, короче, летают.
Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. Вышел из подъезда, короче. Лето на дворе, ясен пень.
Птицы поют, короче, солнечно. В общем, в магазин мне надо. Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ... короче,
в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил.
'''


def one_word_check(val: str) -> bool:
    sentence = val.lower().rstrip(".")
    for word in trash:
        if word == sentence:
            return False
    return True


def double_word_check(val: str) -> str:
    sentence = val.lower()

    for word in trash:
        idx_trash = sentence.find(word)
        if idx_trash == -1:
            continue
        else:
            sentence = sentence[:idx_trash] + sentence[idx_trash+len(word):]

    return sentence.strip().capitalize()


def filter_trash(text: str) -> str:
    text_list = [sentence.strip() for sentence in text.split(",")]

    temp_res = " ".join(list(filter(one_word_check, text_list)))
    text_list = [sentence.strip() for sentence in temp_res.split(" ")]
    temp_res = " ".join(list(filter(one_word_check, text_list)))
    text_list = [sentence.strip() for sentence in temp_res.split(".")]
    temp_res = ". ".join(list(map(double_word_check, text_list)))
    return temp_res


print("-------------------------\nЗадача 3")
print(f"Отфильтрованный текст:\n{filter_trash(trash_text)}")

# Задача 4. Чисто для тренировки новый функций, ничего сложного. Создайте два списка — один
# с названиями языков программирования, другой — с числами от 1 до длины первого плюс 1.
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
# написанного большими буквами. Вторая — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается,
# его номер заменяется на сумму очков. Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# С помощью reduce сложите получившиеся числа и верните из функции в качестве ответа.


def my_upper(val: str) -> str:
    return val.upper()


def check_tuple(val: tuple) -> bool:
    name = val[1]
    points = sum(map(lambda x: ord(x), name))
    if points % val[0] == 0:
        return True
    return False


def update_order(val: tuple) -> tuple:
    points = sum(map(lambda x: ord(x), val[1]))
    return (points, val[1])


def make_lang_pairs(order, lang):
    return list(zip(order, lang))


def filter_lang_pairs(lang_list: list) -> int:
    res = map(update_order, filter(check_tuple, lang_list))
    total_points = reduce(lambda sum, b: sum + b[0], res, 0)
    return total_points


def points_lang() -> int:
    languages = ["Python", "Java", "JavaScript",
                 "c/c++", "c#", "PHP", "Swift", "Kotlin", "Go", "TypeScript"]
    orders = [i for i in range(1, len(languages) + 1)]

    lang_pairs_list = make_lang_pairs(orders, map(my_upper, languages))
    total_points = filter_lang_pairs(lang_pairs_list)

    return total_points


print("-------------------------\nЗадача 4")
print(f"Сумма очков: {points_lang()}")

# Экстра-задачи:
# Задача 3 3. Начиная с числа 1 и двигаясь дальше вправо по часовой стрелке, образуется следующая спираль 5 на 5:

# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13

# Можно убедиться, что сумма чисел в диагоналях равна 101. (1+3+5+7+9+13+17+21+25)

# Какова сумма чисел в диагоналях спирали 1001 на 1001, образованной таким же способом?


def sum_of_diag(n):
    sum = 1
    a0 = 1
    for i in range(3, n + 1, 2):
        a0 = (i-2)**2 + i - 1
        sum += a0
        for _ in range(3):
            a0 += i - 1
            sum += a0
    return sum


print("-------------------------\nExtra задача 3")
n = 1001
print(f"Сумма чисел в диагоналях спирали {n} на {n}: {sum_of_diag(n)}")
