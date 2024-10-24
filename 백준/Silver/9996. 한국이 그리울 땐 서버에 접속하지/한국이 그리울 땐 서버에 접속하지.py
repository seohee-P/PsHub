# 한국이 그리울 땐 서버에 접속하지
def main():
    N = int(input())
    pattern_start, pattern_end = input().split("*")
    files = [input() for _ in range(N)]

    for file in files:
        if file.startswith(pattern_start) and file.endswith(pattern_end):
            if len(pattern_start) + len(pattern_end) <= len(file):
                print("DA")
            else:
                print("NE")
        else:
            print("NE")


if __name__ == '__main__':
    main()