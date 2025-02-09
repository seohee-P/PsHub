# 수학숙제
import sys
input = sys.stdin.readline

def main():
    answer = []
    for _ in range(int(input())):
        s = input()
        num = ''
        for l in s:
            if not l.isdigit():
                if num:
                    answer.append(int(num))
                    num = ''
                continue
            num += l
        if len(num) > 0:
            answer.append(int(num))
    answer.sort()
    print(*answer, sep="\n")

if __name__ == "__main__":
    main()