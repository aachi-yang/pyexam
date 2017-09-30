class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x_str = str(x)

        if x < 0:
            _, v = x_str.split('-')
            result = int(v[::-1]) 
            if (result > 0x7fffffff):
                result = 0
            else:
                result *= -1            
        else:
            result = int(x_str[::-1])
            if (result > 0x7fffffff):
                result = 0

        return result


solution = Solution()
print(solution.reverse(-2147483648))        

solution = Solution()
print(solution.reverse(-123))

solution = Solution()
print(solution.reverse(1000000003))


