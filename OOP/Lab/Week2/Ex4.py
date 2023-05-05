def count_minus(str):
    numl = [int(i) for i in str .split()]
    total = sum([1 for i in numl if i<=-1])
    print(total)
count_minus("1 2 9 -1 2 -2")