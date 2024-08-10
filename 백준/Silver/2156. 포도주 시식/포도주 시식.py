import sys
input = sys.stdin.readline

N = int(input())

arr = [ 0 for _ in range(N+1)] # arr도 1부터 시작

for _ in range(1,N+1):
    arr[_] = int(input())

DP = [ 0 for _ in range(N+1)]
DP[1] = arr[1]

# 초기값 예외처리
if N >= 2:
    DP[2] = DP[1] + arr[2] 

if N >= 3:
    for i in range(3, N+1):
        DP[i] = max(DP[i-1],DP[i-2] + arr[i] , DP[i-3] + arr[i] + arr[i-1])
        
print(DP[N])