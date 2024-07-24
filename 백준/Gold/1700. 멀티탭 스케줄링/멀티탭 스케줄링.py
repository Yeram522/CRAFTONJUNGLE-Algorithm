import sys
import heapq
input = sys.stdin.readline

N, K = map(int, input().split())
# N : 멀티탭 구멍의 개수, K = 전기 용품 총 사용 횟수

schedule = list(map(int, input().split()))
# 전기용품의 이름이 k이하의 자연수로 사용 순서대로 주어진다.



multi_tab = [] # always len(multi_tab) == N
result = 0
#Schedule 순회
for i in range(0, len(schedule)): # O(n)
    if schedule[i] in multi_tab: continue # 이미 콘센트에 있으면 안 뽑아도 되니까 그냥 지나친다.
    if len(multi_tab) == N: #콘센트 크기만큼 다 찼다면! 콘센트에있는 친구를 하나 빼준다
        latest = -1
        to_remove = -1
        for item in multi_tab:
            if item not in schedule[i:]:
                to_remove = item
                break
            else: # 앞으로도 사용될 경우 나아아중에 쓰는 애들을 구해야함
                next_use = schedule[i:].index(item)
                if next_use > latest:
                    latest = next_use
                    to_remove = item

        multi_tab.remove(to_remove)
        result += 1

    multi_tab.append(schedule[i])




print(result)