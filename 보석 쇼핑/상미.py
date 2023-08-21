from collections import Counter

def solution(gems):
    answer = []
    cnt = Counter(gems)     # 보석 이름과 개수 딕셔너리
    cnt_key = []            # 보석 이름 리스트
    start, end = 0, 0       # 투포인터 지정
    min_dis = 100000        # 가장 짧은 길이
    checked = {}            # 가진 보석 확인 리스트
    for key in cnt:
        if key not in cnt_key:
            cnt_key.append(key)
            
    while end < len(gems):
        if gems[end] not in checked:    # endpoint의 보석이 없으면
            checked[gems[end]] = 1    
        else:
            checked[gems[end]] += 1 
        end += 1             

        if len(checked) == len(cnt):    # 확인된 보석 개수가 총 보석 개수랑 같으면
            while start < end:
                if checked[gems[start]] > 1:
                    checked[gems[start]] -= 1 
                    start += 1   
                elif min_dis > end - start:     # 배열에서의 길이 확인해서 작으면
                    answer = [start+1, end]
                    min_dis = end - start
                    break
                else:
                    break
                
    return answer
            
    
    
