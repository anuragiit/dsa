class TreeNode:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
    def insert(self,node):
        current=self
        parent=self
        while current:
            parent=current
            if node.value>current.value:
                current=current.right
            else:
                current=current.left
        if parent.value>node.value:
            parent.left=node
        else:
            parent.right=node
        #current=self
        #while current.left is not None and node.value<current.value or current.right is not None and node.value>current.value:
          #  if current.left is not None and node.value<current.value:
                #current=current.left
            #if current.right is not None and node.value>current.value:
                #current=current.right
         #if current.left is None and node.value<current.value:
                #current.left=node
         #if current.right is None and node.value>current.value:
                #current.right=node      
                

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value)
        if self.right:
            self.right.inorder()


    def levelorder(self):
        queue=[]
        queue.append(self)
        while queue:
            c=queue.pop(0)
            print(c.value)
            if c.left:
              queue.append(c.left)
            if c.right:
               queue.append(c.right)
               
    def parent_node_data(self,data):
        current=self
        parent=self
        while current.value!=data:
            parent=current
            if current.value>data:
                current=current.left
            else:
                current=current.right
        return parent.value        
        
               
r=TreeNode(50)
r.insert(TreeNode(80))
r.insert(TreeNode(70))
r.insert(TreeNode(30))
r.insert(TreeNode(40))
r.insert(TreeNode(45))
r.insert(TreeNode(55))
r.insert(TreeNode(10))
r.insert(TreeNode(15))
r.insert(TreeNode(60))
r.insert(TreeNode(65))



