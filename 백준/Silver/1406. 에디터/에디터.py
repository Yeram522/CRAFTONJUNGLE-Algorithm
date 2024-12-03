import sys
input = sys.stdin.readline

s1 = list(input())  # stack 1
s1.pop() # '\n' 제거
count = int(input())

s2 = list() # stack 2 (sub)


while(count > 0):
    command = input().split()
    ch = command[1] if len(command) > 1 else None
    command = command[0]
    
    if(command == 'L'):
        # 커서가 문장의 맨 앞이면 무시됨 -> s1 이 비어있을 경우
        if(len(s1) == 0) : 
            count -= 1
            continue
        temp = s1.pop()
        s2.append(temp)
    elif(command == 'D'):
        # 커서가 문장의 맨 뒤이면 무시됨 -> s2 가 비어있을 경우
        if(len(s2) == 0) : 
            count -= 1 
            continue
        temp = s2.pop()
        s1.append(temp)
    elif(command == 'B'):
        # 커서가 문장의 맨 앞이면 무시됨 -> s1 이 비어있을 경우
        if(len(s1) == 0) : 
            count -= 1 
            continue
        s1.pop()
    elif(command == 'P'):
        s1.append(ch)
        
    count -= 1
        
    
        
        
# 문자열 합치기
while(len(s2) > 0):
    temp = s2.pop()
    s1.append(temp)
    
print(*s1, sep='')
    
