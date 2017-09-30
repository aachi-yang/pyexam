class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        elem_a_round = numRows + numRows - 2
        if elem_a_round <= 0: 
            elem_a_round = 1

        rows = [''] * numRows
        for i, x in enumerate(s):
            r = i % elem_a_round
            if r >= numRows:
                r = elem_a_round - r
            rows[r] += x     
        
        result = ''.join(rows[j] for j in range(numRows))

        return result
"""
PAYPALISHIRING
P   A   H   N
A P L S I I G
Y   I   R
"""



