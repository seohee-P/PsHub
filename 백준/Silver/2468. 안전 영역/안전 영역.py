# 안전 영역
from collections import deque
import sys
input = sys.stdin.readline

def main():
    global n, area
    n = int(input())
    area = [list(map(int, input().split())) for _ in range(n)]
    max_height = 0
    for a in area:
        max_height = max(max_height, max(a))

    answer = 0
    for i in range(max_height):
        answer = max(bfs(i), answer)

    print(answer)

def bfs(height):
    visited = [[False] * n for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] <= height or visited[i][j]:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            count += 1
            while queue:
                y, x = queue.popleft()
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if ny < 0 or ny >= n or nx < 0 or nx >= n:
                        continue
                    if visited[ny][nx]:
                        continue
                    if area[ny][nx] > height:
                        queue.append((ny, nx))
                        visited[ny][nx] = True

    return count

if __name__ == '__main__':
    main()