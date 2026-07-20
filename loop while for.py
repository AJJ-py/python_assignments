#1
n=int(input('num:'))
for i in range(1,n+1,1):
    print(i,end=' ')
print('\n')
#2
n=int(input('num:'))
a=n*2
for i in range(0,a+1,2):
    print(i,end=' ')
print('\n')
#3
n=int(input('num:'))
a=n*2
for i in range(1,a+1,2):
    print(i,end=' ')
print('\n')
#4
n=int(input('num:'))
a=n*3
for i in range(3,a+1,3):
    print(i,end=' ')
print('\n')
#5
n=int(input('num:'))
a=n*5
for i in range(5,a+1,5):
    print(i,end=' ')
print('\n')
#6
n=int(input())
for i in range(2,n,2):
    print(i,end=' ')
print('\n')
#7
n=int(input())
for i in range(1,n+1):
    if i%2==0 or i%3==0:
        print(i,end=' ')
    else:
        pass
print('\n')
#8
n=int(input())
for i in range(1,n+1):
    if i%2==0 or i%5==0 or i%7==0:
        print(i,end=' ')
    else:
        pass
print('\n')
#9
n=int(input())
i=1
c=0
while c<n:
    if i%3==0 or i%7==0 or i%5==0:
        c+=1
        print(i)
    i+=1
#10
n=int(input())
s=1
i=0
while i<=n:
    s+=n%10
    n=n//10
    i+=1
print(s)
#11
n=int(input())
i=1
while i<n:
    n=n//10
    i+=1
print(i)
#12 and #13
n=int(input())
c=0
for i in range(1,n+1,1):
    if n%i==0:
        print(i,end=' ')
        c+=1
    else:
        pass
print('\n',c)

#14
n=int(input())
c=0
for i in range(2,n,1):
    if n%i==0:
        c+=1
    else:
        pass
if c==0:
    print("Yes")
else:
    print("False")
#16
n=int(input())
m=int(input())
c=0
for i in range(1,m+1,1):
    if n%i==0 and n%i==0:
        c=i
    else:
        pass
print("gcd",c)
#17
n=int(input())
m=int(input())
if n>=m:
    a=n
else:
    a=m
for i in range(1,a+1):
    if n%i==0 and m%i==0:
        print(i)
    else:
        pass
#22
n=int(input())
a=n
b=n
f=n
c=0
while a>0:
    c+=1
    a=a//10
print(c)
s=0
while b>0:
    s+=(b%10)**c
    b=b//10
print(s)
if f==s:
    print("it is an armstrong number")
else:
    print("no")
#palindrome
n=int(input())
a=str(n)
b=a[::-1]
print(b)
#factorial
n=int(input())
i=0
s=1
while i<n:
    i+=1
    s*=i
print(s)
#19factorial
n=int(input())
s=1
for i in range(1,n+1):
    s=s*i
print(s)
#count factors
n=int(input())
i=1
c=0
while i<=n:
    if n%i==0:
        c+=1
    i+=1
print(c)
#fibonacci
n=int(input())
x=0
y=1
z=0
print(0)
while x+y<n:
        if z<n:
            z=x+y
            print(z)
            x=y
            y=z
        else:
            break
#prime
n=int(input())
for j in range(2,n):
    a='prime'
    for i in range(2,j):
        if j%i==0:
            a='composite'
            break
    if a=='prime':
         print(j)
#sum of odd and even
j=int(input())
even=0
odd=0
for a in range(1,j):
    for i in range(a):
        num=int(input())
        if num%2==0:
            even+=num
        else:
            odd+=num
print('sum of odd',odd)
print('sum of even',even)
        
                
            
            
            
        
