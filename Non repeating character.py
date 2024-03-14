class DLLNode:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None

class Solution:
    
    def __init__(self):
        self.references={}
        self.head=None
        self.tail=None
        
    def add(self,node):
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=self.tail.next
            
    def delete(self,node):
        if node is self.head:
            self.head=self.head.next
        if node is self.tail:
            self.tail=self.tail.prev    
        if node.prev:    
            node.prev.next=node.next
        if node.next:
            node.next.prev=node.prev
        node.prev=None
        node.next=None
            
            
    def FirstNonRepeating(self, A):
        ans=''
        for i in A:
            if i not in self.references:
                temp=DLLNode(i)
                self.add(temp)
                self.references[i]=temp
            elif self.references[i] is not None:
                self.delete(self.references[i])
                self.references[i]=None
            if self.head:
                ans+=(self.head.val)
            else:
                ans+='#'
        return ans         
        


if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

 # hrqcvsvszpsjammdrw       
