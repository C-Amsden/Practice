'''aTuple = (10,20,30,40,50)
aTuple = aTuple[::-1]
print(aTuple)'''

"""aTuple = ("Orange", [10,20,30], (5,15,25))
print(aTuple[0][5])"""

'''aTuple = (50)
print(aTuple)'''

'''aTuple = (10,20,30,40)

a,b,c,d = aTuple

list0 = [a,b,c,d]

for x in range(0,4):
    print(list0[x])'''

'''tuple1 = (11,22)
tuple2 = (99,88)

tupleA = ( tuple1, tuple2)

tuple1 = tupleA[1]
tuple2 = tupleA[0]
print( tuple1,tuple2)'''
#my way
'''tuple1 = (11,22,33,44,55,66)

tuple2 = ( tuple1[3],tuple1[4])

print("tuple2 = ", tuple2)'''
#other way
'''tuple1 = (11, 22, 33, 44, 55, 66)
tuple2 = tuple1[3:-1]
print(tuple2)'''

'''tuple1 = (11,[22,33],44,55)

tuple1[1][0]= 222

print(tuple1)'''
# I didn't know this one
'''tuple1 = (('a',23),('b',37),('c',11),('d',29))

tuple1 = tuple(sorted(list(tuple1), key= lambda x: x[1]))

print(tuple1)'''

'''tuple1 =(50,10,60,70,50)

print(tuple1.count(50))'''
# Mine
'''tuple1 = (45,45,45,45)'''

'''if tuple1[0]==tuple1[1]==tuple1[2]==tuple1[3]:
    print (True)
else:
    print(False)'''
#optimized
'''tuple1 = (45,45,45,45)

print (all(i==tuple1[0]for i in tuple1))'''



for i in range(1,11):
    for x in range(1,11):
        print(i*x, end=" ")
    print("\n")



