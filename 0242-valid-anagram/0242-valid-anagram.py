class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)
        return s == t
        """for i in range (len(s)):
            for i in range (len(t)):
                if s[i] == t[i]:
                    i += 1
                    return True
                else:
                    return False"""  