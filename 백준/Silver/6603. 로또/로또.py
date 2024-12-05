import sys
from itertools import combinations

input = sys.stdin.readline

while(True):
    testCase = list(map(int, input().split()))
    K = testCase[0]
    if( K == 0 ) : break
    
    S = testCase[1:] # 2번째 원소부터 끝까지
    
    for case in combinations(S, 6):
        print(*case, sep=" ")
        
    print()
    
    
