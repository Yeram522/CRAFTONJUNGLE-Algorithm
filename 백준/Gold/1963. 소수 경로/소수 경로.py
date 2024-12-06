import sys
import math
input = sys.stdin.readline

# is_prime
def isPrime(N : int):
    for i in range(2, int(math.sqrt(N) + 1)):
        if(N % i == 0):
            return False
    return True

# DFS
def DFS(cur : int, end : int): # end의 value에 저장되는 수가 최단거리.
    queue = list()
    queue.append(cur)
    visited = dict() # dictionary
    visited[cur] = 0 
    
    if(cur == end):
        return 0
    
    while queue:
        cur = queue.pop(0)
        cur_str = str(cur)
        
        for i in range(4):  # 각 자릿수에 대해
            for j in range(10):  # 0~9 시도
                # 현재 자릿수 숫자와 같으면 건너뛰기
                if int(cur_str[i]) == j:
                    continue
            
                nCur = int(cur_str[:i] + str(j) + cur_str[i+1:])
                 # 1000 미만이면 건너뛰기
                if nCur < 1000:
                    continue
                    
                # 소수가 아니면 건너뛰기
                if not isPrime(nCur):
                    continue
                    
                # 방문하지 않았거나 더 짧은 경로를 찾은 경우
                if nCur not in visited or visited[cur] + 1 < visited[nCur]:
                    visited[nCur] = visited[cur] + 1
                    queue.append(nCur)
            

                    
    return visited.get(end, -1)
                    
testCase = int(input())

for test in range(testCase):
    start, end = map(int, input().split())
    result = DFS(start, end)
    print(result if result >= 0 else "Impossible")
    