import sys
input = sys.stdin.readline

R,C = map(int, input().split()) # N, M

arr = [list(input().strip()) for _ in range(C)]
visited = [[0 for i in range(R)] for j in range(C)] # 방문 여부 배열
dr = [0,0,1,-1]
dc = [1,-1,0,0]


def BFS(c : int, r : int, team : str):
    visited[c][r] = 1 # 방문처리
    count = 0
    
    for dir in range(4):
        # 새로운 좌표
        nr = r + dr[dir]
        nc = c + dc[dir]
        
        # 범위 유효성 체크
        if(nr < 0 or nc < 0 or nr >= R or nc >= C):
            continue
        
        # 같은 팀 체크
        if(arr[nc][nr] != team):
            continue
        
        # 방문 여부 체크
        if(visited[nc][nr] == 0):
            count += BFS(nc, nr , team) + 1
            
    return count
        
        
# arr의 모든 좌표를 탐색한다.-> Component 찾기
Power = [0,0] # W, B

for c in range(C):
    for r in range(R):
        team = arr[c][r]
        if(visited[c][r] == 0):
            Power[0 if team == 'W' else 1] += (BFS(c,r, team)+1)**2 # N^2
            
            
print(*Power, sep=' ')