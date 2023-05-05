a = input("")
num = a.split()
indexZ  = []
numN = []

for i in range(len(num)):
    num[i] = int(num[i])

print(num)

for i in range(len(num)):
    
    if num [i] == 0:
        indexZ.append(i)
    else:
        numN.append(num[i])

numN.sort()

for i in range(len(indexZ)):
    numN.insert(indexZ[i],0)


print(numN)

for i in range(len(numN)):
    print(numN[i],end="")
    
# num.sort()

# # for k in range(len(indexx)):
# #     num.insert(0,k)

# # print(num)
# # a = [3,8,1,3,3]
# # a.remove(0)

# # a.sort()

# # #a.insert(1,0)  
# # print(a)

# lis = [1,20,0,0,12,12]
# lis.remove(0)
# print(lis)