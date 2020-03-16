# Leetcode

### 1. 391. Perfect Rectangle

TLE 了 之后考虑把list 换成 set 效果不错的！
```python
TLE 了
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        points = []
        s = 0 
        
        for x1,y1,x2,y2 in rectangles:
            vertices = [[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
            s += (y2-y1)*(x2-x1)
            for i,j in vertices:
                if [i,j] not in points:
                    points.append([i,j])
                else:
                    points.remove([i,j])
        
            
        if len(points) == 4:
            points = sorted(points, key = lambda x:(x[0], x[1]))
            if points[1][0] == points[0][0] and  points[3][0] == points[2][0] and points[2][1] == points[0][1] and  points[3][1] == points[1][1] and s == (points[2][0]-points[0][0])*(points[3][1]-points[0][1]):
                return True
        
        return False

```

``` python
class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        
        points = set()
        s = 0 
        for x1,y1,x2,y2 in rectangles:
            vertices = [[x1,y1],[x2,y1],[x1,y2],[x2,y2]]
            s += (y2-y1)*(x2-x1)
            for i,j in vertices:
                if (i,j) not in points:
                    points.add((i,j))
                else:
                    points.remove((i,j))
   
        if len(points) == 4:
            points = sorted(points, key = lambda x:(x[0], x[1]))
            if points[1][0] == points[0][0] and  points[3][0] == points[2][0] and points[2][1] == points[0][1] and  points[3][1] == points[1][1] and s == (points[2][0]-points[0][0])*(points[3][1]-points[0][1]):
                return True
        return False
  ``` 
  
  
  
  
  
