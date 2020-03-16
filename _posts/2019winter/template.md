# 1. Binary Search

区间定义：[l, r) 左闭右开

其中f(m)函数代表找到了满足条件的情况，有这个条件的判断就返回对应的位置，如果没有这个条件的判断就是lowwer_bound和higher_bound.
```
def binary_search(l, r):
    while l < r:
        m = l + (r - l) // 2
        if f(m):    # 判断找了没有，optional
            return m
        if g(m):
            r = m   # new range [l, m)
        else:
            l = m + 1 # new range [m+1, r)
    return l    # or not found
```
lower bound: find index of i, such that A[i] >= x
```
def lowwer_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
```
upper bound: find index of i, such that A[i] > x
```
def higher_bound(self, nums, target):
    # find in range [left, right)
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) / 2
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid
    return left
```

# 2.BFS and FFS
863. All Nodes Distance K in Binary Tree


# 3 Tree
前序遍历：根结点 ---> 左子树 ---> 右子树   

中序遍历：左子树---> 根结点 ---> 右子树   

后序遍历：左子树 ---> 右子树 ---> 根结点   
## preoder
```python
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    result = []
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = []
        seq = [] #记录先序访问序列
        while ((root!=None) | (len(stack)!=0)):
            if root!=None:
                seq.append(root.val)   #先访问根节点
                stack.append(root)  
                root = root.left   
            else:
                root = stack.pop() #回溯至父节点
                root = root.right
        return seq 
```

```python
    def preOrder(self, root, res):
        if not root: return
        res.append(root)
        self.preOrder(root.left, res)
        self.preOrder(root.right, res)
```

## inorder
```python
class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    result = []
    def inorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        seq = []
        output = []
        while ((root!=None) | (len(stack)!=0)):
            if root!=None:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                seq.append(root.val) # 左孩子先pop出来，再pop根节点
                root = root.right
         
        return seq   
```
```python
    def inOrder(self, root,res):
        if not root:return
        self.inOrder(root.left, res)
        res.append(root)
        self.inOrder(root.right, res)
        return res
```
## postorder
```python
class Solution:
    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    result = []
    def postorderTraversal(self, root):
        # write your code here
        if root is None:
            return []
        stack = []
        seq = []
        output = []
        while ((root!=None) | (len(stack)!=0)):
            if root!=None:
                seq.append(root.val)
                stack.append(root)
                root = root.right  # 这从left变成了 right
            else:
                root = stack.pop()
                root = root.left # 这从right变成了 left
                
        while seq:  # 后序遍历 是 将先序遍历的反过来
            output.append(seq.pop())

        return output
```

## tree recursion
```python
class Solution:
    def mergeTrees(self, t1, t2):
        if not t2:
            return t1
        if not t1:
            return t2
        newT = TreeNode(t1.val + t2.val)
        newT.left = self.mergeTrees(t1.left, t2.left)
        newT.right = self.mergeTrees(t1.right, t2.right)
        return newT
```




### 4 recursion


```
