# 집합
import sys
input = sys.stdin.readline

def main():
    s = [0 for _ in range(21)]
    for _ in range(int(input())):
        command = input().split()

        if command[0] == 'add':
            s[int(command[1])] = 1
            continue

        if command[0] == 'remove':
            if s[int(command[1])] == 1:
                s[int(command[1])] = 0
            continue

        if command[0] == 'check':
            print(1) if s[int(command[1])] == 1 else print(0)
            continue

        if command[0] == 'toggle':
            if s[int(command[1])] == 1:
                s[int(command[1])] = 0
            else:
                s[int(command[1])] = 1
            continue

        if command[0] == 'all':
            s = [1 for _ in range(21)]
            continue

        if command[0] == 'empty':
            s = [0 for _ in range(21)]
            continue


if __name__ == '__main__':
    main()