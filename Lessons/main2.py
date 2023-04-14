a = {1,2,3,5,8}
b = {2,5,8,13,21}

q = a.union(b).difference(a.intersection(b))
print(q)