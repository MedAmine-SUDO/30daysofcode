import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
        
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        q = []
        l = []
        if root.left != None or root.right != None:
            q.append(root)
            while(q):
                t = q.pop(0)
                l.append(t.data)
                if t.left != None:
                    q.append(t.left)
                if t.right != None:
                    q.append(t.right)

        print(" ".join(map(str, l)))

        

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
