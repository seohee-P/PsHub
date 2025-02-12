# 집합
import sys
input = sys.stdin.readline

def main():
    s = set()
    for _ in range(int(input())):
        command = input().split()

        if command[0] == 'add':
            s.add(int(command[1]))
            continue

        if command[0] == 'remove':
            if int(command[1]) in s:
                s.remove(int(command[1]))
            continue

        if command[0] == 'check':
            if int(command[1]) in s:
                print(1)
            else:
                print(0)
            continue

        if command[0] == 'toggle':
            if int(command[1]) in s:
                s.remove(int(command[1]))
            else:
                s.add(int(command[1]))
            continue

        if command[0] == 'all':
            s = set([i for i in range(1, 21)])
            continue

        if command[0] == 'empty':
            s.clear()
            continue

if __name__ == '__main__':
    main()