# 듣보잡
import sys
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    set_n = set()
    set_m = set()
    for _ in range(n):
        set_n.add(input().rstrip())
    for _ in range(m):
        set_m.add(input().rstrip())
    set_n = set_n.intersection(set_m)
    print(len(set_n))
    list_n = sorted(list(set_n))
    for n in list_n:
        print(n)

if __name__ == '__main__':
    main()