# 11047
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = list()


for i in range(N):
    coin = int(input())
    coins.append(coin)


result = 0  # 동전 최소 값
for i in range(len(coins)-1, -1, -1):
    # 동전이 만들어야하는 값K 보다 크면
    if coins[i] > K:
        continue
   
    # K보다 coin값이 작다면 해당 코인으로 값을 나눈당.
    if K // coins[i]  > 0: #0 이상이면 나눠지는 것
        res = K // coins[i]  # 몇개로 나누었는지
        result += res
        K -= res*coins[i]  #실제로 소모된 값 빼주기


print(result)
