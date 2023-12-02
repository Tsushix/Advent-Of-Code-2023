
def main() -> tuple:

    file = open("input.txt")
    ids = []
    gamePower = []

    for line in file.readlines():

        id = int(line.split(":")[0].split()[1])
        sets = line.split(":")[1].split(";")
        max = {"red":0,"green":0,"blue":0}
        toAdd = True

        for set in sets:
            
            datas = set.split(",")

            for data in datas:

                count = int(data.strip().split()[0])

                if "blue" in data:
                    if count > max["blue"]: max["blue"] = count
                    if count > 14: toAdd = False
                elif "green" in data:
                    if count > max["green"]: max["green"] = count
                    if count > 13: toAdd = False
                elif "red" in data:
                    if count > max["red"]: max["red"] = count
                    if count > 12: toAdd = False

        file.close()

        gamePower.append(max["red"]*max["green"]*max["blue"])

        if toAdd:
            ids.append(id)

        return sum(ids),sum(gamePower)

if __name__ == "main":
    print(main())
