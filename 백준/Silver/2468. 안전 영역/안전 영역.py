#안전영역
import sys
input=sys.stdin.readline # input함수 바꾸기
sys.setrecursionlimit(15000) # 10^8 까지 늘림.


dx = [-1,1,0,0]
dy = [0,0,1,-1]

N = int(input())  #안전 높이

a = [[*map(int,input().split())] for _ in range(N)]  # 지역 배열입력

visited = [[0]*N]*N  # 방문 배열 체크

def bfs(i,j,h):
    global visited
    for n in range(0,4):
        ni = i + dx[n] # 다음에 갈 좌표 정해주기
        nj = j + dy[n]
        
        if ni < 0 or nj < 0 or ni >= N or nj >= N: continue#인덱스 범위 체크
        if visited[ni][nj] == 1 : continue # 이미 방문했는지.
        if a[ni][nj] <= h : continue# 물에 잠기는지 확인
            
        visited[ni][nj] = 1

        bfs(ni,nj,h)
        

    return
            
result = 0

max_height = max(list(map(max, a)))

safe_zone = 0
for h in range(0,max_height+1):
     # 초기화
    visited = [[0 for col in range(N)] for row in range(N)]
    safe_zone = 0
    #print(f'물에 잠기는 높이: {h}')
    for i in range(0,N):
        for j in range(0,N):
            if visited[i][j] == 1 : continue
            if a[i][j] <= h : continue
            
            visited[i][j] = 1
            safe_zone += 1
            
            bfs(i,j, h)
    
    #print(f'안전영역: {safe_zone}개')
    result = max(result, safe_zone)
    
   
     
           
    
print(result)       
    

