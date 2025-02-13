# 좌표 압축
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    set_nums = sorted(list(set(nums)))
    idx = dict()
    for i in range(len(set_nums)):
        idx[set_nums[i]] = i
    for n in nums:
        print(idx[n], end=' ')

if __name__ == "__main__":
    main()