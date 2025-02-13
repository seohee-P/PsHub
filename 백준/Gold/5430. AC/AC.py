# AC
from collections import deque
import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        command = input()
        n = int(input())
        if n == 0:
            nums = input()
            nums = deque()
        else:
            nums = input()[1:-2]
            nums = deque(nums.split(','))
        reverse_count = 0
        is_error = False
        for c in command:
            if c == 'R':
                reverse_count += 1
                continue
            if c == 'D':
                if not nums:
                    is_error = True
                    break
                if reverse_count % 2 == 0:
                    nums.popleft()
                else:
                    nums.pop()
        if is_error:
            print("error")
        else:
            if reverse_count % 2 == 0:
                print("[{0}]".format(','.join(nums)))
            else:
                nums = reversed(nums)
                print("[{0}]".format(','.join(nums)))


if __name__ == '__main__':
    main()