playername = input("Добро пожаловать в игру Морской Бой! Введите ваше имя: ")
H, V, COUNT, icons = 7, 8, 0, ["*", "#", "X"]
field = [[f"| {COUNT}"] * H for _ in range(1, V)]
backfield = [[f"| {COUNT}"] * H for _ in range(1, V)]
ships_name, teams = ["трёхпалубного", "двухпалубного", "двухпалубного", "однопалубного", "однопалубного",
                     "однопалубного", "однопалубного", "однопалубного"], ["вашего", "вражеского"]
coord_bool = True


def game_input(ship_name, team):
    print(ship_name)
    while True:
        if len(backfield) < 20:
            player_move = input(
                f"{playername} Введите кординаты местоположения {team} {ship_name} корабля в формате (1 1) "
                f"через пробел: ").split()
            if len(player_move) != 2:
                print("Введите кординаты в формате (1 1) через пробел!")
                continue
            if not (player_move[0].isdigit() and player_move[1].isdigit()):
                print("Подсказка: При вводе кординат,используются только цифры")
                continue
            xp, yp = map(int, player_move)
            if (xp not in range(1, 7)) or (yp not in range(1, 7)):
                print("Подсказка: Введите кординаты цыфрами от 1 до 6")
                continue
            else:
                return xp, yp
        else:
            print(f"Многоуя кораблей")
            continue
    print("Final of input - True return!")
    return True


def get_ship_placement(coordinates, count_shoots):  #
    print(coordinates, "на входе GET_SHIP_PLACEMENT")
    x, y = map(int, coordinates)
    # print("Координаты в функцию гет шип плэйсмент получены", coordinates, korsa)
    if all((backfield[x][y] == "| 0", coordinates in count_shoots,
            field[x][y] == "| 0")):  # Проверка на повторность и выстрел ли это
        # print(f"{x, y} нет в fielde и нет в count_shoots - True - едем дальше")
        return True
    if all((field[x][y] == "| #", coordinates not in count_shoots)):
        print(
            f"Накладочка получилась - место уже занято в фиелде, но его нет среди выстрелов {field[x][y]}, Repeat ure move {playername}")
    if all((backfield[x][y] == "| X", coordinates in count_shoots)):
        print(
            f"Накладочка получилась,точка {coordinates} есть в бэкфиелде = X или кординаты есть в count_shot - False {backfield[x][y]}, Repeat ure move {playername}, потому что {count_shoots}")
        return False
    else:
        print(f"Кординаты {x} и {y} уже водились игркоком {playername}, повторите ход:D")
        count_shoots.pop(-1)
        return count_shoots


def back_field_setter_set(count_shoots):
    for i in count_shoots:
        back_field_setter(i)
    # print("count_shoots Printing - Complete!")


def back_field_setter(coordinats):
    x, y = map(int, coordinats)
    square_range_y = range(y - 1, y + 2)
    square_range_x = range(x - 1, x + 2)
    square_point = []
    for i in square_range_y:
        for j in square_range_x:
            square_point.append((j, i))
            if any((i == 7, j == 7)):
                # print(f"ограничение по Y{j} or X{i}")
                pass
            # if (j, i) == coordinats:
            #     backfield[x][y] = f"| {icons[1]}"
            #     print("___________YEah - im find this fucking double______________________________________")
            #     pass
            else:
                # print(j, i, x, y, "На входе в функцию")
                if field[j][i] == f"| {icons[0]}":
                    # print("Пропуск по значку", "field[i][j] - ", field[i][j], "backfield[i][j] - ")
                    continue
                if field[x][y] == f"| {icons[0]}":
                    field[j][i] = f"| {icons[2]}"
                    # print(field[j][i], j, i, y, x, "Если Х и У *")
                else:
                    backfield[j][i] = f"| {icons[2]}"
                    # print("WTF", "ELSE", backfield[j][i])
    # print(square_point, "\n Полный лист backfield вокруг выстрела")
    # for i in square_point:
    #     get_ship_placement(i, square_point)

    # if (x, y) == i:
    #     print(i, "Повторение")
    #     field[x][y] = f"| {icons[1]}"  # Временно расположение игрока передает эта функция,в идеале
    #     print("Ход после удалния", field[x][y], backfield[x][y])


