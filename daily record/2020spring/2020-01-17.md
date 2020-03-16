# Leetcode 


https://www.hrwhisper.me/leetcode-best-time-to-buy-and-sell-stock-i-ii-iii-iv/

### 1 714. Best Time to Buy and Sell Stock with Transaction Fee
```python
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        cash = 0
        hold = -prices[0]
        
        for i in range(1, len(prices)):
            cash = max(cash, hold + prices[i] - fee)
            #  the maximum profit we could have if we did not have a share of stock
            
            hold = max(hold, cash - prices[i])
            #  the maximum profit we could have if we owned a share of stock
         
        return cash

```

greedy
```c++
class Solution {
public:
    int maxProfit(vector<int>& prices, int fee) {
        int profit=0;
        int curProfit=0;
        int minP=prices[0];
        int maxP=prices[0];
        int i;
        for(i=1;i<prices.size();i++){
            minP=min(minP,prices[i]);
            maxP=max(maxP,prices[i]);
            curProfit=max(curProfit,prices[i]-minP-fee);
            if((maxP-prices[i])>=fee){//can just sell the stock at maxP day.
                profit+=curProfit;
                curProfit=0;
                minP=prices[i];
                maxP=prices[i];
            }
        }
        return profit+curProfit;//the last trade have to be made if there is some profit
    }
};
```

### 2 123. Best Time to Buy and Sell Stock III
```python
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        
        dp = [0] * len(prices) #dp[i]为到第i天能获取的最大值
        _min = prices[0]
        
        for i in range(1, len(prices)):
            #print([prices[i], _min])
            dp[i] = max(dp[i - 1], prices[i] - _min)
            _min = min(prices[i], _min)
            
        
       # print(dp)
        
        ans = dp[-1]
        max_price = prices[-1]
        for i in range(len(prices) - 2, 0, -1):
            ans = max(ans, max_price - prices[i] + dp[i - 1])
            max_price = max(max_price, prices[i])
            
        return ans
```

### 3 188. Best Time to Buy and Sell Stock IV
```c++
        for(int x = 1; x <= k; ++x){
            for(int i = 1; i < prices.size(); ++i){
                dp[i][x] = dp[i - 1][x]; // 不做交易
                for(int j = 0; j < i; ++j){
                    dp[i][x] = max(dp[i][x], dp[j][x - 1] + prices[i] - prices[j]);
                }
```
* 设dp[i][x]为第i天第x次交易的最大利润，则容易写出dp方程：   

    dp[i][x] = max(dp[i-1][x] , dp[j][x – 1] + prices[i] – prices[j])  0 <= j < i    
    上面的状态转移方程第一项为第i天不进行交易，第二项为枚举j 从0~i-1，第j天买入，第i天卖出    

注意当k >= len(prices) / 2的时候，说明相当于无限次交易，和第122题Best Time to Buy and Sell Stock II 一样。    

```python
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k ==0: return 0
        if not prices: return 0
        if k >= (len(prices)>>1): return self.maxprofit2(prices)
        dp = [ [0]*len(prices) for _ in range(k+1)]

        for i in xrange(1,k+1):
            maxTemp=-prices[0]
            for j in xrange(1,len(prices)):
                #print(maxTemp)
                dp[i][j]=max(dp[i][j-1],prices[j] + maxTemp)
                maxTemp =max(maxTemp,dp[i-1][j-1] - prices[j])
        
        #print(dp)
        return dp[k][-1]
    
    def maxprofit2(self, prices):
        res = 0
        
        for i in range(1, len(prices)):
            if prices[i] >= prices[i-1]:
                res += prices[i] - prices[i-1]
        return res
```

### 4 647. Palindromic Substrings

DP
https://www.geeksforgeeks.org/count-palindrome-sub-strings-string/

