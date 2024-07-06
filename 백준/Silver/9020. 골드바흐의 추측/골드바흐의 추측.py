# 조건
# 1. 주어진 N은 2보다 큰 짝수이다.
# 2. 두 소수의 합 = N
# 3. 두 소수의 차이가 가장 작은 쌍

def isPrime(a : int) -> bool :
    if ( a == 1 ) : False

    for i in range(2, 10001):
        if( i*i > a ) : break
        if( a%i == 0 ) : return False

    return True

pbCount = int(input())

for n in range(pbCount):
    N = int(input())
    a = N//2
    b = N//2

    while(True):
        if(isPrime(a) and isPrime(b)) :
            print(a,b)
            break

        a -= 1
        b += 1

