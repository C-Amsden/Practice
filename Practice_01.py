'''n1 = 20
n2 = 30
n3 = 40
n4 = n2

def calc(y,x):
    if x*y > 1000:
        return x+y
    else:
        return x*y


print( calc(n1,n2))
print( calc(n3,n4))'''


'''for i in range(0, 10):
    if i ==0:
        print ( i, i, i)
    else:
        print( i,(i-1), i + (i-1))


x = int(input("any number ="))
p = 0
for i in range(x):
    print( i, p, i+p)
    p = i'''

'''str = "pynative"

for i in range (0, len(str),2):
    print("index[",i,"]",str[i])

def removeChars(str,n):
    return str[n:]
print(removeChars(str,4))'''

'''def endsLogic(li):
    if li[0]==li[-1]:
        print( 'result is True')
    else:
        print( 'result is False')

list1 = [10,20,30,40,10]
list2 = [10,20,30,40,50]

endsLogic(list1)
endsLogic(list2)'''

'''list1 = [10,20,33,46,55]

def Dividebyn (li):
    n = int(input("input whole number ="))
    print("Given list is ",li)
    print("Divisible of ", n, " in the list")
    for i in li:
        if (i%n ==0):
            print (i)


Dividebyn(list1)'''

'''str = "Emma is good developer. Emma is a writer"

print( "Emma appeared ", str.count("Emma"), " times")'''

'''for i in range(0,6):
    for x in range(i):
        print(i, end="")
    print("\n")'''

# I didn't know this one
'''def reverseCheck(number):
    print("original number", number)
    originalNum = number
    reverseNum = 0
    while (number > 0):
        reminder = number % 10
        reverseNum = (reverseNum * 10) + reminder
        number = number // 10
    if (originalNum == reverseNum):
        return True
    else:
        return False

print("The original and reverse number is the same:", reverseCheck(121))'''

'''def revCheck(n):
    Sn = n
    Rn = 0
    while (n>0):
        remainder = n%10 # example 121%10 equals 1
        Rn = (Rn*10) + remainder # 0*10 +1 => 1
        n = n//10 # 121//10 is 12 then it loops
    if (Sn == Rn):
        return True
    else:
        return False

print(revCheck(33))'''

'''Flist = [10,20,23,11,17]
Slist = [13,43,24,36,12]

def oddToeven( li1,li2):
    Thirdlist =[]
    for i in li1:
        if (i%2 !=0):
            Thirdlist.append(i)
    for i in li2:
        if (i%2 ==0):
            Thirdlist.append(i)
    print(Thirdlist)

oddToeven( Flist,Slist)'''

'''def reverseNumber(n):
    while (n > 0):
       x = n%10 # gets last digit from number ex: 7536%10 = 6
       n= n//10 # removes last digit from number ex: 7536//10 = 753
       print(x, end=" ")
reverseNumber(7536)'''
#Yeah I got it
'''def IncomeTax(n):
    remaining = n - 20000
    Tax = 0
    if (n >= 20000):
        Tax = 10000.0*0.0 + 10000.0*(1.0/10.0)+ remaining*(1.0/5.0)
    elif (n <= 19999):
        Tax = 0
    else:
        Tax = 10000.0*0.0 + 10000.0*(1.0/10.0)
    print(Tax)

IncomeTax(20001)'''
#Upside down Triangle
for i in range(6,0,-1):
    for x in range(0,i-1,1):
        print(" ","*",end="")
    print("*")
    


    
    
        

      
    



