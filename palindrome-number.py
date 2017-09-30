from unittest import TestCase, main

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0: return False

        numberInStr = str(x)

        stringLen = len(numberInStr)
        if (stringLen < 2): return True

        halfLen = int(stringLen/2)
        for i in range(halfLen):
            if numberInStr[i] != numberInStr[stringLen-i-1]:
                return False

        return True
        
class TestMyAtoi(TestCase):
    def test_positive_true(self):
        self.assertEqual(Solution().isPalindrome(0), True)
        self.assertEqual(Solution().isPalindrome(11), True)
        self.assertEqual(Solution().isPalindrome(111), True)
        self.assertEqual(Solution().isPalindrome(101), True)
        self.assertEqual(Solution().isPalindrome(22322), True)
        

    def test_positive_false(self):
        self.assertEqual(Solution().isPalindrome(100), False)
        self.assertEqual(Solution().isPalindrome(10), False)
        self.assertEqual(Solution().isPalindrome(223288), False)

    def test_negative(self):
        self.assertEqual(Solution().isPalindrome(-1), False)
        self.assertEqual(Solution().isPalindrome(-2147447412), False)

if __name__ == '__main__':
    main()
    print('completed')
