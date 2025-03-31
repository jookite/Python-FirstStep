import math

j = int(input())
n = int(input())

result=""

if j > 1:
    if n == 0:
        k = 0
    else:
        k = int(math.log(n)/math.log(j))
else:
    k = 1
while k >= 0:
    result = result + str(n//j**k)
    n = n - (n//j**k)*(j**k)
    k = k - 1
print(result)