def set_cordinats(count_shoots):
    for i in count_shoots:
        battleship_printing(i)
    # print("count_shoots Printing - Complete!")


def battleship_printing(coor):  # Назначениекординат
    x, y = map(int, coor)
    # print(f"Printuju {x} {y}", (x == 0 or y == 0), (x > 6 or y > 6))
    # if x == 0 or y == 0 and x > 6 or y > 6:
    #     print(f"{x} or {y} = 0 или больше 6")
    #     pass
    # else:
    #     print(f"{x} or {y} != 0 или меньше 6")
    if coor not in backfield:
        field[x][y] = f"| {icons[1]}"
        # print(f" {x} or {y} ne v backfield", backfield)
    # elif x not in field:
    #     field[x][y] = f"| {icons[1]}"
    #     print(f" {x} or {y} ne v field", field)
    # print(field)
    # print("Printing закончен")


def check_ship(coordinates, count_shoots):
    x, y = map(int, coordinates)
    count_shoots_list = [i for sublist in count_shoots for i in sublist]
    # print(count_shoots)
    pos = [[*range(1, 4)], [*range(2, 5)], [*range(3, 6)], [*range(4, 7)]]
    # print(f"Печать {pos} (Печать: Х и У и ПОЗИЦИЮ) num, Только У")
    pos_x = count_shoots_list[::2]  # iksy
    pos_y = count_shoots_list[1::2]  # igriky
    while True:
        if len(count_shoots) < 4:
            if all((x in pos_x[:0], y in range(y - 1, y + 2))) or any((y in pos_y[:0], x in range(x - 1, x + 2))):
                # print("ПРОХОДИТ ПО общим УСЛОВИЯМ", count_shoots, "Длина  count_shoots -", len(count_shoots))
                if len(count_shoots) < 2:
                    # print("1 kletka")
                    return True
                elif len(count_shoots) == 2 and (
                        [pos_x[0]] * len(pos_x) == pos_x and y in range(pos_y[0] - 1, pos_y[0] + 2)) or [
                    pos_y[0]] * len(
                    pos_y) == pos_y and x in range(pos_x[0] - 1, pos_x[0] + 2):
                    # print(f"Зашла как родимая 2 клетка", len(count_shoots) == 2)
                    return True
                elif len(count_shoots) == 2:
                    print(f"Повторите ввод {len(count_shoots)} пары кординат", {pos_x[0]}, {pos_x[1]}, {pos_y[0]},
                          {pos_y[1]})
                    count_shoots.pop(1)
                    # print("После удаления", count_shoots)
                    return False
                elif len(count_shoots) == 3 and any(
                        ((pos_y.sort() in pos or pos_y in pos[::-1]) and ([pos_x[0]] * len(pos_x) == pos_x),
                         (pos_x.sort() in pos or pos_x in pos[::-1]) and ([pos_y[0]] * len(pos_y) == pos_y))):
                    # print(pos_x, pos_y, count_shoots, {pos_x[0]},
                    #       {pos_x[1]}, {pos_y[0]},
                    #       {pos_y[1]}, "pos_y in pos -", pos_y in pos, "pos_y in pos[::-1] -", pos_y in pos[::-1],
                    #       "([pos_x[0]] * len(pos_x) == pos_x) -", ([pos_x[0]] * len(pos_x) == pos_x))
                    # print(
                    #     f"Кординаты верны, трёхпалубник создан - Количество кораблей на даннный момент 1", pos_y in pos,
                    #                                                                                        pos_y in pos[
                    #                                                                                                 ::-1],
                    #                                                                                        [pos_x[
                    #                                                                                             0]] * len(
                    #                                                                                            pos_x) == pos_x,
                    #     "///", pos_x in pos, pos_x in pos[::-1], [pos_y[0]] * len(pos_y) == pos_y)
                    return True
                elif len(count_shoots) == 3:
                    print(f"Повторите ввод {len(count_shoots)} пары кординат")
                    count_shoots.pop()
                    return False
                else:
                    break
            else:
                print("Введите 3 пары кординат")
                break
        if len(count_shoots) < 8:
            if len(count_shoots) == 4 and backfield[x][y] == "| 0":
                # print("Первая точка 1 двухпалубного создана", backfield[x][y], coordinates not in backfield, backfield)
                return True
            elif len(count_shoots) == 4 and backfield[x][y] != "| 0":
                count_shoots.pop(-1)
                print("Не прошла первая точка первого двухпалубника", count_shoots)
                return False

            if all((len(count_shoots) == 5, backfield[x][y] == "| 0", (
                                                                              pos_x[3] == pos_x[4] and y in range(
                                                                          pos_y[3] - 1, pos_y[3] + 2)) or pos_y[3] ==
                                                                      pos_y[4] and x in range(pos_x[3] - 1,
                                                                                              pos_x[3] + 2))):
                # print("Вторая точка 1 двухпалубного создана", coordinates not in backfield)
                # print(backfield, f"\n {field}", count_shoots,
                #       f"\n Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, второй ship пошёл")
                return True
            elif len(count_shoots) == 5:
                count_shoots.pop(-1)
                print("Не прошла вторая точка первого двухпалубника", count_shoots)
                return False

            if len(count_shoots) == 6 and backfield[x][y] == "| 0":
                # print("Первая точка 2 двухпалубного создана")
                return True

            elif len(count_shoots) == 6 and backfield[x][y] != "| 0":
                count_shoots.pop(-1)
                print("Не прошла первая точка 2 двухпалубника", count_shoots)
                return False

            if all((len(count_shoots) == 7, backfield[x][y] == "| 0", (
                                                                              pos_x[5] == pos_x[6] and y in range(
                                                                          pos_y[5] - 1, pos_y[5] + 2)) or pos_y[5] ==
                                                                      pos_y[6] and x in range(pos_x[5] - 1,
                                                                                              pos_x[5] + 2))):
                # print("Вторая точка 2 двухпалубного создана", backfield[x][y])
                # print(backfield, f"\n {field}", count_shoots,
                #       f"\n Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, второй пошёл")
                return True
            elif len(count_shoots) == 7 and backfield[x][y] != "| 0":
                count_shoots.pop(-1)
                print("Не прошла вторая точка 2 двухпалубника", count_shoots)
                return False
            else:
                print("Lahaet", len(count_shoots))
                count_shoots.pop(len(count_shoots) - 1)
                continue
        if len(count_shoots) < 11:
            if backfield[x][y] == "| 0":
                # print(f"Проверка кординат {coordinates} на размещения в backfiel!!! - > field {field} Backfield")
                # print("Printuju odnoekletochnye")
                return True
            elif backfield[x][y] == "| X":
                # print("Lahaet - este raz", len(count_shoots))
                count_shoots.pop(-1)
            else:
                print("Одноклеточный ещё раз")
                return False
        if len(count_shoots) == 11:
            if backfield[x][y] == "| 0":
                # print(f"Проверка кординат {coordinates} на размещения в backfiel!!! - > field {field} Backfield")
                print("Rasstanovka okonchena")
                return True
            elif backfield[x][y] == "| X":
                print("Lahaet - este raz", len(count_shoots))
                count_shoots.pop(-1)
            else:
                print("Одноклеточный ещё раз")
                return False
        else:
            print(f"Игра началась!,Все {len(count_shoots)} клеток расположены расположены - выход из проверки")
            break


