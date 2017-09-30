class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        elem_a_round = numRows + numRows - 2
        if elem_a_round <=0: 
            elem_a_round = 1

        result = ""
        for n in range(numRows):
            for i, x in enumerate(s):
                if i % elem_a_round == n or i % elem_a_round == elem_a_round-n:
                    result += x
        
        return result
"""
PAYPALISHIRING
P   A   H   N
A P L S I I G
Y   I   R
"""

'''
solution = Solution()
s = solution.convert('PAYPALISHIRING', 3)
print('result = ', s)

from cProfile import Profile
from pstats import Stats

profiler = Profile()
profiler.runcall(lambda : solution.convert('PAYPALISHIRING', 3))

stats = Stats(profiler)
stats.strip_dirs()
stats.sort_stats('cumulative')
stats.print_stats()
stats.print_callers()
'''


