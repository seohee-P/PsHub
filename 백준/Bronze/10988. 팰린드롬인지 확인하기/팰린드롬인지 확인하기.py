# 팰린드롬인지 확인하기
def main():
    s = input()
    print(1) if s == s[::-1] else print(0)


if __name__ == '__main__':
    main()