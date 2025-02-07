# 균형잡힌 세상
import sys

input = sys.stdin.readline


def main():
    for line in sys.stdin:
        s = line.rstrip()
        if s == ".":
            break
        stack = []
        for c in s:
            if c != "(" and c != "[" and c != "]" and c != ")":
                continue
            if not stack:
                stack.append(c)
                continue
            if c == "(" or c == "[":
                stack.append(c)
                continue
            if c == "]" and stack[-1] == "[":
                stack.pop()
                continue
            if c == ")" and stack[-1] == "(":
                stack.pop()
                continue
            stack.append(c)

        print("yes") if not stack else print("no")


if __name__ == "__main__":
    main()
