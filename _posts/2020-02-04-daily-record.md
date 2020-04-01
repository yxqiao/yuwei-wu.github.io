---
layout: post
title: leetcode daily record 2020-02-04
date: 2020-02-04
Author: Yuwei Wu
categories: 
tags: [daily]
comments: true
toc: true
---


# Leetcode


### 1. 221. Maximal Square

```python
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        import math
        if not matrix: return 0
        res = 0
        R,C = len(matrix), len(matrix[0])
        for i in range(R):
            if matrix[i][0] == '1':
                res = 1
                break
        for j in range(C):
            if matrix[0][j] == '1':
                res = 1
                break            
        for i in range(1,R):
            for j in range(1,C):
                if matrix[i][j] == '1':
                    res = max(res, 1)
                    if matrix[i-1][j] !="0" and matrix[i][j-1] !="0" and matrix[i-1][j-1] != '0' :
                        min_value = min(int(matrix[i-1][j]), int(matrix[i-1][j-1]), int(matrix[i][j-1]))
                        matrix[i][j] =  str(int((math.sqrt(min_value )+1)**2)) 
                        res = max(res, float(matrix[i][j]))
        
        #print(matrix)
        return int(res)
```

### 2.  309. Best Time to Buy and Sell Stock with Cooldown
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #dp[i][x] = max(dp[i-1][x] , dp[j-2][x – 1] + prices[i] – prices[j]) 
        if not prices or len(prices) <2: return 0
        # 冷冻， j<i
        n = len(prices)
        dp =[[0]* n for _ in range(n//2)]
        for x in range(n//2):
            for i in range(1, n):
                for j in range(0, i):
                    #print(i,j,x)
                    if j<=2:
                        dp[x][i]= max(dp[x][i-1] , dp[x][i], prices[i]-prices[j])
                        #print(prices[i]-prices[j])
                    else:
                        dp[x][i]= max(dp[x][i-1] , dp[x][i], dp[x-1][j-2] + prices[i]-prices[j])
                  
        #print(dp)
        return max( dp[k][n-1] for k in  range(n//2))
```
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n=len(prices)
        sell = [0]*n
        buy = [0]*n
        max_profit = [0]*n
        buy[0] = -prices[0]
        for i in range(1,len(prices)):
            buy[i] = max(buy[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        
        return sell[-1]

```
