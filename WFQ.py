file = open("input queue.txt", "r")
#print(file.read())
pArray = []
sArray = []
eArray = []
lines = 0
for x in file:
    i = x.split(" ")
    if i[0] == "P":
        pArray.append(i[1].strip())
    elif i[0] == "S":
        sArray.append(i[1].strip())
    else:
        eArray.append(i[1].strip())
    lines += 1

#print(pArray,sArray,eArray)

for i in range(lines):
    for x in range(3):
        if len(pArray) != 0:
            print(pArray[0])
            pArray.pop(0)
        else:
            pass
    for x in range(2):
        if len(sArray) != 0:
            print(sArray[0])
            sArray.pop(0)
        else:
            pass
    if len(eArray) != 0:
        print(eArray[0])
        eArray.pop(0)
file.close()

