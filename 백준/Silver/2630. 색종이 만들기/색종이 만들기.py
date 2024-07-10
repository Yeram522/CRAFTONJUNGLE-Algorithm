import sys
input=sys.stdin.readline # input함수 바꾸기
import copy
#input
N = int(input()) # 종이의 크기

W=[[*map(int,input().split())] for _ in range(N)] # 정리 해두기 N행 배열 입력 받는 법

result = []

#크기가 4씩 나눠짐.
def divided_conquer(div, start): # start = {x,y}
    color = W[start[0]][start[1]]

    for i in range(start[0], start[0] + div):
        for j in range(start[1], start[1]+div):
            if color != W[i][j]:
                # 만약 다른 색이 나온다면 분할한다.
                divided_conquer(div//2, start) 
            
                divided_conquer(div//2, [start[0], start[1]+ div//2 ])
            
                divided_conquer(div//2, [start[0]+ div//2 , start[1]])
            
                divided_conquer(div//2, [start[0]+ div//2 , start[1]+ div//2 ])
                
                return
            
                
    if color == 0:
        result.append(0)
    else:
        result.append(1)
        
    
    return 



divided_conquer(N, [0,0])

print(result.count(0))
print(result.count(1))
    