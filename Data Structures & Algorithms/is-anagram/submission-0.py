class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1, t1 = {},{}

        for s2 in s:
            s1[s2] = s1.get(s2,0) + 1
        for t2 in t:
            t1[t2] = t1.get(t2,0) + 1

        return t1 == s1


