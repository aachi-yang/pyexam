from unittest import TestCase, main

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        negative = False
        strippedStr = str.strip()
        if len(strippedStr) == 0:
            return 0

        resultValue = 0
        for index, c in enumerate(strippedStr):
            
            if index == 0:
                if c == '+': continue
                if c == '-': 
                    negative = True
                    continue

            v = ord(c) - ord('0')
            if v < 0 or v > 9:
                break

            resultValue = resultValue * 10 + v

            if index > 12:
                break
                           
        if negative:
            resultValue = resultValue * -1
            if resultValue < -2147483648:
                return -2147483648
        else:
            if resultValue > 2147483647:
                return 2147483647

        return resultValue

class TestMyAtoi(TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_normal(self):
        self.assertEqual(Solution().myAtoi("+1"), +1)
        self.assertEqual(Solution().myAtoi("  +1  "), +1)
        #self.assertEqual(Solution().myAtoi('"+1"'), 1)
        self.assertEqual(Solution().myAtoi('+123'),123)
        self.assertEqual(Solution().myAtoi('0'),0)
        self.assertEqual(Solution().myAtoi('-0'),0)
        self.assertEqual(Solution().myAtoi('21474836479999999'),2147483647)
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
        self.assertEqual(Solution().myAtoi('-2147483649'),-2147483648)
        self.assertEqual(Solution().myAtoi('2147483649'),2147483647)


if __name__ == '__main__':
    main()
    print('completed')

