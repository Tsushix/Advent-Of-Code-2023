
def checkValidNumber(cosNumber:list,cosSymbols:list) -> bool:

    valid = False

    for coN in cosNumber:
        for coS in cosSymbols:

            if coN[0]-1 == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]: valid = True
            elif coN[0] == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]: valid = True
            elif coN[0]+1 == coS[0]:
                if coN[1]-1 == coS[1] or coN[1] == coS[1] or coN[1]+1 == coS[1]: valid = True
    
    return valid

def main() -> int:

    file = open("input.txt")
    lines = file.readlines()
    file.close()

    width,height = len(lines),len(lines[0])-1
    symbols = ["+","$","*","#","@","/","%","=","&","-"]
    symbolsCo = []
    numbersCo = []
    numbers = []

    for y in range(width):
        for x in range(height):

            if lines[y][x] in symbols: symbolsCo.append((x,y))
            elif lines[y][x].isdigit():

                if not len(numbersCo): numbersCo.append([(x,y)])
                elif numbersCo[-1][-1] != (x-1,y): numbersCo.append([(x,y)])
                else: numbersCo[-1].append((x,y))

    for co in numbersCo:
        if checkValidNumber(co,symbolsCo):
            numbers.append(int("".join([ lines[y][x] for x,y in co ])))

    return sum(numbers)

if __name__ == "__main__":
    print(main())