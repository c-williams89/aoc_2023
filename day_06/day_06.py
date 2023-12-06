#!/usr/bin/evn python3
import math
def part_one():
    time_dist = [[56, 499], [97, 2210], [77, 1097], [93, 1440]]
    num_ways = []
    for race in time_dist:
        best_time = race[1]
        winning = 0
        for i in range(race[0]):
            speed = i
            distance = i * (race[0] - i)
            if distance > best_time:
                winning += 1
        num_ways.append(winning)
    print(math.prod(num_ways))
    
    # 1710720 Correct

def part_two():
    # time_dist = [[56977793, 499221010971440]]
    time_dist = [56977793, 499221010971440]

    # num_ways = []
    # for race in time_dist:
    # best_time = time_dist[1]
    winning = 0
    for i in range(int(time_dist[0] / 2) + 1):
        distance = i * (time_dist[0] - i)
        if distance > time_dist[1]:
            winning += 1
    
    # print(f"{winning}")
    print(f"{winning * 2}")
    #     best_time = race[1]
    #     winning = 0
    #     for i in range(race[0]):
    #         # if i % 100 == 0:
    #         #     print(f"Processed {i} races")
    #         speed = i
    #         distance = i * (race[0] - i)
    #         if distance > best_time:
    #             winning += 1
    #     num_ways.append(winning)
    # print(math.prod(num_ways))
    # 35349468 Correct
    #time: 20
    #time: 8 s
    pass


if __name__ == "__main__":
    # part_one()
    part_two()