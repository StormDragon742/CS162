import numpy

arry = numpy.random.randint(0,100,(5,5))

print(arry)
print(arry[1,2])

def summation(array):
    i = 0
    for size in array:
        for length in size:
            i += length
    return(i)
def mean(array):
    i = 0
    isub = []
    for row in array:
        i = 0
        for column in row:
            i += column
        i = i / 5
        isub.append(i)
    return(isub)
def max(array):
    i = 0
    while i < 5:
        store = 0
        x = 0
        while x < 5:
            if array[x, i] > store:
                store = array[x,i]
            x += 1
        i+=1
        print(store)


print(summation(arry))
print(mean(arry))
max(arry)
