import sys
input = sys.stdin.readline

MOD = 1000000000

N = int(input())

# 1 <= N <= 100
DP = [[0 for _ in range(10)] for _ in range(N+1)] # 수의 길이와 올수있는 숫자종류 0~9 

# 초기 조건 설정 (1자리 숫자)
for i in range(1, 10):  # 0으로 시작하는 수는 계단 수가 아니므로 1부터 시작
    DP[1][i] = 1

if N >= 2:
    for i in range(2, N+1):
        DP[i][0] = DP[i-1][1] % MOD
        
        for j in range(1, 9):
            DP[i][j] = (DP[i-1][j-1] + DP[i-1][j+1]) % MOD
        
        DP[i][9] = DP[i-1][8] % MOD

result = sum(DP[N]) % MOD
        
print(result)