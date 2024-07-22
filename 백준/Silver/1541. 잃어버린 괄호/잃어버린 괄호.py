import sys
import re
input = sys.stdin.readline

#input
iexp = input().rstrip() # string으로 입력 받는다. 나중에 쓸 때 int로 형변환하기!

exp = re.split(r'(\-|\+)',iexp)


#print(exp)
# min value exp
prev = 0

esum = list()
for e in range(0, len(exp)): #+묶음들을 좍 묶고 마이너스로 뺸다.
    if exp[e] == '+':
        prev += int(exp[e-1])
        continue
    elif exp[e] == '-':
        if prev == 0:
            esum.append(int(exp[e-1]))
        else:
            esum.append(prev+int(exp[e-1]))
            prev = 0

# 리스트 마지막 숫자 계산 처리.
if prev != 0:
    if exp[len(exp)-2] == '+':
        esum.append(prev+int(exp[len(exp)-1]))
    else:
        esum.append(prev)
        esum.append(int(exp[len(exp)-1]))
else:
    esum.append(int(exp[len(exp) - 1]))

# 모든 아이들을 빼준단.
result = esum[0]
for i in range(1, len(esum)):
    result -= esum[i]


print(result)