'''
Sets
'''
# zb={8,2,3,4,2,3,4,2,3,4}
# print(zb)
# zb2=set()
# print(zb2)

# zb2.add(3)
# print(zb2)

# zb.remove(2)
# print(zb)
# if 2 in zb:
#     zb.remove(2)
# else:
#     print("Nie ma 2 w zbiorze")

# zb.discard(2) #nie wywołuje błedu gdy nie ma elamentu w zbiorze

# a={2,3,4}
# b={1,3,5}
# print(f"a: {a}, b: {b}")
# print(a.intersection(b)) #iloczyn zbiorów (częśc wspólna)\
# print(a.union(b)) #suma zbiorów 
# print(b.difference(a))
# print(a.difference(b)) #różnica zbiorow

listax=[2,3,4,3,4,5,6,7,8,8]
listax=list(set(listax))
print(listax)


