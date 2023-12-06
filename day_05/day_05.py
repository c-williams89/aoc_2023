#!/usr/bin/env python3

def part_one():
    # file_in = open("/home/student/aoc23/aoc_2023/day_05/input2.txt", "r")
    file_in = open("./input.txt", "r")
    str_list = file_in.readlines()
    seed_list = str_list[0].replace("seeds: ", "")
    seed_list = seed_list.split()
    str_list.pop(0)
    str_list.pop(0)
    seed_to_soil = []
    soil_to_fertilizer = []
    fert_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_hum = []
    hum_to_loc = []

    i = 1
    while str_list[i] != "\n":
        # str_list[i] = int(str_list[i])
        seed_to_soil.append(str_list[i].split())
        # for seed in seed_to_soil:
        #     seed = int(seed)
        # val = seed for int(seed) in seed_to_soil
        i += 1
    i += 2
    while str_list[i] != "\n":
        soil_to_fertilizer.append(str_list[i].split())
        i += 1
    i += 2
    while str_list[i] != "\n":
        fert_to_water.append(str_list[i].split())
        i += 1
    i += 2
    while str_list[i] != "\n":
        water_to_light.append(str_list[i].split())
        i += 1
    i += 2
    while str_list[i] != "\n":
        light_to_temp.append(str_list[i].split())
        i += 1
    i += 2
    while str_list[i] != "\n":
        temp_to_hum.append(str_list[i].split())
        i += 1
    i += 2
    try:
        while str_list[i]:
            hum_to_loc.append(str_list[i].split())
            i += 1
    except IndexError:
        pass

    # print(seed_list)
    # print(seed_to_soil)
    # print(soil_to_fertilizer)
    # print(fert_to_water)
    # print(water_to_light)
    # print(light_to_temp)
    # print(temp_to_hum)
    # print(hum_to_loc)
    for i, seed in enumerate(seed_list):
        for map in seed_to_soil:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        # print(seed_list)
        for map in soil_to_fertilizer:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        # print(seed_list)
        for map in fert_to_water:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        for map in water_to_light:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        for map in light_to_temp:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        for map in temp_to_hum:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
        for map in hum_to_loc:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    print(seed_list)
    print(min(seed_list))
    # 196167384 CORRECT

