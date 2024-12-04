import sys
from collections import deque  # deque 사용

input = sys.stdin.readline
q1 = deque(input().strip())
target = input().strip()
stack = []
t_len = len(target)

result = []
while q1:
    result.append(q1.popleft())  # O(1) 연산
    
    # result의 길이가 target보다 길 때만 검사
    if len(result) >= t_len:
        # 마지막 t_len개의 문자가 target과 같은지 검사
        if ''.join(result[-t_len:]) == target:
            # target 길이만큼 제거
            del result[-t_len:]

print('FRULA' if not result else ''.join(result))