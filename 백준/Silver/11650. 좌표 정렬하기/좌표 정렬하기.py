# 좌표 정렬하기
import sys
input = sys.stdin.readline

def main():
    position = []
    for _ in range(int(input())):
        position.append(list(map(int, input().split())))
    position = sorted(position, key=lambda x: (x[0], x[1]))
    for p in position:
        print(p[0], p[1])

if __name__ == '__main__':
    main()