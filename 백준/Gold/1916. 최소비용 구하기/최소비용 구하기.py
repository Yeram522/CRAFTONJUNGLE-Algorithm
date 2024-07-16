import sys
import heapq # 우선순위 큐 사용
input=sys.stdin.readline # input함수 바꾸기

# 도시의 개수
N = int(input())

# 버스의 개수
M = int(input())

# 연결 그래프 초기화!
Graph = { i : {} for i in range(1, N+1)}

# 버스 정보
# 출발도시번호 - 도착도시번호 - 버스 비용 
for i in range(M):
    start, end, cost = map(int, input().split())
    
    if end not in Graph[start] or cost < Graph[start][end]: ## 출발-도착은 같은데 비용이 다른것이 들어왓을때 둘중 작은걸로 해줌
        Graph[start][end] = cost
   
    
# 구해야할 것 입력.
start, end = map(int, input().split())

    
# 출발~도착 까지 최소 비용 = BFS
def dijkstra(start, end):
    # 무한대 값 정의 **************
    INF = float('inf')
    
    # 거리 리스트 초기화
    costs = [INF for _ in range(N+1)]
    costs[start] = 0 # 처음 위치는 0으로 초기화.
    
    # 우선순위 큐 초기화
    q = [(0, start)]
    
    
    while q:
        current_cost, node = heapq.heappop(q) # 우선순위 큐 pop

        # 이미 처리된 노드이면 continue
        if current_cost > costs[node]:
            continue
        
        for next_node, cost in Graph[node].items():
            new_cost = current_cost + cost
            
            # 더 짧은 경로 발견 시 갱신
            if new_cost < costs[next_node]:
                costs[next_node] = new_cost
                heapq.heappush(q, (new_cost, next_node))
           

             
    return costs[end]


print(dijkstra(start,end))

# Note
# 처음에는 단순히 BFS를 써서 최단거리르 계산하려고했는데, 간선마다 비용이 달라서, 하기가 쉽지않앗당
#그래서 다익스트라 알고리즘을 써봤느데, 잘 안되서 보니
# 우선순위큐를 안쓰고있엇다!이런!!