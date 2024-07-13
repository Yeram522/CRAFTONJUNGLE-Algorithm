import sys
input=sys.stdin.readline # input함수 바꾸기

# union find algorithm
def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
        
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    
#input
V , E = map(int, input().split())
parent = [0]*(V+1) #부모 테이블 초기화 하기

edges = []
result = 0

for i in range(1, V + 1):
	parent[i] = i
 
#Vertex imfo
for i in range(E):
    A, B, C = map( int, input().split() ) #  각 간선에 대한 정보
    # A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어있다. C는 음수일 수 있다.
    # 가중치를 오름차순으로 정렬해야되기 때문에 첫 원소를 비용으로 둠!!
    edges.append((C, A, B))
    
# 비용을 오름차순으로 정렬!!!!!!
edges.sort()

for edge in edges:
    cost, a, b = edge
    
    if find_parent(parent, a) != find_parent(parent,b):
        union(parent, a, b)
        result += cost
        
#ouput
#최소 스패닝 트리의 가중치를 출력.
print(result)
    