def largestRectangle(h):
    # Complete this function
    max=0
    for i in range(len(h)):
        area=h[i]
        lc=0
        rc=0
        j=i-1
        while j>=0:
            if h[j]>=h[i]:
                lc+=1
                j-=1
            else:
                break
        j=i+1
        while j<len(h):
            if h[j]>=h[i]:
                rc+=1
                j+=1
            else:
                break
        area=h[i]*(rc+lc+1)
        if area>max:
            max=area
    return max        
                
            
n = int(input())
h = [int(i) for i in input().split()]
result = largestRectangle(h)
print(result)
