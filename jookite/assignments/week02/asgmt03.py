import math
import random

x = int(input())
y = int(input())

avg1 = random.randint(-4, 4)
avg2 = random.randint(-4, 4)
std1 = random.randrange(1, 5)
std2 = random.randrange(1, 5)

PI = math.pi
E = math.e

Z = ((1/(2*PI*std1**2)**0.5))*E **(-(x-avg1)/(2*std1**2)) * (1/(2*PI*std2**2)**0.5)*E**(-(y-avg2)/(2*std2**2))

print(Z)