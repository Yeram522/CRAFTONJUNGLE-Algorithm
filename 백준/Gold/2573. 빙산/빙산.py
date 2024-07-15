import sys
import copy
input=sys.stdin.readline # input함수 바꾸기

#input
N, M = map(int, input().split())
 
MAP = [list(map(int, input().split())) for _ in range(N)]

#어쨋든 뭐라도 하나 녹아야 분리가 되던가 말던가 하니까..
# 높이의 최소값부터 년도를 건너뛰기 해서 범위를 줄일수있음.
dx = [1,-1,0,0]
dy = [0, 0,1,-1]
# 컴포넌트 찾기
def DFS(x,y,visited):
    stack = [[x,y]]
    while(stack):
        pos = stack.pop()
        x = pos[0]
        y = pos[1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M : continue  # 탐색 불가능한 조건
            if visited[nx][ny] == 1: continue 
            if MAP[nx][ny] == 0: continue #바다이면 가지 X
            # 탐색 가능할때 stack에 해당 위치 추가
            visited[nx][ny] = 1 # 방문 처리
            stack.append([nx,ny])
            
    return

    
visited = [[0 for _ in range(M)] for _ in range(N)]
year = 0
count = 0
while True: #count가 2가 초과되는 순간 반복문 종료 
    # 방문배열과 카운트 초기화.
    visited =[[0 for _ in range(M)] for _ in range(N)] # 초기화
    count = 0
                    
    #isMelted = True
    for i in range(N):
        for j in range(M):
            if MAP[i][j] == 0: continue
            # 0일때는 무시하구. 아닐때부터 component 탐색
            if visited[i][j] == 1 : continue #이미 visited?면 무시.
            visited[i][j] = 1 # 방문 처리
            count += 1
            DFS(i, j, visited)
            
    
    if count >= 2:
        break

        
    NMAP = copy.deepcopy(MAP) # 1년에 감소되는 빙하는 동시적이므로 탐색이 꼬이지 않게 복사본을 참조하여 계산한다.
    # 빙하 높이 업데이트
    for i in range(N):
        for j in range(M):
            if NMAP[i][j] == 0: continue  # 바다면 탐색하지 않는다.
            for z in range(4):
                nx = i + dx[z]
                ny = j + dy[z]
                if nx < 0 or ny < 0 or nx >= N or ny >= M : continue
                if NMAP[nx][ny] == 0: # 바다이다?
                    MAP[i][j] = max(0, MAP[i][j] - 1)   #바다이면 해당 감소시킨다.
    
    
    if all(MAP[i][j] == 0 for i in range(N) for j in range(M)):
        year = 0  # 모든 빙하가 녹았다면 0년
        break
    
    # 얘는 초기화 ㄴㄴ        
    year += 1 
      
   
    #print(f'{year}년후')
    
    #for row in MAP:
        
        #print(row)
    

#print(f'빙하개수:{count}')
print(year)