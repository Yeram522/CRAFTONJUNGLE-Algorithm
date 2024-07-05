# 1978 소수 찾기

num = int(input())

nums = map(int, input().split(' '))


def isPrime(a : int) -> bool:
    if( a == 1 ) : return False

    for n in range(2, 1001):
        if n * n > a : break
        if( a % n == 0 ) : return False

    return True


anw = 0
for n in nums:
    if(isPrime(n)) : anw += 1

print(anw)