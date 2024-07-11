import sys
#input
N = int(sys.stdin.readline())# 영상 크기

W= [sys.stdin.readline() for _ in range(N)]# 정리 해두기 N행 배열 입력 받는 법

result = list()   #문자열 리스트이다.


def quad_tree(x,y, div): # x,y 좌표, 나누는 분기
    color = int(W[x][y])
    
    for i in range(x,x + div):
        for j in range(y,y + div):
            if color != int(W[i][j]):
                result.append('(')
                quad_tree(x,y, div//2)
                quad_tree(x,y+div//2, div//2)
                quad_tree(x+div//2,y, div//2)
                quad_tree(x+div//2,y+div//2, div//2)
                result.append(')')
                return
            
    if color == 1:
        result.append('1')
    else:
        result.append('0')
    return 
                
    
                       
quad_tree(0,0,N)


for r in result:
    print(r, end='')