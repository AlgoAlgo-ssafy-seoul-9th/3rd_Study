# 2512 예산
import sys

input = sys.stdin.readline

# input
N = int(input())
request = list(map(int, input().split()))
total = int(input())

# define
maxBudget = max(request)

if sum(request) <= total:
    print(maxBudget)
else:
    for i in range(total//N, maxBudget):
        tmp = [0] * N
        for j in range(N):
            if i < request[j]:
                tmp[j] = i
            else:
                tmp[j] = request[j]

        if sum(tmp) <= total:
            print(i)
            break