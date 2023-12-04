def part_one():
    i = 0
    arr = []*140
    symbols = "%#/*-=@+$&"
    total = 0
    with open("input.txt", "r") as file_in:
        arr = [0]*140
        for line in file_in.read().splitlines():
            for idx, character in enumerate(line):
                if character.isdigit():
                    new_num = ""
                    while line[idx].isdigit():
                        new_num += character
                        line[idx - 1] = "."
            arr[i][idx] = character
            # arr.append(line)


    # for line_no, line in enumerate(arr):
    #     print(line)
    #     for idx, symbol in enumerate(line):
    #         if symbol.isdigit():
    #             re_num = 0
    #             digit_count = 1
    #             while symbol.isdigit():
    #                 # line += 1
    #                 re_num += symbol
    #                 digit_count += 1
            # if symbol.isdigit():
            #     pass
            # if symbol in symbols:
            #     if line_no == 0:
            #         if line[idx - 1].isdigit():

            #         pass
            #     elif line_no == 139:
            #         pass
            #     else:
            #         pass

    for line in arr:
        pass
    print(arr)
    # print(lines)

def part_two():
    pass

if __name__ == "__main__":
    part_one()
    # part_two()