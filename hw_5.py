# Задача 1. Напишите программу, удаляющую из текста все слова содержащие "абв".
# Используйте знания с последней лекции. Выполните ее в виде функции.


import math
from random import randint
from unittest import result


text = "абвгдеж рабав копыто фабв Абкн абрыволк аБволк"
pattern = 'абв'


def filter_text(text: str, pattern: str):
    text_list = text.split()
    for char in pattern:
        text_list = list(
            filter(lambda word: char not in word.lower(), text_list))
    return ' '.join(text_list)


print("-------------------------\nЗадача 2")
print(filter_text(text, pattern))

# Задача 2. Вы когда-нибудь играли в игру "Крестики-нолики"? Попробуйте создать её, причем чтобы сыграть в нее можно было в одиночку.


def get_players_names() -> tuple:
    print("Введите имена игроков")
    player_1 = input("Имя первого игрока: ")
    player_2 = input("Имя второго игрока: ")
    return (player_1, player_2)


def get_position() -> tuple:
    pos = tuple(map(int, input("Куда ходим? ").split()))
    return (pos[0] - 1, pos[1] - 1)


def draw_game_board(game_board: dict):
    size = int(math.sqrt(len(game_board)))
    print()
    for j in range(size):
        print(f"     {j + 1}", end=' ')
    print()
    for i in range(size):
        print(f"{i+1} ", end=" ")
        for j in range(size):
            print(f"| {game_board.get(i * size + j)} |", end="  ")
        print()
    print()


def check_winners(board: dict, symb: str, pos: tuple) -> bool:
    size = int(math.sqrt(len(board)))
    result = False
    if pos[0] == pos[1] == 1:
        if tuple(board.values())[::4].count(symb) == size or \
                tuple(board.values())[2::2].count(symb) == size or \
                tuple(board.values())[pos[0] * size:pos[0] * size + size].count(symb) == size or \
                tuple(board.values())[pos[1]::size].count(symb) == size:
            result = True
    else:
        if tuple(board.values())[pos[0] * size:pos[0] * size + size].count(symb) == size or \
                tuple(board.values())[pos[1]::size].count(symb) == size:
            result = True

    return result


def tic_tac_toe():
    symbols = ["X", "O"]
    players = get_players_names()
    rnd = randint(0, 1)
    players_symb = {symbols[0]: players[rnd], symbols[1]: players[1-rnd]}

    print("\tИгра 'крестики-нолики'")
    print(
        f"Играют: {players_symb[symbols[0]]} - '{symbols[0]}' и  {players_symb[symbols[1]]} - '{symbols[1]}'")

    board_size = 3
    turn = 0
    has_winners = False
    game_board = {i: '.' for i in range(board_size*board_size)}
    visited_pos = []

    draw_game_board(game_board)

    while (turn < board_size * board_size) and (not has_winners):
        current_symb = symbols[turn % 2]
        print(f"Ход игрока {players_symb[current_symb]} - {current_symb}")
        while True:
            pos = get_position()
            if pos not in visited_pos:
                visited_pos.append(pos)
                break
            else:
                print("Сюда уже ходили")
        game_board[pos[0] * board_size + pos[1]] = current_symb
        draw_game_board(game_board)
        has_winners = check_winners(game_board, current_symb, pos)
        turn += 1
    print("Game Over!")
    print(f"Игрок {players_symb[current_symb]} выиграл!") if has_winners else print(
        "Ничья!")


tic_tac_toe()
