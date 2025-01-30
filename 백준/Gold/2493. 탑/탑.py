# 탑
def main():
    N = int(input())
    A = list(map(int, input().split()))
    stack = [(A[0], 0)]
    answer = [0 for _ in range(N)]
    for i in range(1, N):
        while stack and stack[-1][0] < A[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1][1] + 1
        else:
            answer[i] = 0
        stack.append((A[i], i))
    print(*answer)

if __name__=='__main__':
    main()