def add2list(lst1, lst2):
    ans =  [ lst1[i]+lst2[i] for i in range(len(lst1))]
    return ans

lst1 = [1,2]
lst2 = [3,4]
print(add2list(lst1,lst2))