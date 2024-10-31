# 미로 탐색
from collections import deque

def main():
    N, M = map(int, input().split())
    maze = [list(input()) for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0] = 1
    answer = 0
    while queue:
        x, y, count = queue.popleft()
        answer = max(count, answer)
        if x == N - 1 and y == M - 1:
            break
        for (dx, dy) in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                if visited[nx][ny] == 1:
                    continue
                if maze[nx][ny] == '1':
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count + 1))
    print(answer)


if __name__ == '__main__':
    main()