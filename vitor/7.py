
#my solution is not the best
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s1 = str(x)
        anwser = 0
        if s1[0] == '-':
            anwser = int(self.reversed_string_with_signal(s1))
        else:
            anwser = int(self.reversed_string(s1))
        return  0 if self.is_bigger_than_32_bits(anwser) else anwser

    def reversed_string(self,a_string):
        return a_string[::-1]

    def reversed_string_with_signal(self,a_string):
        return '-{0}'.format(self.reversed_string(a_string)[0:-1])

    def is_bigger_than_32_bits(self,x):
        return True if x.bit_length() >= 32 else False

''' using bit operators is faster than using string and it is less code
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        y = x
        if x < 0:
            y = -y
        z = 0
        while y :
            z = z * 10 + y % 10
            y = y / 10
        if x < 0:
            z = -z
            if z < -(1 << 31):
                return 0
        if z > ((1 << 31) - 1):
            return 0
        return z
'''

print(Solution().reverse(1563847412))
