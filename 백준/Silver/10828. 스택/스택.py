# 스택
from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    stack = deque()
    for _ in range(n):
        command = input().rstrip().split()
        if command[0] == "push":
            stack.append(int(command[1]))
        elif command[0] == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command[0] == "size":
            print(len(stack))
        elif command[0] == "empty":
            print(0) if stack else print(1)
        elif command[0] == "top":
            if not stack:
                print(-1)
            else:
                print(stack[-1])

if __name__ == '__main__':
    main()