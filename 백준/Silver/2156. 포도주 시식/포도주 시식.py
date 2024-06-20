# 포도주 시식
import sys
input = sys.stdin.readline

N = int(input())
a = [int(input()) for _ in range(N)]
dp = [0 for _ in range(N+1)]

if N >= 1:
    dp[1] = a[0]
if N >= 2:
    dp[2] = a[0] + a[1]
if N >= 3:
    dp[3] = max(dp[2], a[0]+a[2], a[1]+a[2])
if N >= 4:
    for i in range(4,N+1):
        dp[i] = max(dp[i-1], max(dp[i-2]+a[i-1], dp[i-3]+a[i-2]+a[i-1]))

print(dp[N])