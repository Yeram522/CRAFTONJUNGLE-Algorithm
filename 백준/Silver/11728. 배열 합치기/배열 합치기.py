import sys
input = sys.stdin.readline

a, b  = map(int, input().split())  # 집합의 원소 개수들

# input
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 

result = list()
i = 0
j = 0

# while(i != a or j != b):     # index가 둘다 유효하지 않을 경우
while(len(result) < a + b):
    if(i == a and j < b): # i가 유효하지 않을 경우
        result.append(B[j])
        j += 1
        continue
    elif(j == b and i < a):  # j가 유효하지 않을 경우
        result.append(A[i])
        i += 1
        continue
      
    # index가 둘다 유효하지 않을 경우
    # index가 둘다 유효할 경우
    if(A[i] < B[j]):
        result.append(A[i])
        i += 1
    else:
        result.append(B[j])
        j += 1
        
print(*result)