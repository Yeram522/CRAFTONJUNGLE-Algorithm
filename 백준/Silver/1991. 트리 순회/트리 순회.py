import sys
input=sys.stdin.readline # input함수 바꾸기

N = int(input()) # 영상 크기

tree = {}

# 전위순회
def preorder(node):
    if node != ".":
        print(node, end = "")
        preorder(tree[node][0])
        preorder(tree[node][1])
    
# 중위순회
def inorder(node):
    if node != ".":
        inorder(tree[node][0])
        print(node,end = "")
        inorder(tree[node][1])
        

# 후위순회
def postorder(node):
    if node != ".":
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node,end = "")


for n in range(N):
    p, l, r = map(str, input().split())
    
    tree[p] = (l, r)
    

preorder("A")  
print("\n",end = "")
inorder("A") 
print("\n",end = "")
postorder("A")
