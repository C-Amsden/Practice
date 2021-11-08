'''def NameandAge(name,age):
    print(name+",","Age: ",age)

NameandAge("Bobby",25)'''

#Multiple variables *args

'''def func1(*n):
    for i in n:
        print(i)

func1(20,40,60)
func1(80,100)'''

'''def calculation(a,b):
    n1 = a + b
    n2 = a - b
    return n1, n2

res = calculation(40,10)

print(res)'''

#specific values

'''def showEmployee(name,salary=9000):
    print( name, salary)
showEmployee("Ben", 90000)
showEmployee("Ben")'''

'''def summation(n):
    x= 0
    for i in range(0,n+1):
        x += i
    print(x)

summation(30)
summation(0)'''

# calling a defination something new

'''mathNext = summation
mathNext(30)'''


'''def EvenBetweenList(n1,n2):
    Even=[]
    for x in range(n1+2,n2,2):
        Even.append(x)
    print(Even)

EvenBetweenList(4,30)'''
#other way
'''def EvenBetterBetweenList():
    print(list( range(4, 30, 2)))'''

'''EvenBetterBetweenList()

def OddBetweenList(n1,n2):
    Odd=[]
    for x in range(n1+1,n2,2):
        Odd.append(x)
    print(Odd)

OddBetweenList(4,30)'''


alist = [4,6,8,24,12,2]

print(max(alist))

