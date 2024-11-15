# 오큰수
import heapq


def main():
    N = int(input())
    A = list(map(int, input().split()))
    answer = [-1 for i in range(N)]
    heap = []
    for i in range(N - 1, -1, -1):
        while heap and heap[0] <= A[i]:
            heapq.heappop(heap)
        if len(heap) > 0:
            answer[i] = heap[0]
        heapq.heappush(heap, A[i])

    print(*answer)


if __name__ == '__main__':
    main()