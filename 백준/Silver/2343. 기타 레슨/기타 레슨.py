import sys


input = sys.stdin.readline

N,M = map(int, input().split())

S = list(map(int, input().split()))


start = max(S) # 강의 길이가 가장 긴 값
end = sum(S) # 모든 강의 길이의 합

result = end

def can_divide(max_sum : int):
    count = 1
    current_sum = 0
    
    for lecture in S:
        if(lecture > max_sum):
            return False
        
        if current_sum + lecture > max_sum:
            count += 1
            current_sum = lecture
        else:
            current_sum += lecture
            
    return count <= M

while start <= end:
    mid = (start + end ) // 2
    
    if can_divide(mid):
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        

print(result)
        