# 안전 영역
from collections import deque


def main():
    N = int(input())
    area = []
    max_rain = 0
    for i in range(N):
        temp = list(map(int, input().split()))
        max_rain = max(max_rain, max(temp))
        area.append(temp)

    def check_safe_area(rain):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        queue = deque()
        count_area = 0
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 1 or area[i][j] <= rain:
                    continue
                count_area += 1
                queue.append([i, j])
                visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny] == 0 and area[nx][ny] > rain:
                                visited[nx][ny] = 1
                                queue.append([nx, ny])
        return count_area

    answer = 0
    for i in range(max_rain):
        answer = max(answer, check_safe_area(i))
    print(answer)


if __name__ == '__main__':
    main()