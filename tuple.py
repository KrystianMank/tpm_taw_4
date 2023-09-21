'''
Tuple-immutable!
Krotki
'''
# moja_tupla=(2,3,4,5)
# inna_tupla=(1,)

# print(type(moja_tupla))
# print(type(inna_tupla))

# #moja_tupla.append(2) - nie zadziała

# moja_tupla=moja_tupla+(6,)
# print(moja_tupla)

# print(moja_tupla[1])

#=========================================

# x, y, _= 3, 4, 5
# print(x)
# print(y)

# #flip/flop
# x,y=y,x
# print(x)
# print(y)

#wersja1
# tuple=(4,3,7,1)
# tuple=list(tuple)
# tuple.sort()
# print(tuple)

#wersja2
tupla=(4,3,7,1)
print(tuple(sorted(list(tupla),reverse=False)))


