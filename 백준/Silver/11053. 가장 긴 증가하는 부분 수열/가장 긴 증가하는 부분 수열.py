import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

DP = [1] * N  # 모든 원소의 최소 길이는 1

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]:
            DP[i] = max(DP[i], DP[j] + 1)

print(max(DP))