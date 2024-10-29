# 팰린드롬 만들기
def main():
    S = list(input())
    global alpha
    alpha = [0 for _ in range(26)]

    if can_palindrome(S):
        answer = []
        if len(S) % 2 == 0:
            for i in range(26):
                for j in range(alpha[i] // 2):
                    answer.append(chr(ord('A') + i))
            answer += reversed(answer)
            print(''.join(answer))
        else:
            for i in range(26):
                if alpha[i] % 2 == 1:
                    odd_index = i
                for j in range(alpha[i] // 2):
                    answer.append(chr(ord('A') + i))
            answer += (chr(ord('A') + odd_index))
            answer += reversed(answer[:-1])
            print(''.join(answer))
    else:
        print("I'm Sorry Hansoo")


def can_palindrome(S):
    for i in range(len(S)):
        alpha[ord(S[i]) - ord('A')] += 1
    odd = 0
    for i in range(len(alpha)):
        if alpha[i] % 2 == 1:
            odd += 1

    if len(S) % 2 == 0:
        if odd > 0:
            return False
    else:
        if odd != 1:
            return False

    return True


if __name__ == '__main__':
    main()