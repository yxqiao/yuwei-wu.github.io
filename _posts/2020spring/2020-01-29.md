# 5 Leetcode

### 1 1154. Day of the Year
``` python
class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:])
        print(year, month, day)
        if year%400==0 or (year%4==0 and year%100!=0):
            mo = [31,29,31,30,31,30,31,31,30,31,30,31]
        else: mo  =  [31,28,31,30,31,30,31,31,30,31,30,31]
        
        
        return  sum(mo[0: month-1])+ day
```


### 2. 448. Find All Numbers Disappeared in an Array
```python
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        nums = set(nums)
        res = []
        for i in range(1,n+1):
            if i not in nums:
                res.append(i) 
        return res
```

### 3 442. Find All Duplicates in an Array
```python
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        _set = set()
        res = []
        for i in nums:
            if i in _set:
                res.append(i)
            else:
                _set.add(i)
        
        #print(_set)
        return res

```

### 4 453. Minimum Moves to Equal Array Elements
```python
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        _min = min(nums)
        for i in nums :
            res += i-_min
          
        return res

```


### 5 462. Minimum Moves to Equal Array Elements II
```python
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        
        median = nums[len(nums)//2]

        res = 0
        for i in nums:
            res += abs(median-i)
        return res

```
