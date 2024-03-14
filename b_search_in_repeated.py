def search(arr,ele): 
  low=0
  high=len(arr)-1
  while low<=high:
    mid=(low+high)//2
    if arr[mid]==ele:
      print( "found at"+str(mid))
      return None
    if arr[mid]<=arr[high]:
      if arr[high]>=ele>arr[mid]:
        low=mid+1
      else:
        high=mid-1
      continue  
    elif arr[low]<=arr[mid]:
      if arr[low]<=ele<arr[mid]:
        high=mid-1
      else:
        low=mid+1
  print("Not found")          

arr=[23 ,34,45,46,46,46,47,1,1,3,4,4,10]
for i in arr:
    search(arr,i+1)
    
