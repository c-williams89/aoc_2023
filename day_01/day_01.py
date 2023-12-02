def main():
    total = 0
    with open("input.txt") as file_in:
        for line in file_in.read().splitlines():
            num = ""
            line = line.lstrip("abcdefghijklmnopqrstuvwxyz")
            line = line.rstrip("abcdefghijklmnopqrstuvwxyz")
            num += line[0]
            num += line[-1]
            total += int(num)
    print(total)

def part_two():
    num_dict = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    
    nums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    total = 0
    with open("./input.txt", "r") as file_in:
        for line in file_in.read().splitlines():
            l_index = len(line)
            r_index = -1
            l_num = ''
            r_num = ''
            num_str = ""
            for num in nums:
                index = line.find(num)
                if index < l_index and index > -1:
                    l_index = index
                    if num.isdigit():
                        l_num = num
                    else:
                        l_num = num_dict[num]
            for num in nums:
                index = line.rfind(num)
                if index > r_index:
                    r_index = index
                    if num.isdigit():
                        r_num = num
                    else:
                        r_num = num_dict[num]

            num_str += l_num
            num_str += r_num
            total += int(num_str)
        print(total)


if __name__ == "__main__":
    # main()
    part_two()