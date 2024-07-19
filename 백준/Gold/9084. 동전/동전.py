import sys
import copy
input = sys.stdin.readline

# Test Case 개수
T = int(input())

def DP(N:int, coins: list, M:int):
    # 결과 값을 저장할 배열을 만든다.
    result = [0 for _ in range(M+1)] # 사용하는 인덱스 1~N 따라서 범위는 N+1
    
    #1 초기값 설정
    result[0] = 1
    coins.sort()
    for coin in coins:
        for i in range(coin,M+1):
            # coin >= i 크다면
            result[i] =  result[i - coin] + result[i]  if result[i - coin] != 0 else result[i] 
        
    print(result[M])

for t in range(T): 
    # N가지 동전 개수
    N = int(input())
    # 동전 종류
    coins = list(map(int, input().split())) # 어차피 중복 되는 입력은 안들어오긴하는데 쉬운 탐색을 위해서~! list를 써도 큰 차이가 있을라나 찾아보기.
    # 목표 금액
    M = int(input())
    
    DP(N, coins, M)






            
            

    
    