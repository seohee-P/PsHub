# 절댓값 힙
import sys, heapq
input = sys.stdin.readline

def main():
    heap = []
    for _ in range(int(input())):
        x = int(input())
        if x != 0:
            heapq.heappush(heap, (abs(x), x))
            continue
        print(0) if not heap else print(heapq.heappop(heap)[1])


if __name__ == '__main__':
    main()