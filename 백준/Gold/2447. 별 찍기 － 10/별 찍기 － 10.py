import sys
input = sys.stdin.readline

N = int(input())
result = [[' ' for _ in range(N)] for _ in range(N)]

def print_star(n, x, y):
    if n == 1:
        result[x][y] = '*'
        return
        
    size = n//3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            print_star(size, x + i*size, y + j*size)

print_star(N, 0, 0)
for row in result:
    print(''.join(row))