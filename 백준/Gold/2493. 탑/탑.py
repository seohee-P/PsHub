import heapq

def main():
    N = int(input())
    A = list(map(int, input().split()))
    heap = [(A[0], 0)]
    answer = [0 for _ in range(N)]
    for i in range(1, N):
        while heap and heap[0][0] < A[i]:
            heapq.heappop(heap)
        if heap:
            answer[i] = heap[0][1] + 1
        else:
            answer[i] = 0
        heapq.heappush(heap, (A[i], i))
    print(*answer)

if __name__=='__main__':
    main()