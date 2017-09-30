
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def compareOnNode(n, k, maxlen):
            """
                seg1: prefix part
                seg2: postfix part with reverse order
            """
            result = []
            #print('n = ', n, 'k = ', k)
            start = n-k
            seg1 = s[start:n]
            end = n+k
            # end is start index, so it is included
            seg2 = s[end:n:-1]
            #print('seg1: ', seg1, 'seq2: ', seg2)
            
            if seg1 == seg2:      
                # end is used in end index, so it have to be increased by one                  
                if len(s[start:end+1]) >= len(result):
                    #print('==> seg1: ', seg1, 'seq2: ', seg2)
                    result = s[n-k:n+k+1]

            return result

        def compareOnGap(n, k, maxlen):
            """
                seg1: prefix part
                seg2: postfix part with reverse order
            """
            result = []

            #print('n = ', n, 'k = ', k)
            start = n-k
            if start <= 0: start = None
            seg1 = s[start:n]

            end = n+k-1 # back one position
            seg2 = s[end:n-1:-1] 
            #print('seg1: ', seg1, 'seq2: ', seg2)
            
            if seg1 == seg2:       
                nseg = s[start:end+1] # +1 to include end element                
                if len(nseg) > len(result):
                    #print('==> seg1: ', seg1, 'seq2: ', seg2)
                    result = nseg

            return result

        m = len(s)
        result = []
        for n in range(m):
            maxlen = min(n+1, m-n+1)
            for k in range(maxlen):
                r = compareOnNode(n, k, maxlen)
                if len(r) > len(result):
                    result = r
                r = compareOnGap(n, k, maxlen)
                if len(r) > len(result):
                    result = r

        return result

if __name__ == "__main__" :
    s = Solution()

    r = s.longestPalindrome("a")
    print("result: a", r)

    r = s.longestPalindrome("bb")
    print("result: bb", r)

    r = s.longestPalindrome("1234bb")
    print("result: bb", r)

    r = s.longestPalindrome("bbbb1234bb")
    print("result: bbbb", r)

    r = s.longestPalindrome("bb1")
    print("result: bb", r)

    r = s.longestPalindrome("babad")
    print("result: bab", r)    

    r = s.longestPalindrome("cbbd")
    print("result: bb", r)        

    r = s.longestPalindrome("aabaa-----")
    print("result: aabaa", r)            

    r = s.longestPalindrome("----aabaa")
    print("result: aabaa", r)                

    r = s.longestPalindrome("===aabaa------")
    print("result: ------", r)                


