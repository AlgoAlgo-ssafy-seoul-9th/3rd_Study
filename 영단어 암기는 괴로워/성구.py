# 20920 영단어 암기는 괴로워
import sys
from collections import defaultdict
input = sys.stdin.readline
# Input
N, M = map(int, input().split())

# define
voca = defaultdict(int)

# dictionary setting {"voca": count}
for _ in range(N):
    word = input().strip()
    if len(word) >= M:
        voca[word] += 1

# 정렬을 위한 리스트
vocaList = []
for key, val in voca.items():
    vocaList.append((val, key))
# 음수를 활용한 부분 역정렬(우선순위: count, 길이, 사전순)
vocaList.sort(key=lambda x: (-x[0], -len(x[1]), x[1]))

# Output
for item in vocaList:
    print(item[1])
