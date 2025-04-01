import math


j = int(input())
n = int(input())

result = ""

if j > 1:
    if n:
        k = int(math.log(n) / math.log(j))
    else:
        k = 0
else:
    k = 1

while k >= 0:
    result = result + str(n // j**k)
    n = n - (n // j**k) * (j**k)
    k = k - 1

print(result)


def intresult(i, o):

    result = 0

    if i > 1:
        if o:
            k = int(math.log(o) / math.log(i))
        else:
            k = 0
    else:
        k = 1

    while k >= 0:
        result = result * 10
        result = result + (o // i**k)
        o = o - (o // i**k) * (i**k)
        k = k - 1

    return result

b = int(input())
c = int(input())

a = intresult(b, c)

print(a)

"""

result = 0

while k >= 0:
    result = result * 10
    result = result + (n // j**k)
    n = n - (n // j**k) * (j**k)
    k = k - 1 

"""