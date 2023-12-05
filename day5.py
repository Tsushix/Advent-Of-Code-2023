
def createBlocs(lines:list) -> list:

    blocs = []
    blocsLen = 0

    for line in lines:

        if blocsLen == len(blocs):
            blocs.append([])

        if line == "\n":
            blocsLen += 1

        elif line[-2] != ":":
            blocs[-1].append(line)
    
    return blocs

def main() -> (int, int):

    file = open("input.txt")
    lines = file.readlines()

    blocs = createBlocs(lines)
    seeds = blocs[0][0].split(":")[1].split()
    seeds = [int(s.strip()) for s in seeds]

    """

    seedsPart2 = []

    for i in range(len(seeds)):
    
        if not len(seedsPart2):
            seedsPart2.append(seeds[i])

        elif i%2!=0:
            seedsLastValue = seedsPart2[-1]

            for j in range(1,seeds[i]):
                seedsPart2.append(seedsLastValue+j)

        else:
            seedsPart2.append(seeds[i])
    
    """

    for bloc in blocs[1:]:

        sourceToDestination = []

        for rangeSeeds in bloc:

            rangeSeeds = [int(r) for r in rangeSeeds.strip().split()]
            sourceToDestination.append(rangeSeeds)
        
        for seed in seeds:
            for destination,source,rangeSeeds in sourceToDestination:

                if source <= seed < source+rangeSeeds:

                    seeds.insert(seeds.index(seed),destination+seed-source)
                    seeds.remove(seed)

        """

        for seed in seedsPart2:
            for destination,source,rangeSeeds in sourceToDestination:

                if source <= seed < source+rangeSeeds:

                    seedsPart2.insert(seedsPart2.index(seed),destination+seed-source)
                    seedsPart2.remove(seed)

        """

    file.close()

    return min(seeds)#,min(seedsPart2)

if __name__ == "__main__":
    print(main())
