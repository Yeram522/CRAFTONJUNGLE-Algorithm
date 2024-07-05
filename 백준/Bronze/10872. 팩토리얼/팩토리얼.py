n = int(input())

def factorial(a):
    if a == 0:
        return 1
    elif a > 0:
        return a * factorial(a-1)
    else:
        raise ValueError("음수에 대한 팩토리얼은 정의되지 않습니다.")

try:
    print(factorial(n))
except ValueError as e:
    print(e)