# 최솟값과 최댓값
import sys
input = sys.stdin.readline

def init(arr, node, start, end):
    if start == end:
        tree[node] = [arr[start], arr[start]]
        return

    mid = (start + end) // 2

    init(arr, 2*node, start, mid)
    init(arr, 2*node+1, mid + 1, end)
    tree[node] = [min(tree[2*node][0], tree[2*node+1][0]), max(tree[2*node][1], tree[2*node+1][1])]

def find_min_max(node, start, end, left, right):
    if left > end or right < start:
        return [10e9, -10e9]

    if left <= start and right >= end:
        return tree[node]

    mid = (start + end) // 2
    left_result = find_min_max(2*node, start, mid, left, right)
    right_result = find_min_max(2*node+1, mid + 1, end, left, right)
    return [min(left_result[0], right_result[0]), max(left_result[1], right_result[1])]



def main():
    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]
    global tree
    tree = [0] * (N * 4)
    init(arr, 1, 0, N-1)
    for _ in range(M):
        left, right = map(int, input().split())
        print(*find_min_max(1, 0, N-1, left-1, right-1))


if __name__ == '__main__':
    main()