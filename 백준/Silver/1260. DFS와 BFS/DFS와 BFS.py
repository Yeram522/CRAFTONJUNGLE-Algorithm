import sys
import collections
sys.setrecursionlimit(15000) # 10^8 까지 늘림.
input=sys.stdin.readline # input함수 바꾸기

N, M, V  = map(int, input().split())

edges = {}

for i in range(M):
    a, b = map(int, input().split()) 
    
    #간선은 양방향!
    if edges.get(a): # 딕셔너리에 해당 키가 있는지 판별
        edges[a].append(b) #0은 visited 판별
    else:
        edges[a] = [b]
        
    if edges.get(b): # 딕셔너리에 해당 키가 있는지 판별
        edges[b].append(a) #0은 visited 판별
    else:
        edges[b] = [a]
        
edges = dict(sorted(edges.items()))

for edge, lst in edges.items(): 
    lst.sort()
    
def DFS(node, visited): # 깊이 우선 탐색
    visited.add(node)
    if edges.get(node) == None: return
    for next in edges[node]:
        if next not in visited:
            print(next, end=" ")
            DFS(next, visited)
            
    return
     

def BFS(node): #넓이 우선 탐색
    queue = collections.deque([node])
    visited = set([node])
    
    while queue:
        vertex = queue.popleft()
        if edges.get(vertex) == None : return
        for next in edges[vertex]:
            if next not in visited:
                visited.add(next)
                print(next, end = " ")
                queue.append(next)
                
    return 
        
        
visited = set()
print(V, end = " ")
DFS(V,visited)
print()
print(V, end = " ")
BFS(V)