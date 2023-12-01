
file = open("input.txt")

numbers = []
numberString = ["one","two","three","four","five","six","seven","height","nine"]

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

for line in file.readlines():

    firstValue = ""
    lastValue = ""

    for c in range(len(line)):

        if line[c].isdigit():
            firstValue = line[c]
        
        else:
            firstValue = checkString(line,c)


        if firstValue: break
    
    for c in range(len(line)-1,-1,-1):

        if line[c].isdigit():
            lastValue = line[c]
        
        else:
            lastValue = checkString(line,c,-1)

        if lastValue: break
    
    numbers.append(int(firstValue+lastValue))

print(sum(numbers))