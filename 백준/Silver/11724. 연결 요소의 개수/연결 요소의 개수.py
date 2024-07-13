import sys
import collections
input=sys.stdin.readline # input함수 바꾸기

# input 
N, M = map(int, input().split())

Graph = {i: [] for i in range(1, N+1)}

for i in range(M):
    u, v = map(int, input().split())
    
    Graph[u].append(v)
    Graph[v].append(u)

"""for g ,v in Graph.items():
    print(g,v)"""
    

# Component 구하기
# 연결되어있는거 쭈우우욱 확인.
def BFS(node):
    global visited
    q = collections.deque([node]) 
    
    # 들어온 노드에 연결된노드 큐에넣기
    while q:    
        vertex = q.popleft() 
        for next in Graph[vertex]:
            if next not in visited:
                visited.add(next)
                q.append(next)
                
                
visited = set()
count = 0
for g in Graph:
    if g not in visited:
        visited.add(g)
        BFS(g)
        count += 1

print(count)