a=input('Enter your bracket string\n')
l=list()
status=True
for b in a:
    if b=='(' or b=='{' or b=='[':
        l.append(b)
    elif  not len(l) and (b=='}' or b==')' or b==']'):
        print('invalid')
        status=False
        break
    elif b==')':
        if l[len(l)-1]=='(':
            l.pop(len(l)-1)
        else:
            print('Invalid')
            status=False
            break
    elif b=='}':
        if l[len(l)-1]=='{':
            l.pop(len(l)-1)
        else:
            print('Invalid')
            status=False
            break    
    elif b==']':
        if l[len(l)-1]=='[':
            l.pop(len(l)-1)
        else:
            print('Invalid')
            status=False
            break
if  not len(l) and status:
    print('valid')
elif status and len(l):
    print('Invalid')

# In three cases a given string of brackets can  be invalid
#case 1: [[[]]-----Here,both closing are matching with top of stack,but length of final stack is not zero
#case 2:[[]]]-----Here,closing bracket is encountered first without any opening bracket([[]] is eqiuvalent to empty stack)
#case 3:[{(})]----Here,first closing curly parenthesis is not matching with  top of stack

    

            
