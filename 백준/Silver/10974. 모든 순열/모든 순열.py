import sys
from itertools import permutations  # permutations 사용
input = sys.stdin.readline

N = int(input())

nPr = permutations(range(1,N+1),N)

for numbers in nPr:
    print(*numbers, sep=" ")