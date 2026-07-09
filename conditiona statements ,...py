#1
x = int(input("Enter a num:"))
y = int(input("Enter a num:"))
if x<y:
    print(x,"is smaller")
else:
    print(y,"is smaller")

#2
w = int(input("Enter a num:"))
z = int(input("Enter a num:"))
if w>z:
    print(w,"is larger")
else:
    print(z,"is larger")

#3
k = int(input("enter a number for its absolute value:"))
if k<0:
    print("absolute value:",k*-1)
else:
    print("absolute value:",k)

#4
num=int(input("enter a num:"))
if num%2==0:
    print("even")
else:
    print("odd")

#5
num=int(input("enter a num:"))
if num%5==0:
    print(num,"multiple of 5")
else:
    print(num,"not multiple of 5")

#6
num=int(input("enter a num:"))
if num%10==0:
    print(num,"multiple of 10")
else:
    print(num,"not multiple of 10")

#7
num=int(input("enter a num:"))
if num/10>=1 and num/10<10:
    print(num,"is a 2 digit number")
else:
    print(num,"not a 2 digit number")

#8
num=int(input("enter a num:"))
if num/100>=1 and num/100<10:
    print(num,"is a 3 digit number")
else:
    print(num,"not a 3 digit number")

#9
num=int(input("enter a num:"))
if num%10==0:
    print(num,"ends with zero")
else:
    print(num,"not ends with zero")

#10
num=int(input("enter a num:"))
sqr_1=num*num
if sqr_1>50:
    print("square value of",num,"is above 50")
else:
    print("square value of",num,"is below 50")
    
#11
x=int(input("enter a num:"))
y=int(input("enter a num:"))
z= x-y
if z==0:
    print("the difference between",x,"and",y,"is zero")
else:
    print("difference is not zero")

#12
mark=int(input("enter your computer science mark:"))
if mark>49:
    print("you have passed")
else:
    print("you have failed")

#13
num=int(input("enter a num:"))
if num%10==0:
    print(num,"divisible by 10")
else:
    print(num,"not divisible by 10")

#14
num=int(input("enter a two digit num:"))
x=num%10
y=num//10
if x>y:
    print(x,"is bigger")
else:
    print(y,"is bigger")
#15
print('''*********************\nchoices---\ntype 1 for easy exam or any number if exam is difficult\n**********************''')
      
choice=input("enter a choice:")
if choice=='1':
      print("The Exam is easy")
else:
      print("The Exam is difficult")
      
#16
print('''*********************\nchoices---\ntype 1 to go out and play \n or type any number is you dont want to play\n**********************''')
      
choice=input("enter a choice:")
if choice=='1':
      print("You can go out and play")
else:
      print("You cannot go out and play")

#17
l= int(input("enter height:"))
b= int(input("enter breadth:"))
if l==b:
    print("It is a square")
else:
    print("It is a rectangle")
#18  Check if a given number is the ASCII value of an uppercase alphabet or not. 
a=input("Enter a uppercase alphabet:")                  
b=int(input("Enter the ASCII value for the alphabet:"))
c=chr(b)
if c==a:
    print(b,"is the ASCII value of the number")
else:
    print("Incorrect ASCII value")
    print("Correct ASCII value:",ord(a))
    

#19 .Check if a given number is the ASCII value of a lowercase alphabet.
    
a=input("Enter a lowercase alphabet:")                  
b=int(input("Enter the ASCII value for the alphabet:"))
c=chr(b)
if c==a:
    print(b,"is the ASCII value of the number")
else:
    print("Incorrect ASCII value")
    print("Correct ASCII value:",ord(a))

#20
a=input("Enter a numeric character:")                  
b=int(input("Enter the ASCII value for the numeric character:"))
c=chr(b)
if c==a:
    print(b,"is the ASCII value of the number")
else:
    print("Incorrect ASCII value")
    print("Correct ASCII value:",ord(a))

    
#21
x=int(input("Enter a number:"))
if x%5==0 and x%3==0:
    print(x,"is a multiple of 5 and 3 ")
else:
    print("it is not a multiple of 5 and 3")


#.22 Check if a given number is a three-digit number and also a multiple of 10.
num=int(input("Enter a three digit number:"))
mod=num//100
if mod<1 and num%10==0:
    print("It is a three digit number and it is a multiple of 10")
else:
    print("it is not a 3 digit number or it is not a multiple of 10")

