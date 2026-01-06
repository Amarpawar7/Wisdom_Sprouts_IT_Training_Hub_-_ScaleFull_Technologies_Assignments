#1.Create variables for your name, age, height, and whether you are interested in AI/ML. Print them.

Name="Amar"
Age=21
Height=197,"cm"

print("Name : " ,Name)
print("Age : " ,Age)
print("Height : " ,Height)
print("I am interested in AI/ML..")



#2.Swap the values of two variables without using a third variable.

x=10
y=20
print("Before swapping x : ",x,"y : ",y)

x=x+y
y=x-y
x=x-y

print("After swapping x : ",x,"y : ",y)



#3.Given two numbers, perform all arithmetic operations: addition, subtraction, multiplication, division, floor division, modulus, and power.

x = int(input("Enter the first nuber : "))
y = int(input("Enter the second number : "))

print("Addition of given nos. is : ",x+y)
print("Subtraction of given nos. is :",x-y)
print("Multiplication of given nos. is :",x*y)
print("Division of given nos. is :",x/y)
print("Floor Division of given nos. is :",x//y)
print("Modulus of given nos. is :",x % y)
print("Power of 1st no to 2nd no is :",x**y )



#4.Given a number, check if it is divisible by both 3 and 5.

no= int(input("Enter the number : "))
if no%3 ==0 and no%5 ==0 : 
    print("Yes! the given number is divisible by both 3 and 5.")
else:
    print("No! the given number is not divisible by both 3 and 5.")
    


#5.Check if a number entered by the user is positive, negative, or zero.
n=int(input("Enter the number to check weather it is positive,negative or zero : "))

if n>0:
    print("The given number is a positive number")
elif n<0:
    print("The given number is a negative number")
else:
    print("The given number is Zero")



#6.Take three numbers as input and print the largest one.
x=int(input("Enter first number : "))
y=int(input("Enter second number : "))
z=int(input("Enter third number : "))

if x>=y and x>=z:
    largest=x
elif y >= x and y >= z:
    largest=y
else:
    largest=z

print("Largest number among given three numbers is:", largest)



#7.Check if a given year is a leap year.
n= int(input("Enter a year: "))

if (n%400 == 0) or (n%4 == 0 and n%100 != 0):
    print("Yes! It is a leap year")
else:
    print("No! It is not a leap year")




#8.Find the factorial of a given number using a loop.
n=int(input("Enter the number : "))
fact=1

for i in range(1,n+1):
    fact=fact*i

print("Factorial of the given number is :", fact)



#9.Print the Fibonacci sequence up to n terms
n=int(input("Enter number of terms : "))

a=0
b=1
for i in range(n):
    print(a,end=" ")
    c = a + b
    a = b
    b = c
print()



#10.Write a function to check if a number is prime.
def is_prime(num):
    if num <=  1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

n=int(input("Enter a number: "))
if is_prime(n):
    print("The number is Prime number")
else:
    print("The number is not a Prime number")



#11.Write a function that returns the reverse of a string.
def reverse_string(s):
    return s[::-1]

s=input("Enter a string : ")
print("Reversed string is :",reverse_string(s))