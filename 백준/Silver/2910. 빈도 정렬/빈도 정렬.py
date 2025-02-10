# 빈도 정렬
def main():
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    result = dict()
    for i in range(N):
        key = A[i]
        if key in result:
            result[key][0] += 1
        else:
            result[key] = [1, i]
    sorted_dict = sorted(result.items(), key=lambda x: (-x[1][0], x[1][0]))
    answer = []
    for k, v in sorted_dict:
        answer += [k] * v[0]
    print(*answer)


if __name__ == '__main__':
    main()
