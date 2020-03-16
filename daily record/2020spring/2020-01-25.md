# leetcode contest


###  1330. Reverse Subarray To Maximize Array Value


```python
class Solution(object):
    def maxValueAfterReverse(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxi, mini = -float("inf"), float("inf")
        
        for a, b in zip(nums, nums[1:]):
            maxi = max(min(a, b), maxi)
            mini = min(max(a, b), mini)
        change = max(0, (maxi - mini) * 2)

        print(maxi, mini)
        
        
        
        # consider [nums[0],a] [b, nums[-1]] that change is abs(nums[0] - b)
        for a, b in zip(nums, nums[1:]):
            tmp1 = - abs(a - b) + abs(nums[0] - b)
            tmp2 = - abs(a - b) + abs(nums[-1] - a)
            change = max([tmp1, tmp2, change])
			
        original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
        return  original_value + change
```


###  1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

```python
class Solution(object):
    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        dis = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dis[i][i] = 0
          
        for i, j, w in edges:
            dis[i][j] = dis[j][i] = w
               
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
                    
    
                
        res = {sum(d <= distanceThreshold for d in dis[i]): i for i in range(n)}
        # same number will be replaced by the larger number
        return res[min(res)]


```


### 1335. Minimum Difficulty of a Job Schedule


```python
class Solution(object):
    def minDifficulty(self, jobDifficulty, d):
        """
        :type jobDifficulty: List[int]
        :type d: int
        :rtype: int
        """
        if len(jobDifficulty) < d: return -1
        
        dp = {}
        for i,job in enumerate(jobDifficulty):
            # the base case, all jobs need to be finish in one day
            dp[0, i] = max(dp.get((0, i-1), 0), job)
        
        
        for i in range(1, d):
            for j in range(i, len(jobDifficulty)):
                mx = jobDifficulty[j]
                for k in range(j, i-1, -1):
                    mx = max(mx, jobDifficulty[k])
                    dp[i, j] = min(dp.get((i, j), float("inf")), mx + dp[i-1, k-1])
                
        return dp[d-1, len(jobDifficulty)-1]


```
