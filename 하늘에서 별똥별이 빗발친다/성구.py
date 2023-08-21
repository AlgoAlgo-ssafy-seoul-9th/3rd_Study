# 14658 하늘에서 별똥별이 빗발친다
import sys

input = sys.stdin.readline

# input
N, M, L, K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]
maxV = -1
# 두개의 점을 비교
for x1, y1 in star:
    for x2, y2 in star:
        # 두 점에 대한 사각형 안에 별 개수
        stars = 0
        for x3, y3 in star:
            # 첫번째 별의 x와 두번째 별의 y을 기준으로 +L까지 범위에 포함되는 지 판단
            if x1 <= x3 <= x1 + L and y2 <= y3 <= y2 + L:
                stars += 1
        maxV = max(maxV, stars)
# 튕겨지는 별을 제외한 지구에 떨어지는 별
print(K - maxV)


"""
import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]

maxV = -1
for i in range(K):
    x, y = star[i]
    up1, up2, down1, down2 = 0, 0, 0, 0
    for j in range(K):
        target_x, target_y = star[j]
        if x - L < target_x <= x and y - L < target_y <= y:
            up1 += 1
        if x <= target_x < x + L and y - L < target_y <= y:
            up2 += 1
        if x - L < target_x <= x and y <= target_y < y + L:
            down1 += 1
        if x <= target_x < x + L and y <= target_y < y + L:
            down2 += 1

    print(up1, up2, down1, down2)
    maxV = max(maxV, up1, up2, down1, down2)
print(maxV)

import sys
input = sys.stdin.readline

# input
N, M, L, K = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(K)]

start_i, start_j = 0, 0
maxV = -1
while start_i < M and start_j < N:
    stars = 0
    for i in range(K):
        x, y = star[i]
        if start_i <= y < start_i + L and start_j <= x < start_j + L:
            stars += 1
    maxV = max(maxV, stars)
    if start_j < N - L:
        start_j += 1
    else:
        start_j = 0
        start_i += 1
print(maxV)
"""
