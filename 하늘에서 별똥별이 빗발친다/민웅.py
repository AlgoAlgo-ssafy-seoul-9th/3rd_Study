# 14658_하늘에서별똥별이빗발친다_shooting star
import sys
input = sys.stdin.readline

N, M, L, K = map(int, input().split())

stars = []
for _ in range(K):
    x, y = map(int, input().split())
    stars.append([y-1, x-1])

ans = 0

for i in range(K):
    for j in range(K):
        count = 0
        for star in stars:
            if stars[i][0] <= star[0] <= stars[i][0] + L and stars[j][1] <= star[1] <= stars[j][1] + L:
                count += 1
        ans = max(ans, count)
print(K - ans)
