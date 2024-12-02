import sys
input = sys.stdin.readline

a, b  = map(int, input().split())  # 집합의 원소 개수들

# input
A = list(map(int, input().split())) 
B = list(map(int, input().split())) 

temp = list()

# for i in A:
#   if i in B:
#     temp.append(i) # B에 A의 원소가 있다면 temp list에 추가한다.

set_B = set(B)
temp = [i for i in A if i in set_B]

print((a+ b) - 2*(len(temp)))