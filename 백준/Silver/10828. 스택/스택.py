# 스택 
import sys
input=sys.stdin.readline # input함수 바꾸기

stack = [None]*10003 

pos = -1

def empty() -> int:
    return 1 if pos < 0 else 0

def push(x : int):
    global pos
    pos += 1
    stack[pos] = x
    
    
def pop():
    if empty(): return -1
    global pos
    tmp = stack[pos]
    stack[pos] = None
    pos -= 1
    
    return tmp
    
    
def size() -> int:
    global pos
    return pos+1


def top() -> int:
    global pos
    if empty()==1: return -1
    return stack[pos]


if __name__ == '__main__':
    N = int(input()) 
    
    # input roop
    for i in range(N):
        command = sys.stdin.readline().strip().split()
        
        #print(command)
        if command[0] == 'push':
            push(int(command[1]))
            continue
        
        if command[0] == 'pop':
            print(pop())
            continue
        
        if command[0] == 'size':
            print(size())
            continue
        
        if command[0] == 'empty':
            print(empty())
            continue
        
        if command[0] == 'top':
            print(top())
            continue