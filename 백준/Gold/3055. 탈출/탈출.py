import sys
from collections import deque

input = sys.stdin.readline

# 입력
R, C = map(int, input().split())
Map = [list(input().rstrip()) for _ in range(R)]

# 방향 배열
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 큐와 방문 배열 초기화
dochi_queue = deque()
water_queue = deque()
visited = [[-1 for _ in range(C)] for _ in range(R)]  # 고슴도치 방문 배열
water_visited = [[-1 for _ in range(C)] for _ in range(R)]  # 물 방문 배열

def BFS():
    # 물의 위치 먼저 확장
    while water_queue:
        wx, wy = water_queue.popleft()
        for d in range(4):
            nwx = wx + dx[d]
            nwy = wy + dy[d]
            if 0 <= nwx < R and 0 <= nwy < C and Map[nwx][nwy] == '.' and water_visited[nwx][nwy] == -1:
                water_visited[nwx][nwy] = water_visited[wx][wy] + 1
                water_queue.append((nwx, nwy))
    
    # 고슴도치 이동
    while dochi_queue:
        x, y = dochi_queue.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx < 0 or ny < 0 or nx >= R or ny >= C:
                continue
            if Map[nx][ny] == 'D':  # 비버의 굴에 도착
                return str(visited[x][y] + 1)
            if Map[nx][ny] == '.' and visited[nx][ny] == -1:
                if water_visited[nx][ny] == -1 or visited[x][y] + 1 < water_visited[nx][ny]:
                    visited[nx][ny] = visited[x][y] + 1
                    dochi_queue.append((nx, ny))
    
    return "KAKTUS"

# 고슴도치와 물의 위치를 큐에 저장
for i in range(R):
    for j in range(C):
        if Map[i][j] == 'S':
            dochi_queue.append((i, j))
            visited[i][j] = 0
        elif Map[i][j] == '*':
            water_queue.append((i, j))
            water_visited[i][j] = 0

print(BFS())