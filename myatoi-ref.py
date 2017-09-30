from unittest import TestCase, main

class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        res = 0
        n = len(str)
        i = 0
        if i >=n:
            return 0
        while(i < n and str[i] == ' '):
            i += 1
        sig = 1
        if str[i] == '-' or str[i] == '+':
            sig = 1 - 2 * (str[i] == '-')
            i += 1
        
        while(i < n and ord(str[i])>=ord('0') and ord(str[i])<=ord('9')):
            int_v = int(str[i])
            if (res > 214748364 or (res == 214748364 and int_v>7)):
                if sig == 1:
                    return 2147483647
                else:
                    return -2147483648
            res = res * 10 + int_v
            i += 1
        return res * sig

class TestMyAtoi(TestCase):
    def setUp(self):
        self.solution = Solution()
    def test_normal(self):
        self.assertEqual(Solution().myAtoi("+1  "), +1)
        #self.assertEqual(Solution().myAtoi('"+1"'), 1)
        self.assertEqual(Solution().myAtoi('+123'),123)
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
        self.assertEqual(Solution().myAtoi('-2147483649'),-2147483648)
        self.assertEqual(Solution().myAtoi('2147483649'),2147483647)


if __name__ == '__main__':
    main()
    print('completed')

