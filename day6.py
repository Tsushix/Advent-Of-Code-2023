
from math import sqrt, ceil, floor

def main() -> (int,int):

    file = open("input.txt")

    time_part_1 = file.readline().split(":")[1].split()
    distance_part_1 = file.readline().split(":")[1].split()
    produce_part_1 = 1

    time_part_2 = "".join(time_part_1)
    distance_part_2 = "".join(distance_part_1)

    file.close()

    for i in range(len(time_part_1)):

        time,distance = time_part_1[i],distance_part_1[i]

        x1 = ceil((int(time) - sqrt(int(time) **2 - 4 * int(distance)))/2)
        x2 = floor((int(time) + sqrt(int(time)**2 - 4 * int(distance)))/2)

        if (int(time) - x1) * x1 == float(distance):
            x1 += 1

        if (int(time) - x2) * x2 == float(distance):
            x2 -= 1
                
        produce_part_1 *= x2-x1+1


    x1 = ceil((int(time_part_2) - sqrt(int(time_part_2) ** 2 - 4 * int(distance_part_2)))/2)
    x2 = floor((int(time_part_2) + sqrt(int(time_part_2) ** 2 - 4 * int(distance_part_2)))/2)

    if (int(time_part_2) - x1) * x1 == float(distance_part_2):
        x1 += 1
            
    if (int(time_part_2) - x2) * x2 == float(distance_part_2):
        x2 -= 1

    produce_part_2 = x2-x1+1

    return produce_part_1,produce_part_2

if __name__ == "__main__":
    print(main())