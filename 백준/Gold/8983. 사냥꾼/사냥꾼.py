M, N, L = map(int, input().split())
mList = list(map(int, input().split()))
nList = [list(map(int, input().split())) for _ in range(N)]
caught = [0 for _ in range(N)]

answer = 0
for m in mList:
    for i in range(N):
        if caught[i] != 0:
            continue
        if abs(nList[i][0]-m) + nList[i][1] <= L:
            answer += 1
            caught[i] = 1


print(answer)