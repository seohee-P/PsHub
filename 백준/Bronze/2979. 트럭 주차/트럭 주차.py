# 트럭 주차
def main():
    A, B, C = map(int, input().split())
    B, C = B * 2, C * 3
    time = [0 for _ in range(100)]
    for _ in range(3):
        start, end = map(int, input().split())
        for i in range(start-1, end-1):
            time[i] += 1
    answer = 0
    for i in range(100):
        if time[i] == 0:
            continue
        if time[i] == 1:
            answer += A
        elif time[i] == 2:
            answer += B
        elif time[i] == 3:
            answer += C
    print(answer)


if __name__ == '__main__':
    main()