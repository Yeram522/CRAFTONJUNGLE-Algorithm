
n = int(input())

def hanoi( n : int, a : int, b: int):
    if( n > 20 ) : return
    if( n == 1 ) :
        print(a,b)
    
        return 

    hanoi(n - 1, a, 6-a-b)

    print(a,b)

    hanoi(n - 1, 6-a-b,b)

    
print(2**n - 1)
hanoi(n, 1, 3)