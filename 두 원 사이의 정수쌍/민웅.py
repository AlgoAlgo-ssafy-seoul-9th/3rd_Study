import math

def solution(r1, r2):
    ans = 0
    for i in range(0, r1):
        ans += math.floor(math.sqrt(r2**2 - i**2)) - math.floor(math.sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        ans += math.floor(math.sqrt(r2**2 - i**2))
    return 4 * ans
