import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))
DP = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if(arr[i] < arr[j]):
            DP[i] = max(DP[i], DP[j] + 1)
            
            
print(max(DP))