# 구간 합 구하기
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def main():
    global tree;
    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    tree = [0 for _ in range(N * 4)]
    init(arr, 1, 0, N - 1)
    for _ in range(M + K):
        command, num1, num2 = map(int, input().split())
        if command == 1:
            update(1, 0, N - 1, num1 - 1, num2)
        elif command == 2:
            print(query(1, 0, N - 1, num1 - 1, num2 - 1))


def query(node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2

    left_sum = query(2 * node, start, mid, left, right)
    right_sum = query(2 * node + 1, mid + 1, end, left, right)
    return left_sum + right_sum


def update(node, start, end, idx, value):
    if start == end:
        tree[node] = value
        return
    mid = (start + end) // 2
    if idx <= mid:
        update(2 * node, start, mid, idx, value)
    else:
        update(2 * node + 1, mid + 1, end, idx, value)

    tree[node] = tree[2 * node] + tree[2 * node + 1]


def init(arr, node, start, end):
    if start == end:
        tree[node] = arr[start]
        return

    mid = (start + end) // 2
    init(arr, 2 * node, start, mid)
    init(arr, 2 * node + 1, mid + 1, end)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


if __name__ == '__main__':
    main()
