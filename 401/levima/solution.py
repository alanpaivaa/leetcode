#O(1) for time and space I guess...

class Solution(object):
  
    def is_valid_hour(self,num):
      if (num >> 6) > 11:
        return False
      else:
        return True

    def is_valid_minute(self,num):
      if(num & ~(15<<6)) > 59:
        return False
      else:
        return True
  
    def convert(self,num):
      hour = num>>6
      minute = num & ~(15 << 6)
      return "{:01d}:{:02d}".format(hour,minute) 
    
    
    def readBinaryWatch(self, num):

      res = []
      
      if num > 10:
        return res
        
      for i in range(0,1024):
        if(bin(i).count("1") == num):
          if self.is_valid_hour(i) and self.is_valid_minute(i):
            res.append(self.convert(i))
      return res