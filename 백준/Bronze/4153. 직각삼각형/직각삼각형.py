# 직각삼각형
import sys
input = sys.stdin.readline

while True:
    side = list(map(int, input().split()))
    if sum(side) == 0:
        break
    side.sort()
    if side[0]**2 + side[1]**2 == side[2]**2:
        print("right")
    else:
        print("wrong")
