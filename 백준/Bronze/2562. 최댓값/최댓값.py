# 9개의 서로 다른 자연수
max = 0
cnt = 0

for i in range(0,9):
    num = int(input())
    if max >= num:
        continue
    max = num
    cnt = i
    
print(max)
print(cnt+1)