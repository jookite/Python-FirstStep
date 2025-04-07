n = int(input())

F1 = F2 = F3 = 1

for i in range(3, n+1):
    F3 = F1 + F2
    F1 = F2
    F2 = F3
print(F3)
