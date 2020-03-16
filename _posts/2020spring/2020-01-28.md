# Leetcode 


### 1. 788. Rotated Digits
```python
class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        #ans = []
        for i in range(1, N+1):
            if self.isrotated(i):
                res += 1
                #ans.append(i)
        #print(ans)
        return res
            
        
    def isrotated(self, n):
        if n<=10:
            if n in [2,5,6,9]:
                return True
        else:
            _list = []
            while n:
                ans = n%10
                _list.append(ans)
                if ans not in [2,5,6,9,1,8,0]:
                    return False
                n = n//10

            for j in [2,5,6,9]:
                if j in _list:
                    return True
            return False
```
### 2. 1002. Find Common Characters
```python
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        res = collections.Counter(A[0])
        for i in range(1,len(A)):
            c = collections.Counter(A[i])
            res = c&res
        print(res)
        
        
        ans = []
        for i,v in res.items():
            for j in range(v):
                ans.append(i)
        return ans
```
### 3. 452. Minimum Number of Arrows to Burst Balloons
```python
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if not points: return 0
        points = sorted(points, key = lambda x: (x[0], x[1]))
        res = 1
        start = points[0][0]
        end = points[0][1]
        for i in range(1,len(points)):
            if points[i][0] <= end:
                start = max(start, points[i][0])
                end = min(end, points[i][1])
            else:
                res += 1
                start = points[i][0]
                end = points[i][1]
        return res

```

### 4. 1185. Day of the Week
```python
class Solution(object):
    def dayOfTheWeek(self, day, month, year):
        """
        :type day: int
        :type month: int
        :type year: int
        :rtype: str
        """
        import calendar
        
        index = calendar.weekday(year, month, day)
        if index == 0: return "Monday"
        if index == 1: return "Tuesday"
        if index == 2: return "Wednesday"
        if index == 3: return "Thursday"
        if index == 4: return "Friday"
        if index == 5: return "Saturday"
        if index == 6: return "Sunday"
```

### 5 1184. Distance Between Bus Stops
```python
class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        
        clockwise = 0
        counter = 0
        
        for i in range(min(start, destination), max(start, destination)):
            clockwise += distance[i]
        
        counter = sum(distance) - clockwise
        return min(counter, clockwise)
```

### 6 674. Longest Continuous Increasing Subsequence
```python
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        _max = 0
        start = 0
        end = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                end += 1
            else:
                _max = max(_max, end-start)
                start = i
                end = i+1
        
        return max(_max, end-start)

```


### 7 710. Random Pick with Blacklist
```python
Memory error  [[1000000000, [640145908]]
import random
class Solution(object):

    def __init__(self, N, blacklist):
        """
        :type N: int
        :type blacklist: List[int]
        """
        self.dic = {}
        self.black = {}
        self.len = N-len(blacklist)
        
        for i in blacklist:
            self.black[i] = i
            
        index = 0
        for j in range(N):
            if j not in self.black:
                self.dic[index] = j
                index += 1
        
            
        print(self.dic)    
            

    def pick(self):
        """
        :rtype: int
        """
        index = random.randint(0, self.len-1)
        return self.dic[index]
```

```python
只存 blacklist 的索引 正常的索引都不需要
import random
class Solution(object):

    def __init__(self, N, blacklist):
        
        blacklist = sorted(blacklist)
        
        self.b = set(blacklist)
        
        self.m = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self):
        i = random.randint(0, self.length - 1)
        
        return self.m[i] if i in self.m else i


```


### 8 456. 132 Pattern
```python
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        s3 = -float("inf")
        for n in nums[::-1]:
            print(s3, stack)
            if n < s3:
                return True
            while stack and stack[-1] < n:
                s3 = stack.pop()
            stack.append(n)
        return False
```

```python
会超时
class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        intervals = []
        i = 1
        s = 0
        
        while i< len(nums):
            if nums[i] <= nums[i-1]:
                if s< i-1:
                    intervals.append((nums[s], nums[i-1]))
                s = i
            for u,v in intervals:
                if u < nums[i] < v:
                    return True
            
            i+= 1
        
        return False
```


### 9 1260. Shift 2D Grid
```python
class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        R, C = len(grid), len(grid[0])
        arr = []
        for i in range(R):
            for j in range(C):                
                arr.append(grid[i][j])        
        index = R*C -k%( R*C )
        for i in range(R):
            for j in range(C):
                if index == R*C:
                    index = 0
                grid[i][j] = arr[index]
                index += 1      
        return grid
```


### 10 1207. Unique Number of Occurrences
```python
class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        c = collections.Counter(arr)
        
        
        return len(set(c.values())) == len(c.values())

```
