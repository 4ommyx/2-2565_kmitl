lis = [[1, -3, 2], [-8, 5], [-1, -4, -3]]

def delete_minus(x):
  ans = [[numlis for numlis in row if numlis >=0] \
      for row in x] 
  return ans
print(delete_minus(lis))