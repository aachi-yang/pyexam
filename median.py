class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = 0
        n = 0

        def get_next_value():
            nonlocal m, n
            try:
                v1 = nums1[m]
                try:
                    v2 = nums2[n]
                    if (v1 < v2):
                        m += 1
                        v = v1
                    else:
                        n += 1
                        v = v2
                except IndexError:
                    m += 1     
                    return v1

            except IndexError:
                v =  nums2[n]    
                n += 1
            return v

        total = len(nums1) + len(nums2)
        count = int((total+1)/2)
        
        result = 0
        median = 0

        for k in range(count):
            median = get_next_value()
        
        if total % 2:
            result = median
        else:
            if total > 0:
                result = (median + get_next_value())/2

        return result

if __name__ == '__main__' :                   
    s1 = []
    s2 = [1]                

    s = Solution()
    val = s.findMedianSortedArrays(s1, s2)
    print('val = ', val)

    s1 = [1,3]
    s2 = [2,4]                

    s = Solution()
    val = s.findMedianSortedArrays(s1, s2)
    print('val = ', val)
                

        
        
        
            
            
