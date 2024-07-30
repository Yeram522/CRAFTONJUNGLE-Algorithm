import sys
input = sys.stdin.readline

#n 5<=n<=40

n = int(input())

fibcount = 0

def fib(n):
    global fibcount
    if(n == 1 or n == 2):
        fibcount += 1
        return 1
    
    
    return fib(n-1) + fib(n-2)

f = [0 for _ in range(43)]

f[1] = 1
f[2] = 1
fibonaccicount = 0
def fibonacci(n):
    global f
    global fibonaccicount
        
    for i in range(3, n+1):
        fibonaccicount += 1
        f[i] = f[i-1] + f[i-2]
        
    return f[n]

fib(n)
print(fibcount, end = " ")

fibonacci(n)
print(fibonaccicount)