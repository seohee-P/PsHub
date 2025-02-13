# 단지번호 붙이기
from collections import deque

def main():
    n = int(input())
    Map = [list(input()) for _ in range(n)]
    answer = 0
    counts = []
    for i in range(n):
        for j in range(n):
            if Map[i][j] == '0':
                continue
            answer += 1
            count = 0
            queue = deque([(i, j)])
            Map[i][j] = '0'
            while queue:
                y, x = queue.popleft()
                count += 1
                for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < n and 0 <= nx < n and Map[ny][nx] == '1':
                        Map[ny][nx] = '0'
                        queue.append((ny, nx))
            counts.append(count)
    counts.sort()
    print(answer)
    print(*counts, sep='\n')


if __name__ == '__main__':
    main()