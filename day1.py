
def checkString(line:str,c:int,pas=1) -> str:

    value = ""

    if line[c:c+3*pas:pas] == "one"[::pas]: value = "1"
    elif line[c:c+3*pas:pas] == "two"[::pas]: value = "2"
    elif line[c:c+5*pas:pas] == "three"[::pas]: value = "3"
    elif line[c:c+4*pas:pas] == "four"[::pas]: value = "4"
    elif line[c:c+4*pas:pas] == "five"[::pas]: value = "5"
    elif line[c:c+3*pas:pas] == "six"[::pas]: value = "6"
    elif line[c:c+5*pas:pas] == "seven"[::pas]: value = "7"
    elif line[c:c+5*pas:pas] == "eight"[::pas]: value = "8"
    elif line[c:c+4*pas:pas] == "nine"[::pas]: value = "9"

    return value

def main() -> None:

    file = open("input.txt")
    numbers = []

    for line in file.readlines():

        firstValue = ""
        lastValue = ""

        for c in range(len(line)):

            print(lastValue)

            if line[c].isdigit():
                if not firstValue: firstValue = line[c]
                lastValue = line[c]
            
            elif checkString(line,c):
                if not firstValue: firstValue = checkString(line,c)
                lastValue = checkString(line,c)
        
        numbers.append(int(firstValue+lastValue))
        
        return numbers

if __name__ == "main":
    print(main())

