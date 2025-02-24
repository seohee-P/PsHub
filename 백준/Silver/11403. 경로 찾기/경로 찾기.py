# 경로 찾기
def main():
    n = int(input())
    dist = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dist[i][j] == 0:
                dist[i][j] = float('inf')


    for k in range(n):
        for s in range(n):
            for e in range(n):
                dist[s][e] = min(dist[s][e], dist[s][k] + dist[k][e])

    for i in range(n):
        for j in range(n):
            if dist[i][j] == float('inf'):
                dist[i][j] = 0
                continue
            if dist[i][j] > 0:
                dist[i][j] = 1

    for d in dist:
        print(*d)

if __name__ == '__main__':
    main()