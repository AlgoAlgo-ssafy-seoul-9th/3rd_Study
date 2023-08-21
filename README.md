# 2nd_study

[2주차] 코딩테스트 준비 2주차
<br/>

[프로그래머스 보석 쇼핑](https://school.programmers.co.kr/learn/courses/30/lessons/67258)

[백준 문제집 바로가기](https://www.acmicpc.net/workbook/view/16517)

<br/><br/>

# [프로그래머스] 보석 쇼핑

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./보석%20쇼핑/성구.py)

```py
# 보석 쇼핑

from collections import defaultdict

def solution(gems):
    # define
    #  길이 미리 측정
    len_gem = len(gems)
    # 종류 만들기
    gems_type = set(gems)
    gem_dic = defaultdict(int)
    # 최대치 (최소를 구하기 위해)
    minLen = 100001
    i, j = 0, 0

    while j < len_gem:
        gem_dic[gems[j]] += 1
        if len(gem_dic.keys()) == len(gems_type):
            while len(gem_dic.keys()) == len(gems_type):
                gem_dic[gems[i]] -= 1
                if gem_dic[gems[i]] == 0:
                    print(i,j)
                    gem_dic.pop(gems[i])
                    if minLen > (j - i + 1):
                        answer = [i+1 , j+1]
                        minLen = j - i + 1


                i += 1
        j += 1
    return answer
```

## [민웅](./보석%20쇼핑/민웅.py)

```py
def solution(gems):
    answer = []

    L = len(gems)

    i, j = 0, 0
    g_dict = {}
    num = 0
    for k in range(L):
        if gems[k] in g_dict.keys():
            continue
        else:
            g_dict[gems[k]] = 0
            num += 1
    check = 0
    ans = float('inf')
    while i <= j and i != L:
        if check != num and j != L:
            if g_dict[gems[j]] == 0:
                g_dict[gems[j]] += 1
                check += 1
                j += 1
            else:
                g_dict[gems[j]] += 1
                j += 1
        else:
            if check == num:
                if (j - i) < ans:
                    answer = [i+1, j]
                    ans = (j-i)
                g_dict[gems[i]] -= 1
                if g_dict[gems[i]] == 0:
                    check -= 1
                    i += 1
                else:
                    i += 1
            else:
                i += 1
    return answer
```

## [병국](./보석%20쇼핑/병국.py)

```py

```

## [상미](./보석%20쇼핑/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 예산

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./예산/성구.py)

```py

```

## [민웅](./예산/민웅.py)

```py
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
```

## [병국](./예산/병국.py)

```py
# 이분탐색
# mid 구하는과정,,
# arr 돌면서 mid보다 큰거는 mid 더하고 아니면 그냥 원래값 더하고
# total 보면서 더 크면 end-1 아니면 start+1

def binary(arr):
    start, end = 0, max(arr)
    while start<=end:
        mid = (start+end)//2
        sum = 0
        for i in arr:
            if i < mid:
                sum += i
            else:
                sum += mid
        if sum > m:
            end = mid-1
        else:
            start = mid+1
    return end



n = int(input())
arr = list(map(int,input().split()))
m = int(input())
arr.sort()
print(binary(arr))
```

## [상미](./예산/상미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 볼 모으기

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./볼%20모으기/성구.py)

```py

```

## [민웅](./볼%20모으기/민웅.py)

```py
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
```

## [병국](./볼%20모으기/병국.py)

```py
n = int(input())
m = list(input())
# 레드, 블루 선택
# 왼쪽, 오른쪽으로 보낼지 선택
# 총 4가지 중 최소 구하기

#  레드 선택했을 때 먼저 오른쪽으로옮기자
cnt = 0
red = 0
blue = 0
answer = []
# 예시는 RRBRRB


# 오른쪽으로 옮기기 R, B 순으로
for i in range(n):
    if m[i] == 'R':   # R 나오면 red +1 해준다
        red += 1
    if m[i] == 'B' and red: # B가 나왔을 때, 근데 이미 레드가 나왔을때
        cnt += red # 이때까지 센 레드 다 더해줘,, 오른쪽으로 옮겨야하니까,,
        red = 0 # 레드 초기화,, 계속 진행. 그럼 4가 나오겠군0,,
answer.append(cnt)
cnt = 0
for i in range(n):
    if m[i] == 'B':
        blue += 1
    if m[i] == 'R' and blue:
        cnt += blue
        blue = 0
answer.append(cnt)

# 이제 왼쪽으로 옮기는거

cnt = 0
for i in range(n-1,-1,-1):
    if m[i] == 'R':   # R 나오면 red +1 해준다
        red += 1
    if m[i] == 'B' and red: # B가 나왔을 때, 근데 이미 레드가 나왔을때
        cnt += red # 이때까지 센 레드 다 더해줘,, 오른쪽으로 옮겨야하니까,,
        red = 0 # 레드 초기화,, 계속 진행. 그럼 4가 나오겠군0,,
answer.append(cnt)
cnt = 0
for i in range(n-1,-1,-1):
    if m[i] == 'B':
        blue += 1
    if m[i] == 'R' and blue:
        cnt += blue
        blue = 0
answer.append(cnt)

print(min(answer))


```

## [상미](./볼%20모으기/상미미.py)

```py

```

</div>
</details>

<br/><br/><br/>

# [백준] 하늘에서 별똥별이 빗발친다

<details>
<summary>접기/펼치기</summary>
<div markdown="1">

## [성구](./하늘에서%20별똥별이%20빗발친다/성구.py)

```py

```

## [민웅](./하늘에서%20별똥별이%20빗발친다/민웅.py)

```py
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
```

## [병국](./하늘에서%20별똥별이%20빗발친다/병국.py)

```py

```

## [상미](./하늘에서%20별똥별이%20빗발친다/상미.py)

```py

```

</div>
</details>