#23
num=int(input("Enter a three digit number:"))
mod=num//100
if mod<1 and num%10==0 and num%5==0 and num%2==0:
    print("It is a three digit number and it is a multiple of 2,5,10")
else:
    print("it is not a 3 digit number or it is not a multiple of 2,5,10")

#24
x=int(input("Enter a num:"))
y=int(input("Enter a num:"))
if x%2==0 and y%2==0:
    print("The product:",x*y)
else:
    print("The sum:",x+y)

#25
num=int(input("Enter a num:"))
dig=num%10
div=num%7
if dig == 7 or div == 0:
    print("it is a buzz number")
else:
    print("it is not a buzz number")

#if elif else
#1
x=int(input("enter  num:"))
y=int(input("Enter num:"))
z=int(input("Enter num:"))
if x>=y and x>=z:
    print(x,"is the largest number")
elif y>=z and y>=x:
    print(y,"is the largest number")
else:
    print(z,"is the largest number")

#2
x=int(input("enter  num:"))
y=int(input("Enter num:"))
z=int(input("Enter num:"))
if x<=y and x<=z:
    print(x,"is the smallest number")
elif y<=z and y<=x:
    print(y,"is the smallest number")
else:
    print(z,"is the smallest number")

#3
num=int(input("enter num:"))
if num>0:
    print(num,"is positive")
elif num<0:
    print(num,"is negative")
else:
    print("it is zero")

#4
late=int(input("Enter the number of days the books were returned late:"))
if late<6 and late>0:
    print(40*late,"paisa is to be given")
elif late>5 and late <11:
    print(65*late,"paisa is to be given")
elif late>10:
    print(80*late,"paisa is to be given")
else:
    print("days should'nt be in negative")
#5
num_1=int(input("enter a num:"))
num_2=int(input("enter a num:"))
op=input("Enter a operator---(+,-,*,/):")
if op=='+':
    print("sum:",num_1+num_2)
elif op=='-':
    print("difference:",num_1-num_2)
elif op=='*':
    print("product:",num_1*num_2)
elif op=='/':
    print("Quotient:",num_1/num_2)
else:
    print("invalid operator")

#6
num=int(input("enter a num:"))
a=num%5
b=num%3
c=num%7
if a==0 and b==0 and c==0:
    print(num,"is a multiple of 5,3 and 7")
else:
    print("It is not a multiple of 5,3 and 7")

#7
x=int(input("Enter the amount of the parcel in grams:"))
y=input("CHOICES:\nO -- for ordinary delivery\n E-- for express delivery\nEnter your choice:")
if x<101 and x>0:
    if y=='o' or y=='O':
        print("DELIVERY CHARGE: rs.80")
    elif y=='e' or y=='E':
        print("DELIVERY CHARGE: rs.100")
    else:
        print("Invalid choice")
elif x>100 and x<501:
    if y=='o' or y=='O':
        print("DELIVERY CHARGE: rs.150")
    elif y=='e' or y=='E':
        print("DELIVERY CHARGE: rs.200")
    else:
        print("Invalid choice")
elif x>500 and x<1001:
    if y=='o' or y=='O':
        print("DELIVERY CHARGE: rs.210")
    elif y=='e' or y=='E':
        print("DELIVERY CHARGE: rs.250")
    else:
        print("Invalid choice")
elif x>1000:
    if y=='o' or y=='O':
        print("DELIVERY CHARGE: rs.250")
    elif y=='e' or y=='E':
        print("DELIVERY CHARGE: rs.300")
    else:
        print("Invalid choice")
else:
    print("Enter a valid amount")

#8
price=int(input("Enter the price of the laptop:"))
if price < 50001 and price >=0:
    print("Price of laptop",price)
    print("Discount: 0%")
    print("Total Price:",price)
elif price>50000 and price<100001:
    print("Price of laptop",price)
    print("Discount: 10%")
    _nu=(price*10)/100
    final=price-_nu
    print("Total Price:",final)
elif price>100000 and price<150001:
    print("Price of laptop",price)
    print("Discount: 15%")
    _nu=(price*15)/100
    final=price-_nu
    print("Total Price:",final)
elif price>150000 :
    print("Price of laptop",price)
    print("Discount: 20%")
    _nu=(price*20)/100
    final=price-_nu
    print("Total Price:",final)
else:
    print("Enter the correct price")
    
    






































    
    


   
