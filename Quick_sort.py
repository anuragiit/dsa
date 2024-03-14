def quick_sort(arr,a,b):
    if a<b:
        i=a-1 # i always (throughout the movement of variable j) represent the index of rightmost smaller element (smaller w.r.t pivot)
        j=a
        while j<b:
            if arr[j]<arr[b]: # if B occurs do nothing and if S occurs swap it with arr[i] (which will be B) after incrementing i
                i+=1
                arr[i],arr[j]=arr[j],arr[i]
            j+=1
        arr[i+1],arr[b]=arr[b],arr[i+1] # swap the pivot with the element sitting next to the final (i.e. after j reaches pivot-1) rightmost smaller element
        print(arr)
        quick_sort(arr,a,i)   
        quick_sort(arr,i+2,b)
   

for i in range(int(input('Enter no of test cases'))):
        n=int(input('\n Enter how many numbers you want to sort'))
        arr=[int(i) for i in input('Enter array elements').split(' ')]
        quick_sort(arr,0,n-1)
        print("Sorted array\n")
        for i in arr:
            print(i,end=' ')

    
        
