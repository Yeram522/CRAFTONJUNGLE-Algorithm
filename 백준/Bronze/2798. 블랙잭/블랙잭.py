import sys
input = sys.stdin.readline

N,M = map(int, input().split())

lst = list(map(int, input().split()))

result = list()

def Combi(count : int, index : int, sum : int):
    global result
    
    if(sum > M): #합이 M보다 크면 X
        return
    
    if(count == 3):# 합이 M보다 작고 3개 골랐을 떄
        result.append(sum)# M과 차이가 적은 것
        return
    
    # index 유효성 검사
    if(index+1 >= N):
        return
    
    # 다음 수를 선택할 경우
    Combi(count+1, index+1, sum + lst[index])
    # 다음 수를 선택하지 않을 경우
    Combi(count, index+1 , sum )
    

Combi(0,-1,0)

print(max(result))