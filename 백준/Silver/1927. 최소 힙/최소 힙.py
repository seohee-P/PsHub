# 최소 힙
import sys, heapq
input = sys.stdin.readline

def main():
    heap = []
    for i in range(int(input())):
        x = int(input())
        if x == 0:
            print(0) if not heap else print(heapq.heappop(heap))
        else:
            heapq.heappush(heap, x)

if __name__ == '__main__':
    main()