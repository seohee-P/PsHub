# 농구 경기
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    alphabet = [0 for _ in range(26)]
    for i in range(N):
        name = input().strip()
        alphabet[ord(name[0]) - 97] += 1
    answer = []
    for i in range(26):
        if alphabet[i] >= 5:
            answer.append(chr(i + 97))

    if not answer:
        print("PREDAJA")
    else:
        print(''.join(answer))


if __name__ == '__main__':
    main()