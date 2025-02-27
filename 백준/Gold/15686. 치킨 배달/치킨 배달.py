# 치킨 배달


def combination(arr, M):
    # 순서 없이 r개를 뽑는 모든 조합 구하기
    result = []

    def dfs(elements, start, k):
        if k == len(elements):
            result.append(elements[:])
            return

        for i in range(start, len(arr)):
            elements.append(arr[i])
            dfs(elements, i + 1, k)
            elements.pop()

    dfs([], 0, M)
    return result

def main():
    N, M = map(int, input().split())
    house = []
    chicken = []
    for i in range(N):
        temp = list(map(int, input().split()))
        for j in range(N):
            if temp[j] == 2:
                chicken.append((i, j))
            if temp[j] == 1:
                house.append((i, j))
    combi = combination(chicken, M)
    answer = 10e9
    for c in combi:
        temp = 0
        for h in house:
            temp2 = abs(h[0] - c[0][0]) + abs(h[1] - c[0][1])
            for i in range(M):
                temp2 = min(temp2, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
            temp += temp2
        answer = min(temp, answer)
    print(answer)

if __name__ == '__main__':
    main()