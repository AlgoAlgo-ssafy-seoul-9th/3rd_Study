# 2nd_study

[2주차] 코딩테스트 준비 2주차
<br/>

[프로그래머스 두 원 사이의 정수](https://school.programmers.co.kr/learn/courses/30/lessons/152996)
[프로그래머스 시소 짝궁](https://school.programmers.co.kr/learn/challenges?order=recent)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16423)

<br/><br/>

# [프로그래머스] 두 원 사이의 정수쌍

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./두%20원%20사이의%20정수쌍/성구.py)

```py

```

## [민웅](./두%20원%20사이의%20정수쌍/민웅.py)

```py
import math

def solution(r1, r2):
    ans = 0
    for i in range(0, r1):
        ans += math.floor(math.sqrt(r2**2 - i**2)) - math.floor(math.sqrt(r1**2 - i**2 - 1))
    for i in range(r1, r2):
        ans += math.floor(math.sqrt(r2**2 - i**2))
    return 4 * ans

```

## [병국](./두%20원%20사이의%20정수쌍/병국.py)

```py

```

## [상미](./두%20원%20사이의%20정수쌍/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [프로그래머스] 시소 짝궁

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./시소%20짝궁/성구.py)

```py

```

## [민웅](./시소%20짝궁/민웅.py)

```py
def solution(weights):
    answer = 0
    num = {}
    weights.sort(reverse=True)
    for v in weights:
        if v in num.keys():
            answer += num[v]
            num[v] += 1
        else:
            num[v] = 1
        if v*3/2 in num.keys():
            answer += num[v*3/2]
        if v*4/3 in num.keys():
            answer += num[v*4/3]
        if v*2 in num.keys():
            answer += num[v*2]

    return answer
```

## [병국](./시소%20짝궁/병국.py)

```py
def solution(weights):
    answer = 0
    N = len(weights)
    weights.sort()
    dict = {}
    for i in weights:
        if i in dict:
            answer += dict[i]
            dict[i]+=1
        else:
            dict[i] = 1
        if (i/(3/2)) in dict:
            answer += dict[(i/(3/2))]
        if (i/(4/3)) in dict:
            answer += dict[(i/(4/3))]
        if (i/2) in dict:
            answer += dict[(i/2)]

    return answer
```

## [상미](./시소%20짝궁/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 영단어 암기는 괴로워

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./영단어%20암기는%20괴로워/성구.py)

```py
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


```

## [민웅](./영단어%20암기는%20괴로워/민웅.py)

```py
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
```

## [병국](./영단어%20암기는%20괴로워/병국.py)

```py
n,m = map(int,input().split())
dic = {}
for _ in range(n):
    eng = input()
    if len(eng) < m:
        continue
    if eng in dic:
        dic[eng] += 1
    else:
        dic[eng] = 1
sordic = (sorted(dic.items(),key=lambda x:(-x[1],-len(x[0]),x[0])))
for i in (list(sordic)):
    print(i[0])

```

## [상미](./영단어%20암기는%20괴로워/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 1,2,3 더하기4

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./1,2,3%20더하기4%20/성구.py)

```py

```

## [민웅](./1,2,3%20더하기4%20/민웅.py)

```py
# 15989_1,2,3 더하기 4_plus-four
import sys
input = sys.stdin.readline

N = int(input())

dp = [1 for _ in range(10001)]
dp[1] = 1
dp[2] = 2

for i in range(3, 10001):
    dp[i] += dp[i-2]

for i in range(3, 10001):
    dp[i] += dp[i-3]


for _ in range(N):
    print(dp[int(input())])

# # 15989_1,2,3 더하기 4_plus-four
# import sys
# input = sys.stdin.readline

# N = int(input())

# dp = [1 for _ in range(10001)]
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3

# for i in range(4, 10001):
#     dp[i] += dp[i-2]

# for i in range(4, 10001):
#     dp[i] += dp[i-3]


# for _ in range(N):
#     print(dp[int(input())])
```

## [병국](./1,2,3%20더하기4%20/병국.py)

```py
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr_max = max(arr)
dp = [1]*(arr_max+1)

for i in range(2, arr_max+1):
    dp[i] += dp[i - 2]

for i in range(3, arr_max+1):
    dp[i] += dp[i - 3]

# 2의배수*1이면 1개 2*2면 2개
# 3의배수*1이면 1개 3*2면 2개
for i in arr:
    print(dp[i])

```

## [상미](./1,2,3%20더하기4%20/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 파티

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./파티/성구.py)

```py

```

## [민웅](./파티/민웅.py)

```py
# 1238_파티_party
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

adjL = [[] for _ in range(N+1)]
adjL2 = [[] for _ in range(N+1)]
visited = [0]*(N+1)
visited2 = [0]*(N+1)
for _ in range(M):
    s, g, t = map(int, input().split())
    adjL[g].append([s, t])
    adjL2[s].append([g, t])

stack = [[X, 0]]
stack2 = [[X, 0]]
visited[X] = 1
visited2[X] = 1
ans = 0
while stack:
    node, dis = stack.pop()

    for v in adjL[node]:
        if visited[v[0]] == 0 or visited[v[0]] > dis+v[1]:
            stack.append([v[0], dis + v[1]])
            visited[v[0]] = dis + v[1]

while stack2:
    node, dis = stack2.pop()

    for v in adjL2[node]:
        if visited2[v[0]] == 0 or visited2[v[0]] > dis+v[1]:
            stack2.append([v[0], dis + v[1]])
            visited2[v[0]] = dis + v[1]

for i in range(1, N+1):
    if (visited[i] + visited2[i]) > ans:
        ans = (visited[i] + visited2[i])
print(ans)

```

## [병국](./파티/병국.py)

```py
import heapq


def dijk(start):
    q = []
    heapq.heappush(q,(0,start))
    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist: # 갱신해줄필요없다 ( 거리가 더 짧다 ) 그럼 패스
            continue
        #거리가 크다면
        for now1, dist1 in graph[now]: # 연결된거 다 탐색하자,,
            if dist+dist1 < distance[now1]: # 갱신해주자
                distance[now1] = dist+dist1 # 갱신해주면 뭐해야되지,,
                heapq.heappush(q, (dist+dist1, now1))



n,m,x = map(int,input().split())
INF = float('inf')
graph = [[] for _ in range(n+1)]
visited = [False] *(n+1)
for _ in range(m):
    start, end, time = map(int,input().split())
    graph[start].append((end,time))
# print(graph)

answer = [[0]*(n+1)]
for i in range(1,n+1):
    distance = [INF]*(n+1)
    dijk(i)
    answer.append(distance)
# print(answer)
maxx = 0
for i in range(1,n+1):
    if i == x:
        continue
    if maxx < answer[i][x]+answer[x][i]:
        maxx =answer[i][x]+answer[x][i]
print(maxx)

```

## [상미](./파티/상미.py)

```py

```

</div>
</details>
