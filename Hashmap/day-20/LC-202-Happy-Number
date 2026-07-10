class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool"""

        seen= set()
        while n != 1:
            if n in seen:
                return False

            seen.add(n)

            temp = n
            sum_square = 0

            while temp > 0:
                digit = temp % 10
                sum_square += digit * digit
                temp //= 10

            n = sum_square

        return True
        
