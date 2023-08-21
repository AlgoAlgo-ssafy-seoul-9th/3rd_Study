# 17615 볼 모으기
import sys
input = sys.stdin.readline

# input
N = int(input())
arr = input().strip()

# define
cnt = [0] * 4

# right Red
rr = arr.rstrip("R")
cnt[0] = rr.count("R")

# left Red
lr = arr.lstrip("R")
cnt[1] = lr.count("R")

# right Blue
rb = arr.rstrip("B")
cnt[2] = rb.count("B")

# left Blue
lb = arr.lstrip("B")
cnt[3] = lb.count("B")

print(min(cnt))


"""
import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
arr = input().strip()

cnt = [0] * 4
# BLUE
# left
i = 0
blue, red = 0, 0
while i < N:
    if arr[i] == "B":
        blue += 1
    else:
        red += 1
    if red and arr[i] == "B":
        cnt[0] += 1
    i += 1
# right
j = N - 1
blue, red = 0, 0
while j > -1:
    if arr[j] == "B":
        blue += 1
    else:
        red += 1
    if red and arr[j] == "B":
        cnt[1] += 1
    j -= 1

# RED
# left
i = 0
blue, red = 0, 0
while i < N:
    if arr[i] == "B":
        blue += 1
    else:
        red += 1
    if blue and arr[i] == "R":
        cnt[2] += 1
    i += 1
# right
j = N - 1
blue, red = 0, 0
while j > -1:
    if arr[j] == "B":
        blue += 1
    else:
        red += 1
    if blue and arr[j] == "R":
        cnt[3] += 1
    j -= 1
print(min(cnt))
"""
