---
layout: post
title: leetcode daily record 2020-03-26
date: 2020-03-26
Author: Yuwei Wu
categories: 
tags: [daily]
comments: true
toc: true
---


# Leetcode 5


### 1 780. Reaching Points
```python
class Solution(object):
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
        
        if sx > tx or sy > ty:
            return False
        
        if sx == tx and (ty-sy)%sx == 0:
            return True
        
        if sy == ty and (tx-sx)%sy == 0:
            return True
        
        if tx < ty:
            return self.reachingPoints(sx,sy,tx,ty%tx)
        else:
            return self.reachingPoints(sx,sy,tx%ty,ty)
```



### 2 414. Third Maximum Number
```python
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(list(set(nums)))
        
        if len(a) <= 2: return max(nums)
        else: return a[-3]
```

### 3 459. Repeated Substring Pattern
```python
class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        start = 0
        
        for i in range(1,len(s)):
            if s[i] == s[start]:
                string = s[start:i]
                _len = len(s)
                check = "".join([string] * (_len/len(string)))
                #print([_len/len(string), check])
                if check == s:
                    return True
            
        return False
               
```

### 4 476. Number Complement

```python
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1

            
        return (i - 1) ^ num 
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        i = 1
        while i <= num:
            i = i << 1

            
        return (i - 1) ^ num 
```


### 5 482. License Key Formatting
```python

class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        
        s = S.upper().split("-")
        s = "".join(s)
        
        
        first =  len(s)%K
        res = ""
        ans = s[0:first]
        if ans:
            res = ans +  "-"
        for i in range(1, (len(s)//K)+1 ):
            ans = s[first + (i-1)*K : first+ i*K]
            #print(ans)
            res +=   ans +  "-"
```