# 여행 가자

global parent

def init(N):
    global parent
    parent = [i for i in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def main():
    N = int(input())
    M = int(input())
    road = [list(map(int, input().split())) for _ in range(N)]
    plan = list(map(int, input().split()))
    init(N)
    for i in range(N):
        for j in range(N):
            if road[i][j] == 0:
                continue
            union(i, j)

    root = find(plan[0]-1)
    for p in plan:
        if find(p-1) != root:
            print("NO")
            return
    print("YES")


if __name__ == '__main__':
    main()
