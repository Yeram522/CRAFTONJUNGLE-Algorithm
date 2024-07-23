import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    # Test Case
    N = int(input())
    avg = (N+1)//2
    result = 0
    score = list()
    for i in range(N):
        a, b = map(int, input().split())
        score.append([a,b])

    # sort
    score.sort()
    #print(score)
    a_max = score[0][0]
    b_max = score[0][1]
    result += 1
    for s in score:
        # a비교
        if a_max > s[0] or b_max > s[1]: # 면접과 시험중 둘중 하나라도 그 전사람들의 최고 등수보다 좋으면
            # 최고 등수를 갱신 해주고 값을 증가 시킨다.
            a_max = min(a_max, s[0])
            b_max = min(b_max, s[1])
            result += 1

    print(result)
