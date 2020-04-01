---
layout: post
title: leetcode daily record 2020-02-06
date: 2020-02-06
Author: Yuwei Wu
categories: 
tags: [daily]
comments: true
toc: true
---


# Leetcode


### 1 492. Construct the Rectangle
```python
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import math
        a = math.sqrt(area)
        if isinstance(a, int):
            return [a,a]
        
        start = int(a)
        
        while start >=1:
            if area%start == 0:
                return [area//start, start]
        
        
            start -= 1

```


### 2  504. Base 7
```python
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = []
        flag = 1
        if num <0:
            flag = -1
            num = -num
            
        if num == 0: return "0"
        while num >0:
            res.append(str(num%7))
            
            num = num // 7
        
        
        if flag == -1:
            return "-" + "".join(res[::-1]) 
        return "".join(res[::-1])

```

### 3 520. Detect Capital
```python

class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        if word == word.lower() or word == word.upper():
            return True
        if word[0] == word[0].upper() and word[1:] == word[1:].lower():
            return True
    
    
    
        return False
```

### 4 
