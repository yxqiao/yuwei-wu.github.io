# Leetcode

### 1. 643. Maximum Average Subarray I
```python
class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        if len(nums)< k: return 0
        
        res = sum(nums[0:k])
        ans = res
        for i in range(k, len(nums)):
            
            res = res+nums[i]-nums[i-k]
            ans = max(res, ans)
        return ans*1.0/k

```


### 2 644. Maximum Average Subarray II  [locked]
```python
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        res = -float("inf")
        for i in range(k, len(nums)+1):
            k_sum = sum(nums[i-k:i])
            res = max(res, k_sum*1.0/k)
            for j in range(i,len(nums)):
                k_sum += nums[j]
                average = k_sum*1.0/(k+(j-i+1))
                res = max(res, average)
            
        
        return res
```

``` python
二分法 有点难想出来
class Solution:
    """
    @param nums: an array with positive and negative numbers
    @param k: an integer
    @return: the maximum average
    """
    def maxAverage(self, nums, k):
        # write your code here
        n = len(nums)
        _sum = [0]*(n+1)
        left = min(nums)
        right = max(nums)
        
        while right-left > 1e-5:
            minSum = 0
            mid = left + (right - left) *1.0/2
            check = False
            for i in range(1,n+1):
                
                _sum[i] = _sum[i-1]+nums[i-1]-mid
                if i >= k:
                    minSum = min(minSum, _sum[i-k])
                    
                if i >= k and _sum[i] - minSum >0:
                    check = True
                    break
            
                
            if check:
                left = mid
            else: 
                right = mid
                
        return round(left,3)
```

### 3 966. Vowel Spellchecker
```python
class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """
        table1 = set(wordlist)
        
        table2 = {}
        table3 = {}
        
        for word in wordlist[::-1]:
            table2[word.lower()] = word
            no_vowel = re.sub("[aeiou]", '#', word.lower())
            table3[no_vowel] = word
        
        res = []
        for q in queries:
            if q in table1:
                res.append(q)
            elif q.lower() in table2:
                res.append(table2[q.lower()])
            elif  re.sub("[aeiou]", '#',q.lower()) in table3:
                res.append(table3[re.sub("[aeiou]", '#', q.lower()) ])
            else:
                res.append("")
        
        return res
            
```
### 4 594. Longest Harmonious Subsequence
https://en.wikipedia.org/wiki/Subsequence
subsequence  VS Substring
"pwwkew"
"pwke" is a subsequence and not a substring

```python
class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        c = collections.Counter(nums)
        res = 0
        sub = sorted(c.items())
        print(sub)
        n = len(sub)
        for i in range(n-1):
            if sub[i][0]+1 == sub[i+1][0]:
                res = max(sub[i][1]+sub[i+1][1],res)
        

```
