# 1
import sys


def main():
    for line in sys.stdin:
        n = int(line)
        if n == 1:
            print(1)
            continue
        digit = 1
        now = 11
        while True:
            if now % n == 0:
                print(len(str(now)))
                break
            digit += 1
            now += pow(10, digit)


if __name__ == '__main__':
    main()