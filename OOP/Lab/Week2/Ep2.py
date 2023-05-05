
def count_chardef_in_string(x,c):
    count = [sum([ 1 for ch in row if ch == c])
        for row in x ]
    return count
    # print(count)

c = "b"
x = ["aabba","aabd"]
print(count_chardef_in_string(x,c))
