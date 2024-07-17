import sys
from collections import deque
input = sys.stdin.readline

# 입력
n, k = map(int,input().split())

coins = set()

for _ in range(n):
    coins.add(int(input()))
    

dp = [1e9] * (k + 1)
        
dp[0] = 0


for i in range(1,k+1):
    for coin in coins:
        if i - coin >= 0 : 
            dp[i] = min(dp[i] , dp[i-coin] + 1) 
        
# 결과 출력
if dp[k] == 1e9:
    print(-1)  # k원을 만들 수 없는 경우
else:
    print(dp[k])
    
# 메모리 초과 개빡치네"?


# 참고문제
# https://www.acmicpc.net/problem/1463