# Leetcode


### 1 581. Shortest Unsorted Continuous Subarray
```python
class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new = sorted(nums)
        i = 0
        j = len(nums)-1
        
        while i< len(nums) and nums[i] == new[i]:
            i += 1
        if i == len(nums):
            return 0
            
        while j>=0 and nums[j] == new[j]:
            j -= 1
                
        return j-i+1


```
### 2 832. Flipping an Image
```python
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        
        R,C = len(A), len(A[0])
        
        
        
        for i in range(R):
            A[i] = A[i][::-1]
        
        
        
        
        for i in range(R):
            for j in range(C):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        
        
        return A

```

### 3 888. Fair Candy Swap
```python
class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        diff = sum(B)-sum(A)
        c= collections.Counter(B)
        for i in range(len(A)):
            if A[i] + diff//2 in c:
                return [A[i], A[i] + diff//2]
            


```


### 4 733. Flood Fill
```python
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        color = image[sr][sc]
        R,C = len(image), len(image[0])
        start = [[sr,sc]]
        visited = [[sr,sc]]
        while start:
            x,y = start.pop(0)
            for tx,ty in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=tx<=R-1 and 0<=ty<=C-1 and [tx,ty] not in visited and image[tx][ty] == color:
                    visited.append([tx,ty])
                    start.append([tx,ty])        
        
        for i,j in visited:
            image[i][j] = newColor  
    
        return image


```

### 5 401. Binary Watch
```python
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        
        if num == 0: return ["0:00"]
        ans = []
        
        from itertools import combinations 
        
        for item in combinations(range(10), num) :
            time = [0] * 10
            for i in item:
                time[i] = 1
            if self.comp_time(time):
                ans.append(self.comp_time(time))        
        return ans
    
    def comp_time(self,time):
        hours = 0
        minutes = 0      
        index = 0    
        for i in time[:4]:
            hours += i * (2**index)
            index += 1        
        index = 0
        for j in time[4:]:
            minutes += j* (2**index)
            index += 1
        
        if hours >= 12 or minutes >= 60:
            return False
        return str(hours) + ":" + str(minutes).zfill(2)

```

### 6 409. Longest Palindrome
```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        
        odd = 0
        _len  = len(s)
        for i,v in c.items():
            if v%2 !=0:
                odd += 1       
        if odd == 0:
            return _len
        return _len - odd +1
```


### 7 434. Number of Segments in a String
```python
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.split()
        return len(s)
 ```
 
 
 ### 8 985. Sum of Even Numbers After Queries
 ```python
 class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        even = []
        for i in A:
            if i%2 == 0:
                even.append(i)
        
        _sum = sum(even)
        
        res = []
        for value, index in queries:
            if A[index]%2 == 0:
                _sum -= A[index]    
            A[index] += value
            if A[index]%2 == 0:
                _sum += A[index]            
            res.append(_sum)       
        return res
 
 ```
 
 ### 9 1018. Binary Prefix Divisible By 5
 ```python
 TLE 了！
         res = [False] * len(A)
        for i in range(len(A)):
            ith = A[:i+1][::-1]
            #print(ith)
            num = sum([ v* (2**j)  for j,v in enumerate(ith) ])
            #print(num)
            if num%5 == 0:
                res[i] = True
        
        return res
 
 
 ```
 
 ```python
 class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        string = ""
        res = [False]*len(A)
        for a in A:
            string += str(a)    
        for i in range(len(string)):
            num = int(string[:i+1],2)
            if num%5 == 0: res[i] = True  
        return res
 ```
 better one
 ```python
 class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans=[]
        cur=0
        for a in A:
            cur=cur*2+a
            if(cur%5==0):
                ans.append(True)
            else:
                ans.append(False)
        return ans
 
 
 ```
 
 ### 10 807. Max Increase to Keep City Skyline
 ```python

 class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R,C = len(grid), len(grid[0])        
        
        max_R = [0]*R
        max_C = [0]*C
        
        for i in range(R):
            max_R[i] = max(grid[i])
            for j in range(C):
                max_C[j] = max(max_C[j], grid[i][j])   
        res = 0
        for i in range(R):
            for j in range(C):
                num = min(max_R[i], max_C[j])
                res += num - grid[i][j]
        return res
 
 ```
