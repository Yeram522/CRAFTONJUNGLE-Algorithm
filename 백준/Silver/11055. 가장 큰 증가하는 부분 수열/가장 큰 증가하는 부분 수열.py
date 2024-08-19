import sys
import copy
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

DP = copy.deepcopy(arr)

for i in range(1, N):
    for j in range(i):
        if(arr[i] > arr[j]):
            DP[i] = max(DP[i], DP[j] + arr[i])
            
print(max(DP))