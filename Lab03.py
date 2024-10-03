#Develop a Program for checking if a given n digit number is palindrome or not 

def palindrome(number):
    on = number
    rn = 0

    while number > 0:
        digit = number % 10
        rn = (rn*10) + digit
        number = number // 10
    
    if on == rn:
        return True
    else: 
        return False
    
n = int(input("enter a n - digit Number:"))

if(palindrome(n)):
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")

'''def palindrome(number):
    num_str = str(number)
    rev_str = ""

    for i in range(len(num_str)-1, -1, -1):
        rev_str += num_str[i]

    if num_str == rev_str:
        return True
    else:
        return False

n = int(input("Enter a n-digit number: "))

if palindrome(n):
    print(n, "is a palindrome number")
else:
    print(n, "is not a palindrome number")'''
