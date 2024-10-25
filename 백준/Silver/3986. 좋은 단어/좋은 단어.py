# 좋은 단어
def main():
    answer = 0
    N = int(input())
    for _ in range(N):
        word = list(input())
        stack = []
        for w in word:
            if len(stack) == 0:
                stack.append(w)
                continue
            if stack[-1] == w:
                stack.pop()
            else:
                stack.append(w)
        if not stack:
            answer += 1
    print(answer)


if __name__ == '__main__':
    main()