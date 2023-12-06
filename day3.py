
def checkNumberStatus(cosNumber:list,starsCo:list) -> (bool,tuple):

    valid = False
    gear = ""
    x_min,x_max = cosNumber[0][0]-1,cosNumber[-1][0]+1
    y_min,y_max = cosNumber[0][1]-1,cosNumber[0][1]+1

    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):

            if (x,y) in starsCo:
                gear = str(x)+","+str(y)
                valid = True

    return valid, gear

def manageNumbers(numbersCo:list,starsCo:list,lines:list,numbers:list,gears:list) -> None:

    valid,gear = checkNumberStatus(numbersCo,starsCo)

    if valid:

        numberValue = int("".join([ lines[y][x] for x,y in numbersCo ]))

        if gear:
            if not gear in gears.keys():
                gears[gear] = []
            gears[gear].append(numberValue)

        numbers.append(numberValue)

def main() -> (int,int):

    file = open("input.txt")
    lines = file.readlines()
    file.close()

    width,height = len(lines),len(lines[0])-1
    symbols = ["+","$","*","#","@","/","%","=","&","-"]
    symbolsCo = []
    starsCo = []
    numbersCo = [(0,0)]
    numbers = []
    gearsRatios = []
    gears = {}

    for y in range(width):
        for x in range(height):

            if lines[y][x] in symbols:
                symbolsCo.append((x,y))

            if lines[y][x] == "*":
                starsCo.append((x,y))

    for y in range(width):
        for x in range(height):
                
            if lines[y][x].isdigit():

                if numbersCo[-1] == (x-1,y):
                    numbersCo.append((x,y))

                else:
                    numbersCo = [(x,y)]

                if x+1 >= height:
                    manageNumbers(numbersCo,starsCo,lines,numbers,gears)

                else:
                    if not lines[y][x+1].isdigit():
                        manageNumbers(numbersCo,starsCo,lines,numbers,gears)         
    
    for v in gears.values():

        if len(v) == 2:
            gearsRatios.append(int(v[0]) * int(v[1]))

    return sum(numbers),sum(gearsRatios)

if __name__ == "__main__":
    print(main())
