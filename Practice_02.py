#number triangle
'''start = 0

for x in range(1,11):
    for j in range(1,x+1):
        print( j, end=" ")
        
    print(" ")
'''# Summation of numbers
'''n = int(input("give number"))
t = 0
for x in range(0,n+1,1):
    t += x
print(t)
'''#multiplication Table
'''num = 2
for x in range(0, 11):
    print(x*num, end =" ")'''

'''list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]

for x in list1:
    if x > 150:
        break
    if x%5==0:
        print(x)'''
#digit counting
'''
num =75869
x = 0
while num > 0:
    num = num//10
    x += 1

print(x)'''
# Upside down triangle sequncial order
'''for x in range(0,6,1):
    for j in range(5-x,0,-1):
        print(j, end=' ')
    print(" ")'''
#reverse order in list
'''
list1 = [10,20,30,40,50]

for x in range(len(list1)-1,-1,-1):
    print(list1[x])'''
#negative ordering
'''
for x in range(-10,0,1):
    print(x)
'''

'''x = 4
while x >0:
    for i in range(5):
        print(i)
        x -= 1
        
print("done")
# other way???!!

for i in range(5):
    print(i)
else:
    print("done")'''
#prime numbers
'''
for x in range( 0, 500):
    if x > 1:
        for j in range(2, x):
            if (x%j) ==0:
                break
        else:
            print(x)
'''
'''n=1
for x in range(1, 6):
    n = n*(x)
print(n)'''

'''num = 76542
reverse = 0
while num > 0:
    r = num%10
    reverse = (reverse*10)+r
    num = num//10
print(reverse)'''

'''list0 = [10,20,30,40,50,60,70,80,90,100]

for x in range(1, len(list0)+1, 2):
    print(list0[x],end=" ")'''

# other way
'''my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for i in my_list[1::2]:
    print(i, end=" ")'''
