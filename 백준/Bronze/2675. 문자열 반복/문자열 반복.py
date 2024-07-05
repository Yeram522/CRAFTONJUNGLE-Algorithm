roop = int(input())
result = list()

for r in range(roop):
    a, b = input().split()
    string = str()
    for i in range(len(b)):
        string += b[i]*int(a)
        
    result.append(string) 
for k in result:
    print(k)
        
        
        
    