def seprate_digit(num):
    digits=[]
    while num>0:
        digit=num%10
        digits.append(digit)
        num=num//10
    return digits

n = int(input("Enter a n-digit Input:"))

digits = seprate_digit(n)

##digits.reverse()

for digit in digits:
    print(digit,end=" ")
