class Solution(object):
    def isPalindrome(self, s):

        s = s.lower()

        new_s = ""
        for i in s:
            if i.isalnum():
                new_s += i
        return new_s == new_s[::-1]



        """s = s.lower()

        new_s = ""

        for i in s:
            if i.isalnum():
                new_s += i

        return new_s == new_s[::-1]"""