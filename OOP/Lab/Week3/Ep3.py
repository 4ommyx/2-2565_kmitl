lis = []
def is_plusone_dictionary(d):
    count = 0
    for i,j in d.items():
        lis.append(i)
        lis.append(j)
    print(lis)
    
    for c in range(len(lis)-1):
        if lis[c]+1 == lis[c+1]:
            count+=1
    if count == len(lis)-1:
        return True
    else:
        return False
        
d = {1:2,3:4}
is_plusone_dictionary(d)
