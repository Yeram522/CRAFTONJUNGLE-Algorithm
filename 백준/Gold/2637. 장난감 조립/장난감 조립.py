import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())
M = int(input())

Graph = { i : {} for i in range(1, N+1)} # 이중 딕셔너리!
need = [0 for _ in range(N+1)] # indegree 개수를 센 리스트
indegree = [0 for _ in range(N+1)]
for i in range(M):
    X, Y, K = map(int, input().split())
    
    Graph[X][Y] = K
    need[Y] += 1
    indegree[X] += 1
    
basic_part = list()
for i in range(1, N+1):
    if indegree[i] == 0:
        basic_part.append(i) # i는 인덱스이므로 1 더해서 넣어준다.
        
q = deque([N])
count =[0 for _ in range(N+1)]
count[N] = 1

while q:# 큐는 기본 부품 리스트!!
    node = q.popleft() # 1시작이야!!
    for next,cost in Graph[node].items():        
        need[next] -= 1
        count[next] += cost*count[node]
        if need[next] == 0:
            q.append(next)

for i in basic_part:
    print(i, count[i])