```python
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        N = len(s)
        ans = 0
        for center in range(2*N  -1):
            left = center //2
            right = left + center %2
            #print([left, right])
            while left >= 0 and right < N and s[left] == s[right]:
                ans += 1
                right +=1
                left -= 1        
        return ans
```
Manacher's Algorithm
```python
def countSubstrings(self, S):
    def manachers(S):
        A = '@#' + '#'.join(S) + '#$'
        Z = [0] * len(A)
        center = right = 0
        for i in xrange(1, len(A) - 1):
            if i < right:
                Z[i] = min(right - i, Z[2 * center - i])
            while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                Z[i] += 1
            if i + Z[i] > right:
                center, right = i, i + Z[i]
        return Z

    return sum((v+1)/2 for v in manachers(S)) # 长度变成了两倍


```

### 5 500. Keyboard Row

```python
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row = [""]*3
        row[0] = "qwertyuiop"
        row[1] = "asdfghjkl"
        row[2] = "zxcvbnm"
        res = []
        for word in words:
            lo_word = word.lower()
            for i in range(3):
                if lo_word[0] in row[i]:
                    r = i
                    break
            flag = 0
            for w in lo_word:
                if w not in row[r]:
                    flag = 1
                    break            
            if flag == 0: res.append(word)
        
        
        return res

```
better 
```python
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3
        res = []
        for word in words:
            if len(set(rowdict[c] for c in word)) == 1:
                res.append(word)
        return res

```

### 6 355. Design Twitter
```python
class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweetId= collections.defaultdict(list) 
        self.follering = collections.defaultdict(list) 
        self.count = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        
        self.tweetId[userId].append([self.count, tweetId])
        self.count += 1
        
        

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        #print(self.tweetId[userId])
        feed = []
        _id = self.follering[userId] + [userId]
  
        for i in _id:
            for item in self.tweetId[i]:
                feed.append(item)
      
        feed = sorted(feed, key = lambda x :x[0] , reverse = True)
  
        return [ v for i,v in feed[:min(10,len(feed))]  ]
        
    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId: return        
        if followeeId in self.follering[followerId]: return
        self.follering[followerId].append(followeeId)


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId: return
        if followeeId in self.follering[followerId]:
            self.follering[followerId].remove(followeeId)
             


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)


```


### 7 482. License Key Formatting
```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [[False for i in range(9)] for j in range(9)]
        col = [[False for i in range(9)] for j in range(9)]
        block = [[False for i in range(9)] for j in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    k = i//3 *3 + j//3
                    if row[i][num] or col[j][num] or block[k][num]:
                        return False
                    row[i][num] = col[j][num] = block[k][num] = True
        return True
```


### 8 198 house robber
```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp  =  [0] * len(nums)
          
        if len(nums) <=2 : return max(nums) 
        dp[0] =nums[0]
        dp[1] = nums[1]
        dp[2] = nums[2]+dp[0]
        if len(nums) == 3: return max(dp)
        for i in range(3, len(nums)):
            dp[i] =  max(dp[i-2],dp[i-3]) + nums[i]
        return max(dp) 
```
```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i] + memo[i-1], memo[i])
            
        return memo[len(nums)]


```
### 9   213. House Robber II

```python
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1: return nums[0]       
        max1 = self.robarray(nums[1:])
        max2 = self.robarray(nums[:-1])
        return max(max1, max2)
        
    def robarray(self, nums):
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        memo = [0] * (len(nums) + 1)
        memo[0] = 0
        memo[1] = nums[0]
        
        for i in range(1, len(nums)):
            memo[i+1] = max(nums[i] + memo[i-1], memo[i])
            
        return memo[len(nums)]

```

### 10 337. House Robber III
```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root):
            # from bottom to top
            if not root: return [0, 0] # before layer, no robcurr, robcurr
            robleft = dfs(root.left)
            robright = dfs(root.right)
            norobcurr = robleft[1] + robright[1]
            robcurr = max(root.val + robleft[0] + robright[0], norobcurr)
            return [norobcurr, robcurr]
        return dfs(root)[1]

```
