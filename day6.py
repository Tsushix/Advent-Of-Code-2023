
def main() -> int:

    file = open("input.txt")

    time_part_1 = file.readline().split(":")[1].split()
    distance_part_1 = file.readline().split(":")[1].split()

    time_part_2 = "".join(time_part_1)
    distance_part_2 = "".join(distance_part_1)

    file.close()

    produce_part_1 = 1
    produce_part_2 = 0

    for i in range(len(time_part_1)):

        valid_distance = []

        for t in range(int(time_part_1[i])):

            remaining_time = int(time_part_1[i]) - t
            distance_traveled = remaining_time * t

            if distance_traveled > int(distance_part_1[i]):
                valid_distance.append(distance_traveled)

        produce_part_1*=len(valid_distance)

    valid_distance = []

    for t in range(int(time_part_2)):

        remaining_time = int(time_part_2) - t
        distance_traveled = remaining_time * t

        if distance_traveled > int(distance_part_2):
            produce_part_2 += 1

    return produce_part_1,produce_part_2

if __name__ == "__main__":
    print(main())
