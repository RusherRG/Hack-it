import math


def calc(c, x, sum):
    while(c > 0):
        sum += c % x
        c = c // x
        sum = calc(c, x, sum)
        return sum
    return sum


c, x = map(int, input().split())
sum = 0
sum = c % x
c = c // x
sum = calc(c, x, sum)
print(sum)
