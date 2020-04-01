---
layout: page
title: leetcode daily record 2020-02-08
date: 2020-02-08
Author: Yuwei Wu
categories: 
tags: [daily]
comments: true
toc: true
---



# Leetcode Contest

### 1 1345. Jump Game IV
```python
TLE ! need improvement
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        import collections
        dic = collections.defaultdict(list)
        for i in range(len(arr)):
            dic[arr[i]].append(i)
        
            
        n = len(arr)
        self.min_step = len(arr)-1
        self.end = len(arr)-1

        
        def dfs (start,visited):
            #print([len(visited), self.min_step])
            if len(visited) >= self.min_step:
                return            
            if start == self.end:
                self.min_step  = min(self.min_step,len(visited))
                return 

        
        
            if len(dic[arr[start]]) >1:
                for j in dic[arr[start]]:
                    if j != start and j not in visited:
                        visited.add(j)
                        dfs (j, visited)
                        visited.remove(j) 
            
            if start + 1 < n and start + 1 not in visited:
                #print([visited, start+1])
                visited.add(start + 1)
                
                dfs (start+1, visited)

                visited.remove(start + 1)

            
            if start - 1 > 0 and start - 1 not in visited: 
                #print([visited, start+1])
                visited.add(start - 1)
                dfs (start-1, visited)
                visited.remove(start - 1)

            
            return 
        
        visited = set()
        visited.add(0)
        dfs(0, visited)
        
        return self.min_step 
```

var |= value is equal to:  var = var | value

```python
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # bfs method
        indices = collections.defaultdict(list)
        for i, a in enumerate(arr):
            indices[a].append(i) 
        #print(indices)    
        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now   # include now in done 
            if len(arr) - 1 in done:
                return steps   
            now = {j for i in now for j in [i-1, i+1] + indices.pop(arr[i], [])} - done
```

### 2 1348. Tweet Counts Per Frequency

```python
class TweetCounts(object):

    def __init__(self):
        
        self.name = collections.defaultdict(set)
        

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        self.name[tweetName].add(time)
               

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """
        #print(self.name)
        interval =  60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        
        
        _len = (endTime-startTime)//interval  +1
        res = [0] * (_len)
        
        times = self.name[tweetName]

        
        for item in times:
            index = (item-startTime)//interval
            if 0 <=index <= _len and startTime<= item <= endTime :
                res[index] += 1
      
        return res
```

```python
from collections import defaultdict
import bisect



class TweetCounts(object):

    def __init__(self):
        
        self.a = defaultdict(list)
        

    def recordTweet(self, tweetName, time):
        """
        :type tweetName: str
        :type time: int
        :rtype: None
        """
        bisect.insort(self.a[tweetName], time)
               

    def getTweetCountsPerFrequency(self, freq, tweetName, startTime, endTime):
        """
        :type freq: str
        :type tweetName: str
        :type startTime: int
        :type endTime: int
        :rtype: List[int]
        """           

        delta = 60 if freq == 'minute' else 3600 if freq == 'hour' else 86400
        i = startTime
        res = []
        while i <= endTime:
            j = min(i + delta, endTime+1)
            res.append( bisect.bisect_left(self.a[tweetName], j) -  bisect.bisect_left(self.a[tweetName], i))
            i += delta
        return res

```

### 3 
