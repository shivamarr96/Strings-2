class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) == 0:
            return 0
        #brute force: O(m*n)
        i = 0
        m = len(haystack)
        n = len(needle)
        if m <= 1:
            if n <= 1:
                if haystack == needle:
                    return 0
            else:
                return -1
        while i<m-n+1:
            j = 0
            k = i
            if haystack[k] == needle[j]:
                while j<n and k<m and haystack[k] == needle[j]:
                    k+=1
                    j+=1
                    if j ==n:
                        return i
            i += 1
        return -1
            
            
