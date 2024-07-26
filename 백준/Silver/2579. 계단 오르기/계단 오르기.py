import sys
input = sys.stdin.readline

N = int(input())
arr = list()
for _ in range(N):
    arr.append(int(input()))
DP = [0] * (N+1)


DP[1] = arr[0]
if N >=2:
    DP[2] = DP[1] + arr[1]

for i in range(3, N+1):
    DP[i] = max(DP[i-2] + arr[i-1], DP[i-3]+ arr[i-1]+ arr[i-2])
    
print(DP[N])

