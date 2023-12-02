#!/usr/bin/env python3

def part_one():
    with open("input.txt") as file_in:
        total = 0
        valid = {"blue": 14, "green": 13, "red": 12}
        for line in file_in.read().splitlines():
            valid_game = True
            game = line.split(":")
            game_no = game[0].split(" ")
            game_no = game_no[1]
            game_sets = game[1].split(";")
            for pick in game_sets:
                pick = pick.lstrip(" ")
                pick = pick.replace(",", "")
                pick = pick.split(sep=" ")
                print(pick)
                for i in range(0, len(pick) - 1, 2):
                    if (valid[pick[i + 1]] < int(pick[i])):
                        valid_game = False

            if valid_game:
                total += int(game_no)
    # 2156
    print(total)


def part_two():
    with open("input.txt") as file_in:
        # total = 0
        total = []
        for line in file_in.read().splitlines():
            fewest = {"blue": 0, "green": 0, "red": 0}
            game = line.split(":")
            game_no = game[0].split(" ")
            game_no = game_no[1]
            game_sets = game[1].split(";")
            for pick in game_sets:
                pick = pick.lstrip(" ")
                pick = pick.replace(",", "")
                pick = pick.split(sep=" ")
                for i in range(0, len(pick) - 1, 2):
                    if int(pick[i]) > int(fewest[pick[i + 1]]):
                        fewest[pick[i + 1]] = pick[i]
                power = 1
            print(fewest)
            for val in fewest.values():
                power *= int(val)
            print(power)
            total.append(power)
    # 66909
    print(sum(total))

if __name__ == "__main__":
    # part_one()
    part_two()