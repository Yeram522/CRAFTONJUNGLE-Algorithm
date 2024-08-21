import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split(' ')))

DP = [0 for _ in range(N)]

def binary_search(left, right, key):
    global DP
    mid = 0
    while(left < right):
        mid = int((left + right)/2)
        if(DP[mid] < key):
            left = mid + 1
        else:
            right = mid
            
    return right


last_num = 0
len = 1
DP[last_num] = arr[0]
for i in range(1, N):
    if DP[last_num] < arr[i]:
        len += 1
        last_num+=1
        DP[last_num] = arr[i]
    else:
        idx = binary_search(0,len, arr[i])
        DP[idx] = arr[i]
            
print(len)