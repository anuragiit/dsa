class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None
        
class BinarySearchTree:
    def __init__(self):
        self.root=None
    def addNode(self,val):
        n=Node(val)
        if self.root==None:
            self.root=n
            return None
        current=self.root
        while current:
            parent=current
            if parent.data<n.data:
                current=current.right
            else:
                current=current.left
        if parent.data>n.data:
            parent.left=n
        else:
            parent.right=n  

    def preorder(self,root):
        if root.left==None and root.right==None:
            return '('+str(root.data)+')'
        if root.left==None:
            return '('+'('+str(root.data)+')'+self.preorder(root.right)+')'
        if root.right==None:
            return '('+'('+str(root.data)+')'+self.preorder(root.left)+')'
        
        else:
            return '('+'('+str(root.data)+')'+self.preorder(root.left)+self.preorder(root.right)+')'
             
             

bst=BinarySearchTree()
bst.addNode(4)
bst.addNode(1)
bst.addNode(2)
bst.addNode(8)
bst.addNode(5)
a=bst.preorder(bst.root)
print(a)
             
             
        
        