def part_two():
    # file_in = open("/home/student/aoc23/aoc_2023/day_05/input2.txt", "r")
    file_in = open("/home/student/aoc23/aoc_2023/day_05/input.txt", "r")
    str_list = file_in.readlines()
    seed_list = str_list[0].replace("seeds: ", "")
    seed_list = seed_list.split()
    seed_set = set()
    seeds = []
    for seed in seed_list:
        seeds.append(int(seed))
    print(max(seeds))
    # start = seed_list[0]
    # end = seed_list[0]
    # for i in range(len(seed_list)):
    #     print(i)
    #     if seed_list[i] < start:
    #         start = seed_list[i]
    #     if seed_list[i] > end:
    #         end = seed_list[i]
    # print(seed_list)
    # start = max(seed_list)
    # end = max(seed_list)
    range_start = int(seed_list[0])
    range_end = int(seed_list[1]) + int(seed_list[0])
    # print(f"start: {start}, end: {end}")
    ranges = []
    for i in range(0, len(seed_list), 2):
        ranges.append((int(seed_list[i]), int(seed_list[i]) + int(seed_list[i + 1])))
    print(ranges)
    mins = []
    maxes = []
    print(min(ranges[1]))
    print(max(ranges[1]))
    for i in range(2, len(seed_list), 2):
        mins.append(int(seed_list[i]))
        maxes.append(int(seed_list[i]) + int(seed_list[i + 1]))
        print(i)
        start = int(seed_list[i])
        end = int(seed_list[i]) + int(seed_list[i + 1])
        # if start < range_start:
        #     if end >= start:

        #     if end >= range_end:
        #         range_start = start
        #         range_end = end
        #     if end >= sta
        if start <= range_start and end >= range_end:
            range_start = start
            range_end = end
        elif start < range_start and end >= range_start:
            range_start = start
        elif end > range_end and start <= range_end:
            range_end = end
        else:
            print("Not in range")
        # print(f"start: {seed_list[i]}, end: {seed_list[i] + seed_list[i + 1]}")
        # print(f"Adding set {i}")
        # for j in range(int(seed_list[i]), int(seed_list[i]) + int(seed_list[i + 1])):
        #     # seed_set.add(int(j))
        #     pass
    
    # print("populated seed set")
    mins.extend(maxes)
    print(len(mins))
    print(mins)
    str_list.pop(0)
    str_list.pop(0)
    seed_to_soil = []
    soil = set()
    fert = set()
    water = set()
    light = set()
    temp = set()
    hum = set()
    loc = set()
    soil_to_fertilizer = []
    fert_to_water = []
    water_to_light = []
    light_to_temp = []
    temp_to_hum = []
    hum_to_loc = []

    i = 1
    while str_list[i] != "\n":
        seed_to_soil.append(str_list[i].split())
        # for seed in seed_to_soil:
        for seed in str_list[i].split():
            soil.add(int(seed))
        i += 1
    i += 2
    # print(seed_to_soil)
    # i = 3
    while str_list[i] != "\n":
        soil_to_fertilizer.append(str_list[i].split())
        # for seed in soil_to_fertilizer:
        for seed in str_list[i].split():
            fert.add(int(seed))
        i += 1
    i += 2
    # print(soil_to_fertilizer)
    while str_list[i] != "\n":
        fert_to_water.append(str_list[i].split())
        # for seed in fert_to_water:
        for seed in str_list[i].split():
            water.add(int(seed))
        i += 1
    i += 2
    while str_list[i] != "\n":
        water_to_light.append(str_list[i].split())
        # for seed in water_to_light:
        for seed in str_list[i].split():
            light.add(int(seed))
        i += 1
    i += 2
    while str_list[i] != "\n":
        light_to_temp.append(str_list[i].split())
        # for seed in light_to_temp:
        for seed in str_list[i].split():
            temp.add(int(seed))
        i += 1
    i += 2
    while str_list[i] != "\n":
        temp_to_hum.append(str_list[i].split())
        # for seed in temp_to_hum:
        for seed in str_list[i].split():
            hum.add(int(seed))
        i += 1
    i += 2
    try:
        while str_list[i]:
            hum_to_loc.append(str_list[i].split())
            # for seed in hum_to_loc:
            for seed in str_list[i].split():
                loc.add(int(seed))
            i += 1
    except IndexError:
        pass
    pass

    seed_list = list(seed_set)
    # print(seed_list)
    seed_set = set()
    seed_list = mins
    for i, seed in enumerate(seed_list):
        for map in seed_to_soil:
            if seed_list[i] >= int(map[1]) and seed_list[i] <= (int(map[1]) + int(map[2])):
                # print("found match")
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed seed to soil")
    
    for i, seed in enumerate(seed_list):
        for map in soil_to_fertilizer:
            if seed_list[i] >= int(map[1]) and seed_list[i] <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i] - int(map[1] + int(map[0])))
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed soil to fertilizer")
    # print("after soil to fert")
    # print(seed_list)

    for i, seed in enumerate(seed_list):
        for map in fert_to_water:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed fertilizer to water")
    # seed_list = list(seed_set)
    # seed_set = set()

    for i, seed in enumerate(seed_list):
        for map in water_to_light:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed water to light")
    # seed_list = list(seed_set)
    # seed_set = set()

    for i, seed in enumerate(seed_list):
        for map in light_to_temp:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed light to temp")
    # seed_list = list(seed_set)
    # seed_set = set()
    
    for i, seed in enumerate(seed_list):
        for map in temp_to_hum:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    seed_list = list(seed_set)
    seed_set = set()
    print("Processed temp to humidity")
    # seed_list = list(seed_set)
    # seed_set = set()

    for i, seed in enumerate(seed_list):
        for map in hum_to_loc:
            if int(seed_list[i]) >= int(map[1]) and int(seed_list[i]) <= (int(map[1]) + int(map[2])):
                # seed_set.add(seed_list[i])
                seed_list[i] = (int(seed_list[i]) - int(map[1]) + int(map[0]))
                break
    seed_set = set(seed_list)
    print("Processed humidity to location")
    print(seed_set)
    print(seed_list)
    print(min(seed_set))

    # 747113782 Too High
    # 1378139923



if __name__ == "__main__":
    # part_one()
    part_two()