import sys

N = int(input())

Cost = [[0 for _ in range(N)] for _ in range(N)]
DP = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    R, G, B = map(int, input().split())
    Cost[i][0] = R
    Cost[i][1] = G
    Cost[i][2] = B
    
DP[1][0] = Cost[0][0]
DP[1][1] = Cost[0][1]
DP[1][2] = Cost[0][2]

for i in range(2, N + 1):
    DP[i][0] = min(DP[i-1][1],DP[i-1][2]) + Cost[i-1][0]
    DP[i][1] = min(DP[i-1][0],DP[i-1][2]) + Cost[i-1][1]
    DP[i][2] = min(DP[i-1][0],DP[i-1][1]) + Cost[i-1][2]
    
print(min(DP[N][0],DP[N][1],DP[N][2]))