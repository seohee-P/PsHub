# 우체국
import sys
input = sys.stdin.readline

def main():
    n = int(input())
    sum_people = 0
    village = dict()
    for _ in range(n):
        v, p = map(int, input().split())
        sum_people += p
        village[v] = p
    villages = sorted(village.items(), key=lambda x: x[0])
    temp = 0
    for v, p in villages:
        temp += p
        if temp >= sum_people // 2 and sum_people % 2 == 0:
            print(v)
            break
        elif temp >= sum_people // 2 + 1:
            print(v)
            break


if __name__ == '__main__':
    main()