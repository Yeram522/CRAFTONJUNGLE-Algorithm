import sys
from collections import deque
input=sys.stdin.readline # input함수 바꾸기

# input
# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시의 번호
N, M ,K, X = map(int, input().split())

Graph = {i: [] for i in range(1, N+1)}

# 도로의 개수만큼 for = 간선의 개수
for i in range(M):
    # 방향 그래프임!!!!
    A, B = map(int, input().split())
    
    Graph[A].append(B)
    
# 구현
def BFS(start):
    q = deque([start])
    # 방문하지 않은 도시를 -1로두고 시작지점을 0으로 둔다.
    distance = [-1 for _ in range(N+1)] # 시작 위치에서의 떨어진 거리.
    distance[start - 1] = 0
    result = list()
    while q:
        node = q.popleft()
        
        for next in Graph[node]: # 갈 수 있는  도시 탐색
            if distance[next-1] == -1: # 간적없다면?
                
                distance[next-1] = distance[node-1] + 1 # 거리 한칸 증가아.
            
            
            
                if distance[next-1] == K : result.append(next) # 조건에 만족하면 리스트에 추가
            
                q.append(next)
            
    if result:
        result.sort()
        for r in result:
            print(r)     
    else:
        print(-1)
        
        
    return
  


BFS(X)
    
    
# 처음에 틀린이유 출발도시를 1로 나둬가지고ㅠㅠX로 뒀어야햇는데 바보임?ㅋㅋ

