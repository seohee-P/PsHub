# 복붙 코드
import sys
from bisect import bisect_left
input = sys.stdin.readline

# target과 가장 가까운 숫자를 리턴
def findClosestNum(array, target):
    index = bisect_left(array, target)
    if index == 0:
        return array[index]
    
    if index == len(array):
        return array[-1]

    left = array[index-1]
    right = array[index]

    if target-left < right - target:
        return left
    return right


m, n, l = map(int, input().split())
hunting_pos = sorted(list(map(int, input().split())))
animals = [tuple(map(int, input().split())) for _ in range(n)]

answer = 0
# 각 동물이 사냥될 수 있는 사대의 위치를 모아본다.
for x, y in animals:
    # 현재 동물의 위치에서 가장 가까운 사대 찾기
    closestHuntingPos = findClosestNum(hunting_pos, x)

    # 사대까지의 거리가 사정거리 안에 있는지 확인해본다.
    if x - (l-y) <= closestHuntingPos <= x + (l-y):
        answer += 1
        
print(answer)