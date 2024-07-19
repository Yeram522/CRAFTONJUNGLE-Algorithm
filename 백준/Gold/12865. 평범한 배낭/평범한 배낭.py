import sys
input = sys.stdin.readline


# 물품의 수, 배낭의 최대 무게
N, K = map(int, input().split())

Weights = [0 for _ in range(N+1)]
Value =  [0 for _ in range(N+1)]

for i in range(1,N+1):
    W,V = map(int, input().split()) 
    
    Weights[i] = W
    Value[i] = V
  
# 가치합의 최댓값 구하기
results = [ [0 for _ in range(K+1)] for _ in range(N+1)] #2차원 배열에 경우에 따른 최대값을 저장해둔다.

for i in range(1,N+1):
    for w in range(1,K+1):
        if w - Weights[i] >= 0:
            # 그전 무게를 넣었을 때와 가치비교해서 높은 가치를 넣는다.
            results[i][w] = max(results[i-1][w],results[i-1][w-Weights[i]]+Value[i])  # 자리가 남으면 들어갈수잇는 가치가 높은 다른 물건을 넣는다.
        else:
            results[i][w] = results[i-1][w]
            
            
print(results[N][K])
    
# 문제를 잘못봐가지고 중복값이 있는줄알았다ㅠㅜㅠ 흑흑 드냥 다 배열로 해서 품