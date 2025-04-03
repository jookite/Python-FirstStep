N=int(input())
D=int(input())

result = ""

if D == 0:
    result = "0"
else:
    while D > 0:
        if D%N ==0:
            result = "0" + result
        else:
            result = str(D%N) + result

        D = D//N
print(result)
