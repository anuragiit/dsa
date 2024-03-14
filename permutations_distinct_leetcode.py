class Solution:
    def __init__(self):
        self.lol=[]
    def permute_i(self, nums,k):
        if k==len(nums)-1:
            a=nums.copy()
            self.lol.append(a)
            del(a)
            
        else:    
            for i in range(k,len(nums)):
                nums[i],nums[k]=nums[k],nums[i]
                self.permute_i(nums,k+1)
                nums[i],nums[k]=nums[k],nums[i]    
            
    def permute(self,nums):
        if len(nums)==1:
            self.lol.append([num[0]])
            return self.lol
        if len(nums)==0:
            return self.lol
        self.permute_i(nums,0)
        return self.lol

s=Solution()
num=[1,2,3]
a=s.permute(num)
print(a)        

'''nums=[1,2,3]
lol=[]
lol.append(nums)
print(lol)
a=nums.copy()
a[0],a[1]=a[1],a[0]
lol.append(a)
del(a)
print(lol)'''
