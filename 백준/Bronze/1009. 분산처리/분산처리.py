# 분산처리

def main():
    for _ in range(int(input())):
        a, b = map(int, input().split())
        answer = pow(a, b, 10)
        print(answer) if answer != 0 else print(10)


if __name__ == '__main__':
    main()
