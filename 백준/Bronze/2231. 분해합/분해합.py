N = int(input().strip())

if N < 1 or N > 1000000:  # 문제의 제한사항 체크
    exit()

def get_digit_sum(n):
    digit_sum = n
    while n > 0:
        digit_sum += n % 10
        n //= 10
    return digit_sum

result = 0
for i in range(max(1, N-54), N):  # 탐색 범위 최적화
    if get_digit_sum(i) == N:
        result = i
        break

print(result)