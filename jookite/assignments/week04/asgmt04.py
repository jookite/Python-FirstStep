n = int(input())

result = ""

if n == 0:
    print("0")

while n!=0:
    if n%2 == 0:
        result = "0" + result
    else:
        result = "1" + result
    n >>= 1

print(result)