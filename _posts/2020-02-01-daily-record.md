# leetcode contest


### 1. 1343. Maximum Product of Splitted Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.value = 0
        self.total = self.get_value(root)
        self.find_max(root)
        return  self.value %(10**9+7)
    
    def get_value(self, root):
        if not root:
            return 0
        return self.get_value(root.left) + self.get_value(root.right) + root.val

    
    def find_max(self, root):
        if not root: 
            return 0
        left = self.find_max(root.left)
        right = self.find_max(root.right)
        self.value = max(self.value, left*(self.total-left), right*(self.total-right))
        return root.val + left +  right


```



### 2 1344. Jump Game V
Reference: https://leetcode.com/problems/jump-game-v/discuss/496620/Python-DP
using the dynamic programming!!!
```python
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        dp = [1] * n
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
        #start from the smallest point
            for di in [-1, 1]:
                for j in xrange(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):  
                        break  
                    dp[i] = max(dp[i], dp[j] + 1)
        
         return max(dp)
```

```python
class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        n = len(arr)
        res = [0] * n

        def dp(i):
            if res[i]: return res[i]
            res[i] = 1
            for di in [-1, 1]:
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]): 
                        break
                    res[i] = max(res[i], dp(j) + 1)
            return res[i]
        ans = 0
        for i in range(n):
            ans = max(ans, dp(i))
        
        return ans


```
