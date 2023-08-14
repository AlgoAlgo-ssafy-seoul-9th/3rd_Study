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