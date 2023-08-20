# 2512_예산_assets
import sys
input = sys.stdin.readline

N = int(input())

assets = list(map(int, input().split()))
M = int(input())

assets.sort()
# s = assets[0]
s = 0
e = assets[N-1]
if sum(assets) <= M:
    e = max(assets)
else:
    while True:
        mid = (s+e)//2
        temp = 0
        for i in range(N):
            if assets[i] <= mid:
                temp += assets[i]
            else:
                temp += mid
        # 여기 temp < M: 으로 하면 1 1 3 7  11 안걸러짐
        if temp <= M:
            s = mid+1
        else:
            e = mid-1

        if s > e:
            break

print(e)