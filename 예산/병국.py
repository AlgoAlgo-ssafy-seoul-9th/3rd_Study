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