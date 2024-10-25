# ROT13
def main():
    S = list(input())
    for i in range(len(S)):
        if not S[i].isalpha():
            continue
        if S[i].isupper():
            S[i] = chr((ord(S[i]) - ord('A') + 13) % 26 + 65)
        else:
            S[i] = chr((ord(S[i]) - ord('a') + 13) % 26 + 97)
    print(''.join(S))


if __name__ == '__main__':
    main()