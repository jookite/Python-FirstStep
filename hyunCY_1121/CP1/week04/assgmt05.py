n = int(input())
d = int(input())

result = ''

if d == 0:
    result = '0'

while d > 0:
    result = str(d % n) + result
    d //= n


print(result)
