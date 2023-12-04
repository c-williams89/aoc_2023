#!/usr/bin/env python3

def part_one():
    # total would be matches squared
    with open("./input.txt", "r") as file_in:
        # line = file_in.readline()
        total = 0
        # print(line)
        for line in file_in:
            card = line.split(sep=":")
            card = card[1].split("|")
            card[0] = card[0].strip()
            card[1] = card[1].strip()
            have = card[0].split()
            winning = card[1].split()
            # print(card)
            # print(have)
            # print(winning)
            current = 0
            for num in have:
                if num in winning:
                    if current == 0:
                        current = 1
                    else:
                        current *= 2
            total += current
        print(total)


def part_two(): 
    with open("./input.txt", "r") as file_in:
        total = 0
        # duplication = [1 for _ in range(6)]
        duplication = [1 for _ in range(202)]
        current_card = 0
        for line in file_in:
            print(f"processing card: {current_card}")
            card = line.split(sep=":")
            card = card[1].split("|")
            card[0] = card[0].strip()
            card[1] = card[1].strip()
            have = card[0].split()
            winning = card[1].split()
            try:
                for _ in range(0, duplication[current_card]):
                    current = 0
                    for num in have:
                        if num in winning:
                            current += 1

                    for i in range(1, current + 1):
                        try:
                            duplication[current_card + i] += 1
                        except IndexError:
                            pass
                total += current * duplication[current_card]
            except IndexError:
                pass
            current_card += 1
        # print(total)
    print(duplication)
    total = sum(duplication)
    print(total)
    # [1, 2, 4, 8, 14, 1]
    # 15455663

if __name__ == "__main__":
    # part_one()
    part_two()