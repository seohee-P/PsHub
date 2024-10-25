# 패션왕 신해빈
from collections import defaultdict

def main():
    for _ in range(int(input())):
        n = int(input())
        dict = defaultdict(int)
        for i in range(n):
            name, type = input().split()
            dict[type] += 1
        answer = 1
        for value in dict.values():
            answer *= (value+1)
        print(answer-1)


if __name__ == '__main__':
    main()