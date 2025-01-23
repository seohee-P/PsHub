# 수열
def main():
    N, K = map(int, input().split())
    temperature = list(map(int, input().split()))
    max_sum = sum(temperature[:K])
    now_sum = sum(temperature[:K])
    for i in range(1, N - K + 1):
        now_sum -= temperature[i-1]
        now_sum += temperature[i+K-1]
        max_sum = max(now_sum, max_sum)
    print(max_sum)


if __name__ == '__main__':
    main()