
def checkNumberStatus(cosNumber:list,symbols:list,lines:list) -> (bool,tuple):

    valid = False
    gear = ""
    x_min,x_max = cosNumber[0][0]-1,cosNumber[-1][0]+1
    y_min,y_max = cosNumber[0][1]-1,cosNumber[0][1]+1

    for x in range(x_min,x_max+1):
        for y in range(y_min,y_max+1):

            if x == -1:
                x = 0
            elif x >= len(lines[0])-1:
                x -= 1
            
            if y == -1:
                y = 0
            elif y >= len(lines)-1:
                y -= 1

            if (x,y) == cosNumber:
                continue

            if lines[y][x] in symbols:
                valid = True
                if lines[y][x] == "*":
                    gear = str(x)+","+str(y)
                
    return valid, gear

def manageNumbers(numbersCo:list,symbols:list,lines:list,numbers:list,gears:list) -> None:

    valid,gear = checkNumberStatus(numbersCo,symbols,lines)

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
    numbersCo = [(0,0)]
    numbers = []
    gearsRatios = []
    gears = {}

    for y in range(width):
        for x in range(height):
                
            if lines[y][x].isdigit():

                if numbersCo[-1] == (x-1,y):
                    numbersCo.append((x,y))

                else:
                    numbersCo = [(x,y)]

                if x+1 >= height:
                    manageNumbers(numbersCo,symbols,lines,numbers,gears)

                else:
                    if not lines[y][x+1].isdigit():
                        manageNumbers(numbersCo,symbols,lines,numbers,gears)         
    
    for v in gears.values():

        if len(v) == 2:
            gearsRatios.append(int(v[0]) * int(v[1]))

    return sum(numbers),sum(gearsRatios)

if __name__ == "__main__":
    print(main())
