class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        s = 0
        num = x
        while num > 0:
            r = num % 10
            s = s * 10 + r
            num /= 10
        if s == x:
            return True
        return False
