import sys
input = sys.stdin.readline

N = int(input())



def Fibo(N):
    fibo = [0] * (N+1)
    fibo[0] = 1
    fibo[1] = 1
    
    if N <= 1: 
        return 1
    
    for n in range(2,N+1):
        fibo[n] = fibo[n-1] + fibo[n-2]
        
    return fibo[N-1]



print(Fibo(N))    