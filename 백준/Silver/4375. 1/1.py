# 1
import sys

def main():
    for line in sys.stdin:
        n = int(line)
        now = 1
        answer = 1
        while now % n != 0:
            answer += 1
            now = (10 * now + 1)%n
        print(answer)

if __name__ == '__main__':
    main()