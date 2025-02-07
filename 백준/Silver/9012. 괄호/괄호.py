# 괄호
import sys

input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        PS = input().rstrip()
        stack = []
        for p in PS:
            if not stack:
                stack.append(p)
                continue
            if stack[-1] == "(" and p == ")":
                stack.pop()
            else:
                stack.append(p)

        print("YES") if not stack else print("NO")


if __name__ == "__main__":
    main()