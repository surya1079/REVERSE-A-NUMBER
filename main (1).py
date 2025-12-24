def NAME(n):
    out=0
    a=n
    while n>0:
        rem=n%10
        out=out*10+rem
        n=n//10
    if a==out:
        return(" it is a palindrome number")
    else:
            return("it is not a palindrome number")
n=int(input("enter the number :"))
print(NAME(n))