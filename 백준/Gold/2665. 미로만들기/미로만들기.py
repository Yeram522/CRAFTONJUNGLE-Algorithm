import sys
import heapq

input=sys.stdin.readline # input함수 바꾸기
sys.setrecursionlimit(15000) # 10^8 까지 늘림.

#input
#한 줄에 들어가는 방의 수
N = int(input())

#미로 맵
Maze = [list(map(int, list(input().rstrip()))) for _ in range(N)] # 붙여서 입력받기 rstrip!!!

# 방향 배열
dx = [1,-1,0,0]
dy = [0,0,1,-1]

INF = int(1e9)
def dijkstra():
    # 최소 힙 초기화
    heap = [(0, 0, 0)]  # (count, x, y)
    visited = [[INF] * N for _ in range(N)]
    visited[0][0] = 0
    
    while heap:
        dist,x,y = heapq.heappop(heap)
        
        if dist > visited[x][y]:
            continue
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx <0 or ny < 0 or nx >=N or ny >=N: continue # 인덱스 범위 체크
            cost = dist
            
            if Maze[nx][ny] == 0 : # 검은방이면 비용 증가
                cost += 1
                
            
            if cost < visited[nx][ny]: #이미 확정된 비용보다 작다면?
                visited[nx][ny] = cost
                heapq.heappush(heap, (cost, nx, ny))
                
    return visited[N-1][N-1]
            
    
   
   
   



print(dijkstra())
        
        
#Note
#의식의 흐름
#1. 뚫을지 안뚫을지를 결정해서 두가지의 재귀함수로 나눠서 풀기 -> 시간초과
#2. 알고보니 1의 방법은 DFS였음
#3. 우리가하려는건 시작-끝까지 최소비용의 검은방. 최소!!!!비용!!!! = BFS
#4. 시작과 끝이 있고 최단거리? = 다익스트라?
#5. 검은방뚫는건 어케해? 어차피 흰방을 어케거쳐가더라도 검은방만 적게!!!지나서 목적지에가면됨
#6. 따라서 비용이 적은 간선을 택한다는 의미가 검은방을 적게 거쳐간다는 의미와 같다.
#7. 검은방을 만나면 비용을 증가시키고, 머 다릏게 돌아가다가 검은방 비용적은 루틴이있ㅇ므 걔가 덮어씌어버리는것!!