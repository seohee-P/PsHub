# 이중 우선순위 큐
from collections import defaultdict
import sys, heapq
input = sys.stdin.readline


def main():
    for _ in range(int(input())):
        max_heap = []
        min_heap = []
        value = defaultdict(int)
        k = int(input())
        for _ in range(k):
            while min_heap and value[min_heap[0]] < 1:
                heapq.heappop(min_heap)
            while max_heap and value[max_heap[0][1]] < 1:
                heapq.heappop(max_heap)
            command = input().split()
            if command[0] == 'I':
                num = int(command[1])
                heapq.heappush(max_heap, (-num, num))
                heapq.heappush(min_heap, num)
                value[num] += 1
            if command[0] == 'D':
                if command[1] == '1':
                    if max_heap:
                        value[max_heap[0][1]] -= 1
                        heapq.heappop(max_heap)
                else:
                    if min_heap:
                        value[min_heap[0]] -= 1
                        heapq.heappop(min_heap)

        while min_heap and value[min_heap[0]] < 1:
            heapq.heappop(min_heap)
        while max_heap and value[max_heap[0][1]] < 1:
            heapq.heappop(max_heap)

        if not max_heap or not min_heap:
            print("EMPTY")
        else:
            print(max_heap[0][1], min_heap[0])


if __name__ == "__main__":
    main()