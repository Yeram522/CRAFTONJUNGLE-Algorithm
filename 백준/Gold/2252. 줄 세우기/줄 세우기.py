import sys
from collections import deque 
input = sys.stdin.readline

# 일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 ?

N, M = map(int, input().split())

Graph = {i : [] for i in range(1,N+1)}

indegree = [0 for _ in range(N)] # indegree 배열

for i in range(M):
    A, B = map(int, input().split())
    Graph[A].append(B) # 방향 그래프 세팅
    # 들어오는 간선을 읽으며 indegree ( 들어오는 간선의 수) 테이블을 채운다.
    indegree[B-1] += 1 # B로 간선이 들어가므로 B-1 인덱스로 테이블 값 접근 후 1증가시킨다.
    
   
#줄 세우기 
# 순서 작은 -> 큰
q = deque()
# indegree가 0인 정점을 모두 q에 채운다.
for i in range(len(indegree)):
    if indegree[i] == 0:
        q.append(i+1) # i는 인덱스이므로 1 더해서 넣어준다.
  
result = list()      
while q:
    vertex = q.popleft()
    
    # 큐에서 정점을 꺼낸 후 위상 정렬 결과에 추가
    result.append(vertex)
    for next in Graph[vertex]:
        indegree[next-1] -= 1
        if indegree[next-1] == 0:
            q.append(next)
            
            
print(" ".join(map(str, result)))
 