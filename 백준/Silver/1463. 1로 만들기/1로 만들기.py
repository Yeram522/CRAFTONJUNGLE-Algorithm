import sys
N = int(input())

DP = [0 for _ in range(N+1)]

if(N > 1):
    for i in range(2,N+1):    
        DP[i] = 1 + min(DP[i//3]  if i%3 == 0 else 1e9 , DP[i//2] if i%2 == 0 else 1e9, DP[i-1]) 
    
    
print(DP[N])