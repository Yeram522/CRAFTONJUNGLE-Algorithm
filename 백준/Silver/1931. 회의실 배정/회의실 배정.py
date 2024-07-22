import sys
input = sys.stdin.readline
origin = []
N = int(input())
# 1. 입력 및 시작 시간이 같은 회의 시간은 배제
maxtime = 0
for i in range(N):
    s,e = map(int,input().split())
    origin.append([s,e])
# 2. 종료시간이 가장 이른 순으로 정렬
origin.sort(key=lambda  x:(x[1],x[0])) # 이차원 배열 0번째 인덱스를 이용한 정렬
# 3. 시간을 안 겹치게 짜면서 최대 회의 개수를 구한다.
time = origin[0]
count = 1
for i in range(1,N):
    if time[1] <= origin[i][0]: # 회의끝난시간 보다 크거나 같은 시간에 시작 하는 회의 찾기.
        count += 1
        time = origin[i] # 다음 타임 넘겨주기

print(count)



