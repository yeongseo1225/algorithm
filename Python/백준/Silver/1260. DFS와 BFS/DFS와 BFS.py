import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

from collections import deque
n, m, v = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()
  
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in graph[v]:
        if not visited[i]:
            DFS(i)
            
visited = [False] * (n+1)
DFS(v)    

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft()
        print(now_Node, end=' ')
        for i in graph[now_Node]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
visited = [False] * (n+1)
print()
BFS(v)