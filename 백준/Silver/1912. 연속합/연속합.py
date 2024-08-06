import sys
import copy
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
DP = copy.deepcopy(arr)
for i in range(1, N):
    DP[i] = max(DP[i]+DP[i-1], arr[i])

  
#result
print(max(DP))



#LOG
"""
1. 시간초과
- 원인 : O(n^2)    

2. 메모리 초과
- DP 2차원 배열 사용( 낭비하는 ㅁㅔ머리 많음)

3. 시간초과
- while 종료 조건을 추가해야한다 생각했는데
- stack에 넣는 것들을 최대한 줄이자~
- stack에 넣을 때 st+1, ed-1 를 append하는거는 어차피 st+1 한번 ed-1 한번하는것과 같기때문에 중복이된다.
- stack에 넣기전에 st,ed의 크기 조건을 비교한 뒤 넣어준다.
- 현재 상태로 while이 몇번 도는지 확인했더니 511번 돈다,ㅋㅋ

4. 굳이 stack 쓸필요 없이 DP하나로 순회하면서 가능
"""
    
