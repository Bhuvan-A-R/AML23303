#Develop a Python Program to Read n Digits integer number, and Separate the integer number and Display each digit.
def seprate_digit(num):
    digits=[]
    while num>0:
        digit=num%10
        digits.insert(0,digit)
        #digits.append(digit) //To Reverse the Digits
        num=num//10
    return digits

n = int(input("Enter a n-digit Input:"))

digits = seprate_digit(n)

##digits.reverse() //To Reverse the Digits

for digit in digits:
    print(digit,end=" ")
