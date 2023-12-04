
def checkString(line:str,c:int) -> str:

    value = ""

    if line[c:c+3] == "one": value = "1"
    elif line[c:c+3] == "two": value = "2"
    elif line[c:c+5] == "three": value = "3"
    elif line[c:c+4] == "four": value = "4"
    elif line[c:c+4] == "five": value = "5"
    elif line[c:c+3] == "six": value = "6"
    elif line[c:c+5] == "seven": value = "7"
    elif line[c:c+5] == "eight": value = "8"
    elif line[c:c+4] == "nine": value = "9"

    return value

def main() -> int:

    file = open("input.txt")
    numbers = []

    for line in file.readlines():

        firstValue = ""
        lastValue = ""

        for c in range(len(line)):

            if line[c].isdigit():
                if not firstValue: firstValue = line[c]
                lastValue = line[c]
            
            elif checkString(line,c):
                if not firstValue: firstValue = checkString(line,c)
                lastValue = checkString(line,c)
        
        numbers.append(int(firstValue+lastValue))

    file.close()
        
    return sum(numbers)

if __name__ == "__main__":
    print(main())

