import sys
input = sys.stdin.readline

# 히든 넘버 
# 1. 연속된 숫자는 한 히든 넘버 fd23A -> 23!
# 2. 두 히든 넘버 사이에는 글자가 적어도 한개 있음!
# 3. 히든 넘버는 6자리를 넘지 않는다.

# Input
# 단어의 길이
N = int(input())
# 단어
Word = input()

#variable
res = 0 # result
powcnt = 0 # sequence numbers count

# reverse for
for i in range(N-1, -1, -1):
    if(Word[i].isalpha()):
        powcnt = 0
        continue
    
    res += int(Word[i]) * (10 ** powcnt)
    powcnt += 1
    
print(res)
    

