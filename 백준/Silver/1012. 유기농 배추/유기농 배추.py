# 유기농 배추
from collections import deque
import sys
input = sys.stdin.readline

def main():
    T = int(input())
    for _ in range(T):
        M, N, K = map(int, input().split())
        field = [[0 for _ in range(M)] for _ in range(N)]
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for _ in range(K):
            x, y = map(int, input().split())
            field[y][x] = 1

        worm = 0
        queue = deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        for i in range(N):
            for j in range(M):
                if field[i][j] == 0:
                    continue
                if visited[i][j] == 1:
                    continue
                worm += 1
                visited[i][j] = 1
                queue.append((i, j))
                while queue:
                    y, x = queue.popleft()
                    for dy, dx in dirs:
                        ny, nx = y + dy, x + dx
                        if (0 <= nx < M and 0 <= ny < N) and visited[ny][nx] == 0:
                            if field[ny][nx] == 1:
                                visited[ny][nx] = 1
                                queue.append((ny, nx))
                                
        print(worm)


if __name__ == '__main__':
    main()