def maxSubarray(arr):
    es=0
    ps=0
    max_=arr[0]
    for i in arr:
        if i>max_:
            max_=i
        ps+=i
        if ps<0:
            ps=0
            continue
        if ps>es:
            es=ps
    if es=0:
      return max_
            
    return es        
def maxSubsequence(arr):
    b=0
    max_=arr[0]
    for i in arr:
        if i>0:
            b=b+i
        if i>max_:
            max_=i
    if b==0:
        return max_

    return b        
            


if __name__ == "__main__":
    t = int(input())
    for a0 in range(t):
        n = int(input().strip())
        arr=[int(i) for i in input().split(' ')]
        result1 = maxSubarray(arr)
        result2=maxSubsequence(arr)
        print(result1,result2,result3)

