# 연구소
from collections import deque
import copy
def main():
    N, M = map(int, input().split())
    Map = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    for i in range(N * M):
        for j in range(i + 1, N * M):
            for k in range(j + 1, N * M):
                copy_Map = copy.deepcopy(Map)
                answer = max(answer, bfs(i, j, k, copy_Map, M, N))
    print(answer)


def bfs(i, j, k, Map, M, N):
    first_y, first_x = i // M, i % M
    second_y, second_x = j // M, j % M
    third_y, third_x = k // M, k % M

    if Map[first_y][first_x] != 0 or Map[second_y][second_x] != 0 or Map[third_y][third_x] != 0:
        return 0

    Map[first_y][first_x] = 1
    Map[second_y][second_x] = 1
    Map[third_y][third_x] = 1

    answer = 0

    visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                continue
            if Map[i][j] == 1 or Map[i][j] == 0:
                continue
            queue = deque([(i, j)])
            visited[i][j] = True
            while queue:
                y, x = queue.popleft()
                for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ny, nx = y + dy, x + dx
                    if 0 > ny or ny >= N or nx < 0 or nx >= M:
                        continue
                    if Map[ny][nx] == 1 or visited[ny][nx]:
                        continue
                    queue.append((ny, nx))
                    Map[ny][nx] = 2
                    visited[ny][nx] = True

    for m in Map:
        answer += m.count(0)

    return answer

if __name__ == '__main__':
    main()