# field[x] == field[i][y]
# class BotBattleship(Battleship):
#     def __init__(self, field, ships_count):
#         self.field = field
#         self.ships_count = ships_count
# field[0][i] = f"|{i}"
#     def set_cord(self):
#         while True:
#             if not bot.cord_bool:
#                 bot_move = [random.randint(1, 6), random.randint(1, 6)]
#                 xb, yb = map(int, bot_move)
#                 print(f"Bot: {xb}, {yb}")
#             return xb, yb


def vyvod(field):  # Ебанная транжира моего времени,матрица начинается с нуля по горизонтали...ИСПРАВИТЬ
    print("___________________________")
    print("\n______Поле Игрока_____")
    print("    1   2   3   4   5   6")
    # specialHandling =
    for i in range(1, 7):
        tas = field[i]
        field[i][0] = i
        print(*field[i], "|")
        if tas[0] != "| 0 ":
            continue
        print("\n______Поле соперника_____")
        print("    1   2   3   4   5   6")
        for i in range(1, 7):
            print(str(i), *backfield[i], "|")
    return field


import random


def battleship(count_shoots):
    ships_count = 0
    while True:
        coordinates = [random.randint(1, 6), random.randint(1, 6)]  # game_input(ships_name[ships_count], teams[0])
        count_shoots.append(coordinates)
        if len(count_shoots) < 4:
            if get_ship_placement(coordinates, count_shoots):
                if check_ship(coordinates, count_shoots):
                    set_cordinats(count_shoots)
                    vyvod(field)
                    vyvod(backfield)
                if len(count_shoots) == 3:
                    back_field_setter_set(count_shoots)
                    vyvod(field)
                    vyvod(backfield)
                    ships_count += 1
                    # print(get_ship_placement(coordinates, count_shoots),
                    #       f"Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, первый пошёл")
                    continue
                else:
                    print(
                        f"{playername}, Для заполнения , {ships_name} корабля заполните три клетки подряд с одинаковым "
                        f"цифровым значением то горизонтали или вертикали")
        elif len(count_shoots) < 8:
            if get_ship_placement(coordinates, count_shoots):
                if check_ship(coordinates, count_shoots):
                    set_cordinats(count_shoots)
                    vyvod(field)
                    vyvod(backfield)
                if len(count_shoots) == 5:
                    # print(backfield, f"\n {field}", count_shoots,
                    #       f"\n Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, второй пошёл")
                    back_field_setter_set(count_shoots)
                    vyvod(field)
                    vyvod(backfield)
                    ships_count += 1
                    continue
                if len(count_shoots) == 7:
                    back_field_setter_set(count_shoots)
                    # print(get_ship_placement(coordinates, count_shoots),
                    #       f"Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, 3 пошёл")
                    vyvod(field)
                    vyvod(backfield)
                    ships_count += 1
                    continue
                else:
                    print(
                        f"{playername}, Для заполнения , {ships_name} корабля заполните 2 клетки подряд с одинаковым "
                        f"цифровым значением то горизонтали или вертикали")
            else:
                count_shoots.pop(-1)
                continue
        elif len(count_shoots) < 11:
            if get_ship_placement(coordinates, count_shoots):
                if check_ship(coordinates, count_shoots):
                    set_cordinats(count_shoots)
                    back_field_setter(coordinates)
                    vyvod(field)
                    vyvod(backfield)
                    ships_count += 1
                    continue
                elif len(count_shoots) == range(8, 12):
                    pass
                    # print(get_ship_placement(coordinates, count_shoots),
                    #       f"Кординаты {len(count_shoots)} точки {ships_name[0]} заданы успешно, 4 пошёл")
                else:
                    print(
                        f"{playername}, Для заполнения , {ships_name} корабля заполните 2 клетки подряд с одинаковым "
                        f"цифровым значением то горизонтали или вертикали")
            else:
                count_shoots.pop(-1)
                vyvod(field)
                vyvod(backfield)
                continue
        elif len(count_shoots) == 11 and get_ship_placement(coordinates, count_shoots):
            print("Rasstanovka okonchena", count_shoots)
            set_cordinats(count_shoots)
            ships_count += 1
            back_field_setter(coordinates)
            vyvod(field)
            vyvod(backfield)
            return count_shoots
        elif len(count_shoots) == 11:
            print(f"Error kooordinaty {len(count_shoots) - 1} ne proshli", count_shoots)
            count_shoots.pop(-1)
            if "| 0" not in field:
                print("Нет свобоного места!!!", len(field))
            #     for i in range(3):
            #         x, y = map(int, count_shoots[-1])
            #         square_range_y = range(y - 1, y + 2)
            #         square_range_x = range(x - 1, x + 2)
            #         for i in square_range_y:
            #             for j in square_range_x:
            #                 if any((i == 7, j == 7)):
            #                     pass
            #                 else:
            #                     if field[x][y] == f"| {icons[1]}":
            #                         field[x][y] = "| 0"
            #                     if backfield[j][i] == f"| {icons[2]}":
            #                         backfield[j][i] = "| 0"
            #                     if backfield[j][i] == "| 0"
            #                         pass
            #    count_shoots.pop(-1)
            # back_field_setter_set(count_shoots)
            # print(
            #     "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print("Вывод после стирания",count_shoots)
            # print(
            #     "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
            # print(count_shoots)
            # vyvod(field)
            # vyvod(backfield)
        else:
            return True


