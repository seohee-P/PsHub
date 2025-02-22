# 줄번호
import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n+1):
    print("{0}. {1}".format(i, input().rstrip()))