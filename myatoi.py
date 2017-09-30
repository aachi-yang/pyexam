from unittest import TestCase, main

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        strippedStr = str.strip()
        if len(strippedStr) == 0:
            return 0
        
        resultStr = ''
        for index, c in enumerate(strippedStr):
            
            if index == 0 and (c is '+' or c is '-'):
                resultStr += c
                continue

            if c not in ['0','1','2','3','4','5','6','7','8','9']:
                break

            resultStr += c
            
        resultValue = 0
        try:
            _, valueStr = resultStr.split('-')
            if (int(valueStr) > 0x7fffffff):
                return 0
            else:
                resultValue = int(resultStr)
        except Exception:
            try:
                resultValue = int(resultStr)
                if (resultValue > 0x7fffffff):
                    return 0                
            except Exception:
                return 0

        return resultValue

class TestMyAtoi(TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_normal(self):
        self.assertEqual(Solution().myAtoi("+1"), 1)
        self.assertEqual(Solution().myAtoi('123'),123)
        self.assertEqual(Solution().myAtoi('0'),0)
        self.assertEqual(Solution().myAtoi('-0'),0)
        self.assertEqual(Solution().myAtoi('2147483647'),2147483647)
        self.assertEqual(Solution().myAtoi('-2147483647'),-2147483647)

    def test_leading_space(self):        
        self.assertEqual(Solution().myAtoi("    +1"),1)

    def test_not_numeric(self):
        self.assertEqual(Solution().myAtoi('12-3'),12)
        self.assertEqual(Solution().myAtoi('0x000'),0)
        self.assertEqual(Solution().myAtoi('0b000'),0)
        self.assertEqual(Solution().myAtoi('  -123a24'),-123)
        
    def test_misc(self):
        self.assertEqual(Solution().myAtoi("++1"), 0)
        self.assertEqual(Solution().myAtoi("--1"),0)
        self.assertEqual(Solution().myAtoi('-    1'),0)
        self.assertEqual(Solution().myAtoi('-2147483649'),0)
        self.assertEqual(Solution().myAtoi('2147483649'),0)


if __name__ == '__main__':
    main()
    print('completed')

