import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

DP = [ 1 for _ in range(N) ]
prev = [-1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and DP[i] < DP[j] + 1:
            DP[i] = DP[j] + 1
            prev[i] = j
            
max_length = max(DP)
max_index = DP.index(max_length)

LIS = []
while max_index != -1:
    LIS.append(arr[max_index])
    max_index = prev[max_index]
    
LIS.reverse()

print(max_length)
print(*LIS)