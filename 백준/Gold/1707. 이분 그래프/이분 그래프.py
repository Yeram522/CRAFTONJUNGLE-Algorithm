import sys
from collections import defaultdict
input=sys.stdin.readline # input함수 바꾸기

sys.setrecursionlimit(10**4) # 10^8 까지 늘림.

# 입력
# test case 개수
t_cnt = int(input())

def DFS(start,visited):
    stack = [start]
    visited[start] = 1 #설정한색으로 방문처리
    
    while stack: # 스택이 없을떄까지
        node = stack.pop()
        for next in Graph[node]:
            if visited[next] == 0: # 방문안한곳은 현재와 다른 색으로 칠해주고 이동
                visited[next] = - visited[node] # 반대색으로 설정
                stack.append(next)
            elif visited[next] == visited[node]: #연결되어잇는 노드인데 같은 색이라면?!?! 이분 그래프가 아니다.
                return False
            
    return True

# V, E
for cnt in range(t_cnt):
    V, E = map(int, input().split())
    # V 정점개수
    # E 간선개수
    
    # 그래프 초기화.
    Graph = defaultdict(list)
    visited = [0] * (V + 1)  # 0은 방문 X, 1과 2는 다른색이자 방문했다는 의미.
    result = True
    
    for n in range(E):
        u, v = map(int, input().split())
        
        Graph[u].append(v)
        Graph[v].append(u)
        
      
    for key in Graph.keys():
        if visited[key] == 0:
            # 근데 이미 result 가 false가 나오면 멈춰도 됨
            if not DFS(key,visited):
                result = False
                break

                     
    print("YES" if result else "NO")
        
# 반례 해결
# 1 . 그래프가 연결되어있따는 보장이 없기때문에 for문 돌려서전체 그래프 확인해야힘
# 2. defaultdic으로 딕셔너리 초기화 최적화
# 3. 재귀 말고 스택으로 바꿈

# 반례 모음
"""https://www.acmicpc.net/board/view/77198"""
        
        