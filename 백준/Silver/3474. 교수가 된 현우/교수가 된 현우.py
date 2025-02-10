# 교수가 된 현우
import sys
input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        n = int(input())
        power_5 = 0
        while True:
            if pow(5, power_5) <= n < pow(5, power_5 + 1):
                break
            power_5 += 1
        answer = 0
        for i in range(1, power_5 + 1):
            answer += n // pow(5, i)
        print(answer)

if __name__ == '__main__':
    main()