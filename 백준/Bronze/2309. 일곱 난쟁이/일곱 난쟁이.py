


def find():
    smalls = list()
    
    for i in range(9):
        height = int(input())
        smalls.append(height)

    
    for i in range(9):
        for j in range(i+1, 9):
            odd = smalls[i] + smalls[j]
            if sum(smalls) - odd == 100:
                if i > j : i , j = j , i
                
                smalls.pop(j)
                smalls.pop(i)
                return smalls
            
            
    return smalls

    


for s in sorted(find()) :
    print(s)
                
