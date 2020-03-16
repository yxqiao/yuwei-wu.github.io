# Leetcode


### 1 889. Construct Binary Tree from Preorder and Postorder Traversal
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre: return None 
        root = TreeNode(pre[0])

        if len(pre) == 1: return root
        mid = post.index(pre[1]) + 1
        root.left = self.constructFromPrePost(pre[1:mid+1], post[0:mid])
        root.right = self.constructFromPrePost(pre[mid+1:], post[mid:-1])
        return root

```



### 2 978. Longest Turbulent Subarray

cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1

```python
class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A: return 0
        i = 0
        max_len = 1
        while i<len(A)-1: 
            pre = A[i]
            cur = A[i+1]            
            while pre == cur and i< len(A)-1:
                pre = A[i]
                cur = A[i+1]
                i += 1
            
            start = i
            
            if pre<cur:
                flag = -1
            else: flag = 1    
            while i< len(A) and (A[i]-cur)*flag >0:
                flag = - flag
                cur = A[i]
                i += 1            
            max_len = max(max_len, i-start)
            if i>= len(A)-1: break
            i = i-1
        return max_len

```


```python
class Solution(object):
    def maxTurbulenceSize(self, A):
        N = len(A)
        ans = 1
        anchor = 0

        for i in xrange(1, N):
            c = cmp(A[i-1], A[i])
            if c == 0:
                anchor = i
            elif i == N-1 or c * cmp(A[i], A[i+1]) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
```

### 3 120. Triangle
```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        # start from the bottom 
        
        dp = triangle[-1]
        
        layer = len(triangle[-1])
        for i in range(layer-2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j+1],dp[j]) +triangle[i][j]
        
        
        return dp[0]

```
