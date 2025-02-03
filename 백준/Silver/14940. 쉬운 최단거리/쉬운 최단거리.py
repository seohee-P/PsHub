# 쉬운 최단거리
import sys
from collections import deque
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    queue = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if a[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = 1
                a[i][j] = 0

    while queue:
        y, x = queue.popleft()
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < m:
                if visited[ny][nx] == 1:
                    continue
                if a[ny][nx] == 0:
                    visited[ny][nx] = 1
                    continue
                visited[ny][nx] = 1
                a[ny][nx] = a[y][x] + 1
                queue.append((ny, nx))

    for i in range(n):
        for j in range(m):
            if visited[i][j] == 0 and a[i][j] == 1:
                a[i][j] = -1

    for row in a:
        print(*row)


if __name__ == '__main__':
    main()