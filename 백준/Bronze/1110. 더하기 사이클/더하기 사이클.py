import sys
import collections
input=sys.stdin.readline # input함수 바꾸기

N = int(input())

q = collections.deque()

new_num = N
cnt = 0

if(new_num <= 9): # 스택에 수 저장하기.
        q.append(0)
else:
    q.append(new_num//10)
        
q.append(new_num%10)
    
# 새로운 수 큐에 저장.
while(True):
    if(new_num == N and cnt >=1) : break#새로운 수 만들기.
    
    #각자리수 더하기
    sum = q.popleft() + q[0]
    q.append(sum%10)
        
    new_num = q[0]*10 + q[1]
         
    cnt += 1
    
print(cnt)