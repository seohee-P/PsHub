# DFS와 BFS
import sys
from collections import deque, defaultdict

input = sys.stdin.readline

def bfs(V, N, vertex):
    queue = deque([V])
    visited = [False] * (N + 1)
    visited[V] = True
    while queue:
        V = queue.popleft()
        print(V, end=" ")
        for v in vertex[V]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

def dfs(V, N, vertex, temp):
    stack = [V]
    visited = [False] * (N + 1)
    while stack:
        V = stack.pop()
        if visited[V]:
            continue
        visited[V] = True
        print(V, end=" ")
        for i in range(len(vertex[V])-1, -1, -1):
            if not visited[vertex[V][i]]:
                stack.append(vertex[V][i])



def main():
    N, M, V = map(int, input().split())
    vertex = defaultdict(set)
    for _ in range(M):
        s, e = map(int, input().split())
        vertex[s].add(e)
        vertex[e].add(s)

    for v in vertex.keys():
        vertex[v] = sorted(list(vertex[v]))

    temp = []
    dfs(V, N, vertex, temp)
    print()
    bfs(V, N, vertex)


if __name__ == '__main__':
    main()