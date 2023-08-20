# 17615_볼모으기_gathering balls
import sys
input = sys.stdin.readline

N = int(input())

balls = list(input())
group_balls = []
temp = balls[0]
cnt = 0
b, r = 0, 0
for i in range(N):
    if balls[i] == temp:
        cnt += 1
    else:
        group_balls.append([temp, cnt])
        if temp == "B":
            b += cnt
        else:
            r += cnt
        temp = balls[i]
        cnt = 1
    if i == N-1:
        group_balls.append([temp, cnt])
        if temp == "B":
            b += cnt
        else:
            r += cnt

# print(b, r)
if group_balls[0][0] == "R":
    case1 = r - group_balls[0][1]
    case2 = b
else:
    case1 = b - group_balls[0][1]
    case2 = r

if group_balls[-1][0] == "R":
    case3 = r - group_balls[-1][1]
    case4 = b
else:
    case3 = r
    case4 = b - group_balls[-1][1]

print(min(case1, case2, case3, case4))