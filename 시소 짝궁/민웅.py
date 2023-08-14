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