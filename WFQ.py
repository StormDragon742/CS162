def fillArrays(text):
    file = open(text, "r")
    pArray = []
    sArray = []
    eArray = []
    for x in file:
        i = x.split(" ")
        if i[0] == "P":
            pArray.append(i[1].strip())
        elif i[0] == "S":
            sArray.append(i[1].strip())
        else:
            eArray.append(i[1].strip())
    qArray = [pArray, sArray, eArray]
    file.close()
    return (qArray)


def printQueue(text):
    queue = fillArrays(text)
    while len(queue[2]) != 0:
        for x in range(3):
            if len(queue[0]) != 0:
                print(queue[0][0])
                queue[0].pop(0)
            else:
                pass
        for x in range(2):
            if len(queue[1]) != 0:
                print(queue[1][0])
                queue[1].pop(0)
            else:
                pass
        if len(queue[2]) != 0:
            print(queue[2][0])
            queue[2].pop(0)


def main():
    printQueue("input queue.txt")


main()
