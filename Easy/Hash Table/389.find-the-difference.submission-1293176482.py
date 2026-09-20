class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        smap = {}
        tmap = {}
        for char in s:
            if char not in smap:
                smap[char] = 1
            else:
                smap[char] += 1
        for char in t:
            if char not in tmap:
                tmap[char] = 1
            else:
                tmap[char] += 1
        for kv in tmap:
            if tmap[kv] != smap.get(kv, 0):
                return kv