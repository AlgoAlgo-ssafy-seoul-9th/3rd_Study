# 20920_영단어암기는괴로워_hard-english-word
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

memo = [[] for _ in range(100000)]
times = {}
for _ in range(N):
    word = input().strip()
    if len(word) < M:
        continue
    else:
        if word in times.keys():
            times[word] += 1
        else:
            times[word] = 1

for (key, value) in times.items():
    memo[value].append([key, len(key)])

for i in range(99999, 0, -1):
    # print(i)
    if memo[i]:
        memo[i].sort(key=lambda x: (-x[1], x[0]))
        for v in memo[i]:
            print(v[0])
