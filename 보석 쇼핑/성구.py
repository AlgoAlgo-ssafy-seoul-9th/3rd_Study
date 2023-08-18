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