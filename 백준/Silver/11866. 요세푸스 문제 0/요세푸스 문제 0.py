import sys
import collections
input=sys.stdin.readline # input함수 바꾸기

size, gap = map(int, input().split())
q = collections.deque()
for i in range(1,size+1):
    q.append(i)
    
result = list()

i = 0

while(len(result) < size):
    
    #만약 index가 length의 끝까지 도달하면.
    if( i == gap ):
        i = 0
    
    if(i%gap == gap-1):
        #gap의 배수 index일때는 pop하고 result에 넣는다.
        tmp = q.popleft()

        result.append(tmp)
        
    else: 
        #나머지는 pop하고 다시 q에 넣는다.
        tmp = q.popleft()
        q.append(tmp)
        
    i+=1
    
    
    
#print

for idx in range(size):
    if size == 1:
        print(f'<1>')
        break
    
    if idx==0:
        print('<', end='')
        print(result[idx], end=', ')
    elif idx== (size-1):
        print(result[idx], end='>')
    else:
        print(result[idx], end=', ')