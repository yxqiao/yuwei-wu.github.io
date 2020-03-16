
# Leetcode


# Leetcode contest


### 5315. Maximum 69 Number
```python
class Solution(object):
    def maximum69Number (self, num):
        """
        :type num: int
        :rtype: int
        """
        string = str(num)
        for i in range(len(string)):
            if string[i] == "6":
                print(string[0:i] + "9" + string[i+1:])
                return int(string[0:i] + "9" + string[i+1:])
        return num
```

### 5316. Print Words Vertically
```python
class Solution(object):
    def printVertically(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        words = s.split()
        res= []
        N = len(words)
        
        index = 0
        while True:
            string = ""
            for word in words:
                if index <= len(word) -1:
                    string += word[index]
                    #print(word[index])
                else:
                    string += " "
            
            
            if string != " " * N:
                #print(string)
                res.append(string.rstrip())
            else:
                break
            index += 1
        
        return res
```


###  5317. Delete Leaves With a Given Value
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if not root: return root
        
        if root.left: root.left = self.removeLeafNodes(root.left, target)
        if root.right: root.right = self.removeLeafNodes(root.right, target)
        
        if root.val == target and not root.left and not root.right:
                return None 
        
        return root

```

### 5318. Minimum Number of Taps to Open to Water a Garden


```python
class Solution(object):
    def minTaps(self, n, ranges):
        """
        :type n: int
        :type ranges: List[int]
        :rtype: int
        """
        intervals = [] 
        for i in range(len(ranges)):
            intervals.append([i - ranges[i], i + ranges[i]])
     
        intervals =  sorted(intervals, key = lambda x: (x[0], -x[1]))
             
        res = 1
        last = 0       
        if intervals[0][0] > 0: return -1        
        i = 0
        
        
        while i <= len(intervals)-1:
            
            if intervals[last][0] <0:
                index = last
                _max = intervals[last][1]
                while i <= len(intervals)-1 and intervals[i][0]<=0:
                    if intervals[i][0] <= 0 and intervals[i][1] >= len(intervals)-1:
                        return 1
                
                    if intervals[i][1] > _max:
                        _max = intervals[i][1]
                        last = i
                    
                    i += 1
            if i > len(intervals)-1: break

                
                
            if intervals[last][1] >= len(intervals)-1: return res
            
            if intervals[i][0] > intervals[last][1]: return -1
            index = i
            _max = intervals[i][1]
            while i <= len(intervals)-1 and intervals[i][0] <= intervals[last][1]:
                if intervals[i][0] <= 0 and intervals[i][1] >= len(intervals)-1:
                    return 1                
                if intervals[i][1] > _max:
                    _max = intervals[i][1]
                    index = i
                i += 1
            last = index
            res += 1

        return res

```


### 5 152. Maximum Product Subarray

```python
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        
        
        f = g = res = nums[0]
        
        for i in range(1, len(nums)):
            pre_f, pre_g = f, g
            f = max(pre_f * nums[i], nums[i], pre_g * nums[i])
            g = min(pre_f * nums[i], nums[i], pre_g * nums[i])
            res = max(res, f)
        return res

```
