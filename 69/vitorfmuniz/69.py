import math

# my solution
class Solution(object):
    def mySqrt(self, m):
        """
        :type x: int
        :rtype: int
        """
        return self.approximateBinarySearch(m)
    def approximateBinarySearch(self,val=0):
        low = 0
        high = val
        while low <= high:
          mid = (low + high)/2
          if val == mid*mid:
               return mid
          if val < mid * mid:
               high = mid-1
          else:
               low = mid+1
        return high if high < low  else low

'''# best solution
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=x
        while i*i>x:
            i=(i+x/i)/2
        return i
'''

print(Solution().mySqrt(0))
