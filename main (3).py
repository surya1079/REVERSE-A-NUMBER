def strongNumber(n):
    out=0
    a=n
    while n>0:
        rem=n%10
        fact=1
        while rem>0:
            fact=fact*rem
            rem=rem-1
        out=out+fact
        n=n//10
    if a==out:
        return "strong Number"
    else:
        return "not a strong Number"
        
n=int(input("enter the number :"))
print(strongNumber(n))
        
        