import sys
input = sys.stdin.readline

K, N = map(int, input().split())
kList = [int(input()) for _ in range(K)]

left, right = 1, max(kList)

while left <= right:
    mid = (left + right) // 2
    count = 0
    for k in kList:
        count += k // mid
    if count < N:
        right = mid - 1
    else:
        left = mid + 1

print((left+right)//2)