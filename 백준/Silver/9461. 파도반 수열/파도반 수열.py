# 파도반 수열
def main():
    for _ in range(int(input())):
        N = int(input())
        answer = [1 for _ in range(N)]
        if N > 3:
            for i in range(3, N):
                answer[i] = answer[i - 2] + answer[i - 3]
        print(answer[N-1])


if __name__ == '__main__':
    main()
