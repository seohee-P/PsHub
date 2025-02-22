# 최단 경로
import sys, heapq
input = sys.stdin.readline


def main():
    V, E = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(V)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u - 1].append((v - 1, w))

    distance = dijkstra(graph, start)
    for d in distance:
        print("INF" if d == float('inf') else d)


def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start - 1] = 0
    heap = [(0, start - 1)]

    while heap:
        dist, current = heapq.heappop(heap)

        if dist > distance[current]:
            continue


        for next_node, weight in graph[current]:
            new_dist = dist + weight

            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))

    return distance


if __name__ == '__main__':
    main()