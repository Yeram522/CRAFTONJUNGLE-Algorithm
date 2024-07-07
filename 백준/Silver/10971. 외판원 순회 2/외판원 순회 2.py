# 외판원 순환

# 입력

N = int(input())

W=[[*map(int,input().split())] for _ in range(N)] # 정리 해두기 N행 배열 입력 받는 법

min_cost = 1e9
visited = [False for _ in range(N)]  # 방문 여부
temp  = list()

def go(depth, cost)->int:
    global min_cost 
    if( depth == N ): 
        if W[temp[N-1]][temp[0]] == 0 : return
        #print(f'{next} to {start}: {distance}+{W[next][start]}')
        #print(f"distance = {distance}")
        min_cost= min(min_cost, cost + W[temp[N - 1]][temp[0]])  # 최솟값 갱신
        return 0 
    
    
    for i in range(N):

        if depth == 0 or (visited[i] == False and W[temp[depth-1]][i] != 0):
            temp.append(i)
            visited[i] = True # visited check
        
            go( depth + 1, cost + W[temp[depth-1]][i])
        
            temp.pop()
            visited[i] = False
        
        
    return 0
        


        

go(0, 0)

   
print(min_cost)

