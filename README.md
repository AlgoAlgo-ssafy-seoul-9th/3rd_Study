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

```

## [병국](./예산/병국.py)

```py

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

```

## [병국](./볼%20모으기/병국.py)

```py

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

```

## [병국](./하늘에서%20별똥별이%20빗발친다/병국.py)

```py

```

## [상미](./하늘에서%20별똥별이%20빗발친다/상미.py)

```py

```

</div>
</details>
