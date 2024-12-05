import sys
input = sys.stdin.readline

N = int(input()) # 컴퓨터의 수
M = int(input()) # 컴퓨터 쌍의 수

Graph = [ list() for _ in range(N+1) ]  # 인접 리스트

for _ in range(M):
    a,b = map(int, input().split())
    
    Graph[a].append(b)
    Graph[b].append(a)
    
# DFS
visited = [0 for _ in range(N+1)]

queue = list()
queue.append(1) # 처음 시작은 1번 컴퓨터
visited[1] = 1 # 1번 방문처리
count = 0 # 1번 컴퓨터는 제외한 카운트
while(len(queue) != 0):
    idx = queue.pop(0)
    
    for com in Graph[idx]:
        if(visited[com] == 0):
            visited[com] = 1
            count += 1 # 감염 카운트 up
            queue.append(com)
        
        # 방문한적 있다면 방문하지 않는다.
        
print(count)