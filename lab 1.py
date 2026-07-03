#1
print ("hello world")

#2
a=int(input('enter num 1:'))
b=int(input("enter num 2:"))
# ADD
print("added value:",a+b)
#sub
print("sub value:",a-b)
#multiply,
print("multiplied value:",a*b)
#Divide
print("divided value:",a/b)
#modulus
print("modulus value:",a%b)

#3
c = int(input("Enter a number for its square root:"))
d= c**0.5
print("Square root is:",d)

#4
x= int(input("enter height of triangle:"))
y= int(input("enter breadth of triangle:"))
print("area of triangle:",0.5*x*y)

#5
num1=int(input("Enter number:"))
num2=int(input("enter number 2:"))
form1= num1**2 + num2**2 +2*num1*num2
form2= num1**2 + num2**2 -2*num1*num2
form3= (num1+ num2)*(num1-num2)
print("(a+b)**2 formula:",form1)
print("(a-b)**2 formula:",form2)
print("(a**2-b**2 formula:",form3)
#6

var1=input("enter a string_1:")
var2=input("enter a string_2:")
var3=var1
var1=var2
var2=var3
print("string1:",var1)
print("string2:",var2)

var1,var2=var2,var1
print("string1:",var1,"\n string 2:",var2)

#7
km=int(input("enter number of kilometers:"))
mil=km*0.63
print("the value in miles is:",mil)

#8  --formula = (Celsius x 1.8) + 32

temp = int(input("enter temp in celsius:"))
fahr =  (temp*1.8)+32
print("temperature in fahrenheit:",fahr)

#9

h=int(input("enter a num:"))
g=h%10
print("last digit is:",g)

#10

i=int(input("enter num:"))
j=i%100
print("last two digits are:",j)


#11

number=int(input("enter a 5 digit number:"))
ig=number%1000
ik=ig//100
print("middle digit is:",ik)
print("square of ",ik," is",ik**2)
    
    
           
                 

           
           




 
       

