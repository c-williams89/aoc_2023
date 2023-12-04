def part_one():
    # arr = [[0]*140]*140
    arr = [0] * 140

    symbols = "%#/*-=@+$&"
    total = 0
    row = 0
    with open("/home/student/aoc23/aoc_2023/day_03/input.txt", "r") as file_in:
        for line in file_in.read().splitlines():
            # print(row)
            col = 0
            arr[row] = []
            while col < len(line):
                if line[col].isdigit():
                    start_index = col
                    new_num = ""
                    try:
                        while line[col].isdigit():
                            new_num += line[col]
                            col += 1
                    except IndexError:
                        pass
                    try:
                        for i in range(start_index, col):
                            # arr[row][i] = int(new_num)
                            arr[row].append(int(new_num))
                    except IndexError:
                        pass
                else:
                    arr[row].append(line[col])
                    # arr[row][col] = line[col]
                    col += 1
            row += 1

        print(arr[1])
        
        cont_count = 0
        total = 0
        total_list = list()
        found = False
        for row in range(140):
            for col in range(140):
                if found and cont_count > 1:
                    cont_count -= 1
                    continue

                cont_count = 0
                found = False
                if str(arr[row][col]).isdigit():
                    start = col
                    # try:
                    while start <= 139 and str(arr[row][start]).isdigit():
                        cont_count += 1
                        start += 1
                    try:
                        if str(arr[row - 1][col - 1]) in symbols:
                            total += int(arr[row][col])
                            total_list.append(int(arr[row][col]))
                            found = True
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass
                    
                    try:
                        if str(arr[row - 1][col]) in symbols:
                            total += int(arr[row][col])
                            total_list.append(int(arr[row][col]))
                            found = True
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass
                    
                    try:
                        if str(arr[row - 1][col + 1]) in symbols:
                            total += int(arr[row][col])
                            total_list.append(int(arr[row][col]))
                            found = True
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass
                    
                    try:
                        if str(arr[row][col - 1]) in symbols:
                            total_list.append(int(arr[row][col]))
                            found = True
                            total += int(arr[row][col])
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass

                    try:
                        if str(arr[row][col + 1]) in symbols:
                            total_list.append(int(arr[row][col]))
                            found = True
                            total += int(arr[row][col])
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass

                    try:
                        if str(arr[row + 1][col - 1]) in symbols:
                            total_list.append(int(arr[row][col]))
                            found = True
                            total += int(arr[row][col])
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass

                    try:
                        if str(arr[row + 1][col]) in symbols:
                            total += int(arr[row][col])
                            total_list.append(int(arr[row][col]))
                            found = True
                            continue
                        else:
                            found = False

                    except IndexError:
                        pass

                    try:
                        if str(arr[row + 1][col + 1]) in symbols:
                            total += int(arr[row][col])
                            total_list.append(int(arr[row][col]))
                            found = True
                            continue
                        else:
                            found = False
                    except IndexError:
                        pass

        # print(sum(total_set))
        print(total)
        print(total_list)
        # print(counter)
        # 348775 too low
        # 824021 too high
        # 435098 too low
        # 498559 CORRECT
        # 497933?
        
def part_two():
    arr = [0] * 140

    symbols = "%#/*-=@+$&"
    row = 0
    with open("/home/student/aoc23/aoc_2023/day_03/input.txt", "r") as file_in:
        for line in file_in.read().splitlines():
            col = 0
            arr[row] = []
            while col < len(line):
                if line[col].isdigit():
                    start_index = col
                    new_num = ""
                    try:
                        while line[col].isdigit():
                            new_num += line[col]
                            col += 1
                    except IndexError:
                        pass
                    try:
                        for i in range(start_index, col):
                            arr[row].append(int(new_num))
                    except IndexError:
                        pass
                else:
                    arr[row].append(line[col])
                    col += 1
            row += 1
    discovered = dict()
    for row in range(140):
        for col in range(140):
            discovered[(row, col)] = set()

    total = 0
    for row in range(140):
        for col in range(140):
            curr = (row, col)
            if str(arr[row][col]) in symbols:
                if isinstance(arr[row - 1][col - 1], int):
                    discovered[curr].add(arr[row - 1][col - 1])
                if isinstance(arr[row - 1][col], int):
                    discovered[curr].add(arr[row - 1][col])
                if isinstance(arr[row - 1][col + 1], int):
                    discovered[curr].add(arr[row - 1][col + 1])
                if isinstance(arr[row][col - 1], int):
                    discovered[curr].add(arr[row][col - 1])
                if isinstance(arr[row][col + 1], int):
                    discovered[curr].add(arr[row][col + 1])
                if isinstance(arr[row + 1][col - 1], int):
                    discovered[curr].add(arr[row + 1][col - 1])
                if isinstance(arr[row + 1][col], int):
                    discovered[curr].add(arr[row + 1][col])
                if isinstance(arr[row + 1][col + 1], int):
                    discovered[curr].add(arr[row + 1][col + 1])
    
    for symbol in discovered.values():
        if len(symbol) == 2:
            gear_total = 1
            for value in symbol:
                gear_total *= value
            total += gear_total

    print(total)
    # 72246648

if __name__ == "__main__":
    # part_one()
    part_two()