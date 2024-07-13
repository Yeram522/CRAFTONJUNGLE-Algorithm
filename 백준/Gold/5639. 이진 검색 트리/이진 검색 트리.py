import sys
input=sys.stdin.readline # input함수 바꾸기
sys.setrecursionlimit(15000) # 10^8 까지 늘림.
# BST
node = list()
        
        
def post_order_print(start, end):
    if start >= end: # 오른쪽 노드가 없을 경우
        return
    
    root = node[start] #root의 노드 번호
    delim = start + 1 #왼오 가 갈리는 인덱스
    
    while delim<end: #인덱스 벗어남녀안되ㅣ니까아
        if root < node[delim]: break #루트보다 큰 친구가 나올때까지 검색
        delim+=1 #delim의 값을 업해주면서 찾음
        
    #while문 빠져나오면~ 루트보다 커졌을때의 index가 delim = 즉 오른쪽 서브트리의 루트를 찾은 것
    post_order_print(start+1, delim)# 왼쪽 서브트리의 루트~ 왼쪽 노드의 마지막 인덱스
    post_order_print(delim, end) #오른쪽노드의 루트~ 끝
    
    print(root) #루트 프린트
         
while True:
    try:
        new_node = int(input())
        node.append(new_node)
    except:
        break
    
post_order_print(0, len(node))