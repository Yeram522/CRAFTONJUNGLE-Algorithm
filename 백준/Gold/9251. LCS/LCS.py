import sys
input = sys.stdin.readline

A = list(input().rstrip())
B = list(input().rstrip())

# LCS 배열을 B의 길이를 행으로, A의 길이를 열로 초기화
LCS = [[0 for _ in range(len(A)+1)] for _ in range(len(B)+1)]

for i in range(1, len(B)+1):
    for j in range(1, len(A)+1):
        if B[i-1] == A[j-1]:  # 같은 경우는 +1
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:  # 다를 경우 최대값 사용
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

print(LCS[len(B)][len(A)])