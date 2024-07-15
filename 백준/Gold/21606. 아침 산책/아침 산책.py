import sys
from collections import defaultdict
input=sys.stdin.readline # input함수 바꾸기

V = int(input())
place = list(input().replace("\n", "")) # arry list의 생성자에 문자열을 넣으면 단일 문자로 구분된 배열을 반환한다.
#입출력 참고
"""https://dreamjy.tistory.com/105"""

Tree = {i: [] for i in range(1, V+1)}

# 트리이므로 간선은 무조건 V-1이다
for i in range(V-1):
    u, v = map(int, input().split())
    
    Tree[u].append(v)
    Tree[v].append(u)
 
def DFS(start):
    count = 0
    stack = [start] # 스택을 이용한 DFS

    while stack:
        node = stack.pop() # 해당 지점과 이어진 노드들 리스트
        for next in Tree[node]:
            if place[next-1] == "0": # 실외일 경우
                stack.append(next)
            else: # 실내일 경우에는 해당 루트의 산책을 종료한다.
                #같은게 나올수있나?
                if(next == start): continue
                count+=1
                #print(start, next)
                
    
    return count


# 시작점과 끝점을 정해야한다. start와 end가 정해지면 경로는 유일.
# for문으로 시작점을 먼저 정해서 시작하면 중복이 일어나지 않음!
result = 0
for vertex in Tree.keys():# 실내인 경우에만 start지점에 포함한다.
    if place[vertex-1] == "1":
        result += DFS(vertex)
        
        
print(result)
        