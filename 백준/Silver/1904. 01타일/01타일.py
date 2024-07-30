import sys
input = sys.stdin.readline

N = int(input())
#첫 번째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)
T = [0 for _ in range(N+5)]

T[1] = 1
T[2] = 2

for i in range(3, N+1):
    T[i] = (T[i-1]+T[i-2])%15746
    #print(f'T[{i}]= {T[i]}')
    
    
    
print(T[N]%15746)