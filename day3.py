
def checkNumberStatus(cosNumber:list,cosSymbols:list,lines:list) -> (bool,tuple):

    valid = False
    gear = ""

    for coS in cosSymbols:

        for coN in cosNumber:

            if coN[0]-1 == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]: 
                    if lines[coS[1]][coS[0]] == "*": gear = str(coS[0])+","+str(coS[1])
                    valid = True
            elif coN[0] == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]:
                    if lines[coS[1]][coS[0]] == "*": gear = str(coS[0])+","+str(coS[1])
                    valid = True
            elif coN[0]+1 == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]:
                    if lines[coS[1]][coS[0]] == "*": gear = str(coS[0])+","+str(coS[1])
                    valid = True

    return valid, gear

def main() -> (int,int):

    file = open("input.txt")
    lines = file.readlines()
    file.close()

    width,height = len(lines),len(lines[0])-1
    symbols = ["+","$","*","#","@","/","%","=","&","-"]
    symbolsCo = []
    numbersCo = []
    numbers = []
    gearsRatios = []
    gears = {}

    for y in range(width):
        for x in range(height):

            if lines[y][x] in symbols: symbolsCo.append((x,y))
            elif lines[y][x].isdigit():

                if not len(numbersCo): numbersCo.append([(x,y)])
                elif numbersCo[-1][-1] != (x-1,y): numbersCo.append([(x,y)])
                else: numbersCo[-1].append((x,y))

    for co in numbersCo:

        valid,gear = checkNumberStatus(co,symbolsCo,lines)

        if valid:

            numberValue = int("".join([ lines[y][x] for x,y in co ]))

            if gear:
                if not gear in gears.keys(): gears[gear] = []
                gears[gear].append(numberValue)

            numbers.append(numberValue)
    
    for v in gears.values():

        if len(v) == 2:
            gearsRatios.append(int(v[0]) * int(v[1]))

    return sum(numbers),sum(gearsRatios)

if __name__ == "__main__":
    print(main())
