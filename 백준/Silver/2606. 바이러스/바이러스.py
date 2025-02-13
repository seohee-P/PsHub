# 바이러스
from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    visited = [False] * (n + 1)
    connections = defaultdict(list)
    for _ in range(int(input())):
        s, e = map(int, input().split())
        connections[s].append(e)
        connections[e].append(s)
    queue = deque()
    queue.append(1)
    visited[1] = True
    answer = -1
    while queue:
        computer = queue.popleft()
        answer += 1
        for e in connections[computer]:
            if not visited[e]:
                visited[e] = True
                queue.append(e)
    print(answer)

if __name__ == '__main__':
    main()