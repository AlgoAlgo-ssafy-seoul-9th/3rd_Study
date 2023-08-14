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