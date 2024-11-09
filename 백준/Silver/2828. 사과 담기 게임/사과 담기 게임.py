# 사과 담기 게임
def main():
    N, M = map(int, input().split())
    J = int(input())
    now, answer = 1, 0
    for _ in range(J):
        apple = int(input())
        if now <= apple < now + M:
            continue
        if apple >= now + M:
            move = apple - (now + M - 1)
            answer += move
            now += move
        if apple < now:
            answer += (now - apple)
            now = apple
    print(answer)


if __name__ == '__main__':
    main()