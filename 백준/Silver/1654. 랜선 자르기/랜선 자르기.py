import sys
input = sys.stdin.readline

K , N = map(int, input().split())

wires = [int(input()) for _ in range(K)]

def cut_wires(cut_len : int ):
    count = 0 # 몇개 만들었는지 카운트
    
    for wire in wires:
        count += wire // cut_len  # while문 대신 나눗셈 사용
        if count >= N:  # 일찍 종료 가능
            return True
    return False



# 이분 탐색
start = 1
end = max(wires)
result = end

while(start <=  end):
    mid = (start + end ) // 2
    
    if(cut_wires(mid)):
        #최대 길이를 구해야하므로
        result = mid
        start = mid + 1
    else: 
        end = mid - 1
            
    
print(result)
            
                
            
                