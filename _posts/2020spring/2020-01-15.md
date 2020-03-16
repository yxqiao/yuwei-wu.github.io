# Leetcode


### 1. 950. Reveal Cards In Increasing Order
```python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck = sorted(deck)     
        res = [deck.pop()]        
        while deck:
            res = [deck.pop()] + [res[-1]] + res[:-1]        
        return res


```


### 2. 64. Minimum Path Sum
```python

TLE了！！！
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
              
        def dfs(x,y,path):
            if x == R-1 and y == C-1:
                return path 
            _min = float("inf")
            if x+1 < R:
                right = dfs(x+1,y,path+grid[x+1][y])
                _min = min(right, _min)
            if y+1 < C:
                down = dfs(x,y+1,path+grid[x][y+1])
                _min = min(down, _min)           
            return _min
        
        res = dfs(0,0,grid[0][0])
        return res
```

```python
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid : return 0
        R, C = len(grid), len(grid[0])
        dp = [ [0]*C for _ in range(R) ]
    
        dp[0][0] = grid[0][0]
        #print(dp)
        
        for i in range(1,R):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for j in range(1,C):
            dp[0][j] = dp[0][j-1] + grid[0][j]     
        
        for i in range(1,R):
            for j in range(1,C):
                dp[i][j] = min(dp[i-1][j]+grid[i][j], dp[i][j-1]+grid[i][j])            
        
        return dp[R-1][C-1]


```


### 3 1131. Maximum of Absolute Value Expression

```python
TLE 暴力
        res = 0
        for i in range(len(arr1)):
            for j in range(i, len(arr1)):
                value = abs(arr1[i] - arr1[j]) + abs(arr2[i] - arr2[j]) + abs(i-j)
                res = max(res, value)
        
        return res


```

abs(a) = max(a, -a)
abs(a)+ abs(b) = max(a+b,-a+b,-a-b,a-b)
abs(x2-x1)+abs(y2-y1) = max[(x2+y2)-(x1+y1),(-x2+y2)-(-x1+y1),(-x2-y2)-(-x1-y1),(x2-y2)-(x1-y1)]

```python
class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        
        symbols = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
        total_case = [ [p*x + q*y +i for i, (x,y) in enumerate(zip(arr1, arr2)) ]  for p, q in symbols ]
        return max([max(case)-min(case) for case in total_case])


```

### 4 883. Projection Area of 3D Shapes

```python
class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """        
        R, C = len(grid), len(grid[0])
        
        xy = 0
        zx = 0
        zy = [0] * C
        
        for i in range(R):
            zx += max(grid[i])
            for j in range(C):
                if grid[i][j] != 0:
                    xy += 1
                    
                zy[j] = max(grid[i][j] ,zy[j])
             
        return xy+zx+sum(zy)
```

### 5 628. Maximum Product of Three Numbers
```python
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums = sorted(nums)
        
        return max(nums[-1]*nums[-2]*nums[-3], nums[-1]*nums[0]*nums[1])

```

### 6 771. Jewels and Stones
```python
class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        res = 0
        for item in S:
            if item in J:
                res += 1
        
        return res

```

### 7 1034. Coloring A Border
```python
class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        R,C = len(grid), len(grid[0])
        border = grid[r0][c0]
        
        start = [[r0,c0]]
        
        visited = [[r0,c0]]
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        while start:
            #print(visited)
            x, y = start.pop(0)
            for dire in directions:
                tx = x + dire[0]
                ty = y + dire[1]
                if tx<0 or tx>R-1 or ty<0 or ty>C-1 or [tx,ty] in visited or grid[tx][ty] != border:
                    continue
                visited.append([tx,ty])
                start.append([tx, ty])
        
        
        res = []
        
        for x, y in visited:            
            if x==0 or y == 0 or x == R-1 or y == C-1:
                res.append([x, y])
            else:
                for j,k in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if grid[j][k] != border: 
                        res.append([x,y])                       

        for x,y in res:
            grid[x][y] = color
        
        return grid

```


### 8 463. Island Perimeter
```python
TLE 了
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R,C = len(grid), len(grid[0])
        visited = []
        res = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==1:
                    count = 0
                    for x,y in ((i,j+1),(i,j-1),(i+1,j),(i-1,j)):
                        if 0<=x<=R-1 and 0<=y<=C-1 and [x,y] in visited:
                            count += 1
                    
                    if count == 0:
                        res += 4
                    elif count == 1:
                        res += 2
                    elif count == 3:
                        res -= 2
                    elif count == 4:
                        res -= 4
                    visited.append([i,j])        
        #print(visited)
        return res

```
```python
还是通不过
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R,C = len(grid), len(grid[0])
        visited = []
        res = 0
        sx, sy = R,C
        for i in range(R):
            for j in range(C):
                if grid[i][j] ==1:
                    sx, sy = i,j
                    break
        
        
        if sx == R: return 0
        visited = [[sx,sy]]
        start =  [[sx,sy]]
        res = 4
        while start:
            x,y = start.pop(0)
            count = 0
            for tx,ty in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if tx<0 or tx>R-1 or ty<0 or ty>C-1 or [tx,ty] in visited or grid[tx][ty] == 0:
                    continue                
                #not in visited
                count = 0
                for nx,ny in ((tx+1,ty),(tx-1,ty),(tx,ty+1),(tx,ty-1)):
                    if nx<0 or nx>R-1 or ny<0 or ny>C-1 or [nx,ny] not in visited or grid[nx][ny] == 0:
                        continue
                    # in visited and ==1 
                    count += 1
                    
                if count == 0:res += 4
                elif count == 1:res += 2
                elif count == 3:res -= 2
                elif count == 4:res -= 4
                    
                visited.append([tx,ty])
                start.append([tx,ty])
                
        return res

```
得用点数学方法
```python
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        R, C = len(grid), len(grid[0])
        counts = 0
        neighbors = 0
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    counts += 1
                    
                    if i < R- 1:
                        if grid[i + 1][j] == 1:
                            neighbors += 1
                    if j < C - 1:
                        if grid[i][j + 1] == 1:
                            neighbors += 1
        return 4 * counts - 2 * neighbors

```





### 9 1051. Height Checker
```python
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        c = sorted(heights)
        res = 0
        for i in range(len(heights)):
            if heights[i] != c[i]:
                res += 1       
        return res
```

### 10 661. Image Smoother
```python
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R,C = len(M), len(M[0])
        new = [ [0]*C for _ in range(R) ]
        
        import math
        for i in range(R):
            for j in range(C):
                _sum = M[i][j]
                count = 1
                for x,y in ((i+1,j),(i-1,j),(i,j+1),(i,j-1),(i+1,j+1),(i+1,j-1),(i-1,j+1),(i-1,j-1)):
                    if 0<=x<=R-1 and 0<=y<=C-1:
                        _sum += M[x][y]
                        count += 1
                
                new[i][j] = int(math.floor(_sum*1.0/count))
                #print([_sum, count])
        
        
        return new
```
