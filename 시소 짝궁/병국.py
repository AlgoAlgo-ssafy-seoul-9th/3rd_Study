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