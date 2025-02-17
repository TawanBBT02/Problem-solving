class Node :
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right  = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
                    
    def PrintTree_In(self):
        if self.left:
            self.left.PrintTree_In()
        print(self.data)
        if self.right:
            self.right.PrintTree_In()
        
    def PrintTree_Pre(self):
        print(self.data)
        if self.left:
            self.left.PrintTree_Pre()
        if self.right:
            self.right.PrintTree_Pre()
            
    def PrintTree_Post(self):
        if self.left:
            self.left.PrintTree_Post()
        if self.right:
            self.right.PrintTree_Post()
        print(self.data)
    
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')

    def find_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.data

    def delete(self, lkpval):
        if lkpval < self.data:
            if self.left:
                self.left = self.left.delete(lkpval)
            else:
                print("Value not found")
        elif lkpval > self.data:
            if self.right:
                self.right = self.right.delete(lkpval)
            else:
                print("Value not found")
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        return self
    
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res
    
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res
    
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res
    
root = Node(10)
root.insert(30)
root.insert(40)
root.insert(35)
root.insert(20)
root.insert(47)
root.insert(5)
print("Print InOrder")
root.PrintTree_In()
print("Print PreOrder")
root.PrintTree_Pre()
print("Print PostOrder")
root.PrintTree_Post()
print()

print(root.findval(7))
print(root.findval(35))

print(root.inorderTraversal(root))
print(root.PreorderTraversal(root))
print(root.PostorderTraversal(root))