# 큐
import sys
input=sys.stdin.readline # input함수 바꾸기

stack = [None]*2000003
front = 0 #원소 pop할떄
rear = 0 # 원소 push 할때

def empty() -> int:
    return 1 if front == rear  else 0

def push(x : int):
    global rear
    stack[rear] = x
    rear += 1
    
    
def pop():
    if empty(): return -1
    global front
    
    elemet = stack[front]
    
    front += 1

    return elemet
    
def fron():
    global front
    if empty(): return -1
    
    return stack[front]

def size() -> int:
    global front,rear
    
    return rear - front


def back() -> int:
    global rear
    if empty()==1: return -1
    return stack[rear-1]


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
        
        if command[0] == 'front':
            print(fron())
            continue
        
        if command[0] == 'back':
            print(back())
            continue