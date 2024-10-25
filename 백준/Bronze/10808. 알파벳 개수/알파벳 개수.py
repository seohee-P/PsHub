# 알파벳 개수
def main():
    alphabet = [0 for _ in range(26)]
    S = list(input())
    for s in S:
        alphabet[ord(s)-97] += 1
    print(*alphabet)


if __name__ == '__main__':
    main()