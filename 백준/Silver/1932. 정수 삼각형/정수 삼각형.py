import sys
input = sys.stdin.readline

N = int(input()) # size of triangle

arr = list()
DP = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    line = list(map(int, input().split()))
    
    arr.append(line)

DP[0][0] = arr[0][0]
level = 0
while(level < N-1):
    for i in range(0,len(arr[level])): #7
        DP[level+1][i] = max(DP[level+1][i], DP[level][i] + arr[level+1][i])
        DP[level+1][i+1] = max(DP[level+1][i+1], DP[level][i] + arr[level+1][i+1])
        
    
    level += 1
    
print(max(DP[level]))
        