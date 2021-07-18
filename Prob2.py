from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        #sliding window
        #solution is O(m+n)
        if len(s) == 0 or len(p)>len(s):
            return []
        p_map = dict(Counter(p))
        res = []
        slow = 0
        match = 0
        for i in xrange(len(s)):
            #incoming
            if s[i] in p_map:
                p_map[s[i]] -= 1  
                if p_map[s[i]] == 0:
                    match += 1
            #outgoing
            if i>=len(p):
                out = s[i-len(p)]
                if out in p_map:
                    p_map[out] += 1
                    if  p_map[out] == 1:
                        match -= 1
            if len(p_map) == match:
                res.append(i-len(p)+1)
        return res
            
        
