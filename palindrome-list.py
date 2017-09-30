
class Solution(object):

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        m = len(s)
        result = []
        res_len = 0
        for n in range(m):
            if (n+1) > (m-n+1):
                maxlen = m-n+1
            else:
                maxlen = n+1
            #maxlen = min(n+1, m-n+1)
            longest_str = ""
            on_node = on_gap = True
            node_half = gap_half = 0
            
            for k in range(1,maxlen):              
                # compare on node
                if on_node:
                    try:
                        if s[n-k] == s[n+k]:
                            node_half = k
                        else:
                            on_node = False
                    except IndexError:
                        on_node = False
            
                # compare on gap
                if on_gap:
                    try:
                        if s[n-k] == s[n+k-1]:
                            gap_half = k
                        else:
                            on_gap = False
                    except IndexError:
                        on_gap = False

                if not on_node and not on_gap:
                    break

            if gap_half > node_half:
                #if len(s[n-gap_half:n+gap_half]) > len(result):
                if (gap_half + gap_half) > res_len:
                    result = s[n-gap_half:n+gap_half]
                    res_len = gap_half + gap_half
            else:
                #if len(s[n-node_half:n+node_half+1]) > len(result):
                if (node_half + node_half + 1) > res_len:
                    result = s[n-node_half:n+node_half+1]
                    res_len = node_half + node_half + 1

        return result

if __name__ == "__main__" :
    
    s = Solution()


    r = s.longestPalindrome("aaabaaaa")
    print("result: aaabaaa", r)        


    from cProfile import Profile
    from pstats import Stats

    profiler = Profile()
    profiler.runcall(lambda : s.longestPalindrome("aaabkkkkkkkkkkabdhhuuueaaaa"))
    stats = Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumulative')
    stats.print_stats()
    stats.print_callers()

    r = s.longestPalindrome("cbbd")
    print("result: bb", r)        

    r = s.longestPalindrome("bbbb1234bb")
    print("result: bbbb", r)

    r = s.longestPalindrome("a")
    print("result: a", r)

    r = s.longestPalindrome("bb")
    print("result: bb", r)

    r = s.longestPalindrome("1234bb")
    print("result: bb", r)


    r = s.longestPalindrome("bb1")
    print("result: bb", r)

    r = s.longestPalindrome("babad")
    print("result: bab", r)    

    r = s.longestPalindrome("aabaa-----")
    print("result: aabaa", r)            

    r = s.longestPalindrome("----aabaa")
    print("result: aabaa", r)                

    r = s.longestPalindrome("===aabaa------")
    print("result: ------", r)                


