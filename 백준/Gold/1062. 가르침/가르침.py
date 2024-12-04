import sys
from itertools import combinations  # combinations 사용

input = sys.stdin.readline
N, K = map(int, input().split())

if K < 5:  # antic 필수
    print(0)
    exit()
    
# 기본 단어 세팅    
basic = {'a', 'n', 't', 'i', 'c'}
if K == 26:  # 모든 알파벳을 다 배울 수 있는 경우
    print(N)
    exit()
    
# 단어 입력 받기
words = []
candidates = set()
for _ in range(N):
    word = set(input().rstrip()) - basic  # antic 제외한 나머지 문자들
    if len(word) <= K-5:  # 배울 수 있는 문자 수보다 적거나 같으면
        words.append(word)
        candidates |= word  # 후보 문자들 추가

if len(candidates) <= K-5:  # 모든 단어를 다 배울 수 있는 경우
    print(len(words))
    exit()

result = 0
# 가능한 모든 조합에 대해
for teach in combinations(candidates, K-5):
    teach = set(teach) | basic
    count = sum(1 for word in words if word <= teach)  # 배울 수 있는 단어 수
    result = max(result, count)

print(result)