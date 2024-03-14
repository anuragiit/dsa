def mul(a,b):
    string=''
    carry=0
    while a:
        a1=a%10
        temp=a1*b+carry
        last_digit=str(temp%10)
        carry=temp//10
        string=last_digit+string
        a=a//10
    temp=temp//10   
    string=str(temp)+string
    return string

a=int(input())
b=int(input())
print(mul(a,b))
