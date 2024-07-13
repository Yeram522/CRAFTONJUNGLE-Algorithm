import sys
import collections
input=sys.stdin.readline # input함수 바꾸기

N = int(input()) # 컴퓨터 수
M = int(input()) # 컴퓨터 쌍의 수

Graph = {i: [] for i in range(1, N+1)}

for j in range(M):
    u, v = map(int, input().split())
    
    Graph[u].append(v)
    Graph[v].append(u)
    
#1번 컴터씨가 웜바이러스에 걸려부림 ㅉㅉ

def BFS(node):
    global visited
    q = collections.deque([node])
    ret = 0
    
    while q:
        vertex = q.popleft()
        
        for next in Graph[vertex]:
            if next not in visited:
                visited.add(next)
                ret += 1
                q.append(next)
                
                
    return ret
            
            
    


visited = set([1])

print(BFS(1))