def main_game():
    ships, shoots_count, ships_coordinates, shoots = 7, 0, [], []
    ships_coord = battleship(ships_coordinates)
    move = "P"
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("GAME STARTED")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    while True:
        vyvod(field)
        shoot = [random.randint(1, 6), random.randint(1, 6)]  # game_input("", teams[1])
        x, y = map(int, shoot)
        # print(x, y)
        if ships > 0:
            shoots_count += 1
            # print("ships - ", ships)
            if field[x][y] == f"| {icons[0]}" or field[x][y] == f"| {icons[2]}":
                print("Повторный",shoots_count, ships)
                shoots_count -= 1
                # print("Кол-во ходов после сокращения - ", shoots_count)
                continue
            # ships_coordinates.append([x, y])
            field[x][y] = f"| {icons[0]}"
            if list(shoot) not in ships_coord:
                pass
                # print("Miss","!!!", x, y, "!!!", shoots_count)
            elif list(shoot) in ships_coord:
                # print("Hit!", "!!!", x, y, "!!!", shoots_count, ships_coord)
                shoots.append([x, y])
                # print("shoots-", shoots)
                if all((ships_coord[0] in shoots, ships_coord[1] in shoots, ships_coord[2] in shoots)):
                    back_field_setter_set((ships_coord[0], ships_coord[1], ships_coord[2]))
                    # print("Трёхпалубный в shoots -> back_field_set")
                    ships -= 1
                    shoots.remove(ships_coord[0])
                    shoots.remove(ships_coord[1])
                    shoots.remove(ships_coord[2])
                if all((ships_coord[3] in shoots, ships_coord[4] in shoots)):
                    back_field_setter_set((ships_coord[3], ships_coord[4]))
                    # print("Первый двухпалубный в shoots -> back_field_set")
                    ships -= 1
                    shoots.remove(ships_coord[3])
                    shoots.remove(ships_coord[4])
                if all((ships_coord[5] in shoots, ships_coord[6] in shoots)):
                    back_field_setter_set((ships_coord[5], ships_coord[6]))
                    # print("Второй двухпалубный в shoots -> back_field_set")
                    ships -= 1
                    shoots.remove(ships_coord[5])
                    shoots.remove(ships_coord[6])
                if ships_coord[7] in shoots:
                    # print("1 Одноклеточный в shoots -> back_field_set")
                    back_field_setter(shoot)
                    shoots.remove(ships_coord[7])
                    ships -= 1
                if ships_coord[8] in shoots:
                    # print("2 Одноклеточный в shoots -> back_field_set")
                    back_field_setter(shoot)
                    shoots.remove(ships_coord[8])
                    ships -= 1
                if ships_coord[9] in shoots:
                    # print("3 Одноклеточный в shoots -> back_field_set")
                    back_field_setter(shoot)
                    shoots.remove(ships_coord[9])
                    ships -= 1
                if ships_coord[10] in shoots:
                    # print("4 Одноклеточный в shoots -> back_field_set")
                    back_field_setter(shoot)
                    shoots.remove(ships_coord[10])
                    ships -= 1
                else:
                    # print("ELSE", shoots, type(shoots), type(ships_coord))
                    continue
        elif ships == 0:
            print(
                f"Поздравляем победой {playername}! - Вы выиграли партию произведя всего {shoots_count} выстрела и ваш коэфициент точности cоставляет",  ((len(ships_coord) / shoots_count) * 100), "%")
            return True
            # if move == "P":
            #     move = "B"
        else:
            print("Lahaet")
            continue

    # for i in range(2):
    #     game_input(ships_name[1], team[0])
    #     if game_input:
    #         vyvod(field)
    # for i in range(4):
    #     if game_input:
    #         game_input(ships_name[2], team[0])  # Убрать ship, korsa
    #     vyvod(field)


main_game()
# try:
#     def ship_border():
#         backfield
# except:  # Ошибка:
#     pass
#     # *Код
#     # отлова *
# else:
#     pass
#     # *Код, который
#     # выполнится
#     # если
#     # всё
#     # хорошо
#     # прошло
#     # в
#     # блоке
#     # try
#
# finally:
#     pass
#     # *Код, который
#     # выполнится
#     # по
#     # любому *
# pass
# a = [4.3 4.6 4]
# res = []
# #return True if
#
#

# При вводе 2,2,2,3 допускает ввод 4,4
