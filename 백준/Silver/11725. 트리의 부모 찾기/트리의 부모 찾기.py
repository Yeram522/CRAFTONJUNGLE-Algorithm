import sys
input=sys.stdin.readline # input함수 바꾸기
sys.setrecursionlimit(10**5)
# input 
N = int(input())

Graph = {i: [] for i in range(1, N+1)}

for i in range(N-1):
    u, v = map(int, input().split())
    
    Graph[u].append(v)
    Graph[v].append(u)
    
    
parents = [0] * (N - 1)  # 부모 테이블 초기화
visited = [False] * (N + 1)  # 방문 여부 체크
   
def DFS(node):
    global visited
    global parents
    visited[node] = True
    for next in Graph[node]:
         if not visited[next]:
            parents[next-2] = node #자식과 연결되면 현재노드가 이자식의 부모임.
            DFS(next)
            
    return
        
DFS(1)

for p in parents:
    print(p)