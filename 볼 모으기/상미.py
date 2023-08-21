N = int(input())
budget = list(map(int, input().split()))
M = int(input())
start, end = 0, max(budget) 

# 브루트포스 하려다가 
# def sum_budget(budget):
#     for b in budget:
#         if b > highest:
#             b = highest
#     return sum(budget)

# while True:
#     if sum_budget(budget) < M:         # 총 예산보다 배정 예산이 적으면
#         highest += 1
#     else:
#         answer = highest - 1
#         break

# 이분 탐색으로
while start <= end:
    mid = (start + end) // 2
    sum_budget = 0
    for b in budget:
        if b > mid:
            sum_budget += mid
        else:
            sum_budget += b
    if sum_budget <= M: 
        start = mid + 1
    else: 
        end = mid - 1
print(end)

