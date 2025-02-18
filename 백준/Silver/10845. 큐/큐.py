# 큐
from collections import deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    queue = deque()
    for _ in range(n):
        command = input().rstrip().split()
        if command[0] == "push":
            queue.append(command[1])
            continue
        if command[0] == "pop":
            if queue:
                print(queue.popleft())
            else:
                print(-1)
            continue
        if command[0] == "size":
            print(len(queue))
            continue
        if command[0] == "empty":
            print(1) if not queue else print(0)
            continue
        if command[0] == "front":
            if queue:
                print(queue[0])
            else:
                print(-1)
            continue
        if command[0] == "back":
            if queue:
                print(queue[-1])
            else:
                print(-1)


if __name__ == "__main__":
    main()