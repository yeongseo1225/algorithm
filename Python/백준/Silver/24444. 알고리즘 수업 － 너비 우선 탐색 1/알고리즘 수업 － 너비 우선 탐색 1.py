import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque

n, m, r = map(int, input().split())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
 
for i in range(1, n+1):
    graph[i].sort()

c = 1 
def BFS(v):
    global c
    queue = deque()
    queue.append(v)
    visited[v] = c
    while queue:
        now_node = queue.popleft()
        for i in graph[now_node]:
            if visited[i] == 0:
                c+=1
                visited[i] = c
                queue.append(i)

BFS(r)

for i in range(1,n+1):
    print(visited[i])
    