import sys
import collections 
input=sys.stdin.readline # input함수 바꾸기
dequeu = collections.deque
#input
N = int(input()) # 보드의 크기
K = int(input()) # 사과의 개수

#사과의 위치
maps = [[0] * N for _ in range(N)] #사과가 위치하는지에 대한 map
for i in range(K):
    y,x = map(int, input().split())
    maps[y-1][x-1] = 1


#뱀의 방향 변환 횟수
L = int(input())
time_dic = {} #dictionary
for j in range(L):
    # 게임 시작 이후 X 초가 끝난 뒤, 해당방향으로 회전
    X, C = input().split()
    time_dic[int(X)] = C

dx = [0, 1, 0, -1]  # 행
dy = [1, 0, -1, 0]  # 열


x,y,d = 0,0,0
time = 0
snake = dequeu([])

while(True):
    snake.append([x,y])
    #시간
    time += 1
    #x초가 끝난 뒤의 위치
               
    #뱀의 이동 
    x += dx[d]
    y += dy[d]
    

    #gameOver조건 : 자기자신 몸에 부딪히거나, 벽에 부딪힐 경우
    if(y < 0 or x < 0 or y >= N or x >= N  or maps[x][y]==2):
        break

    if maps[x][y]==0:#이동할 자리에 사과가 없다.->머리를 늘리고 꼬리를 줄임. pop 하고 insert
        i,j = snake.popleft() #꼬리를 줄인다.
        maps[i][j] = 0
        
    #새자리에 머리를 늘려서 이동
    maps[x][y] = 2
    
    if time in time_dic:
    # 만약 시계방향으로 돈다면
        if time_dic[time] == 'D':
            d = (d + 1) % 4
        else:
            d = (d - 1) % 4
        
    

print(time)