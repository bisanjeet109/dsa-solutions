class Solution:
    def numDecodings(self, s):
        if s[0] == '0':
            return 0

        prev2 = 1
        prev1 = 1

        for i in range(1, len(s)):
            curr = 0

            # Take one digit
            if s[i] != '0':
                curr += prev1

            # Take two digits
            if 10 <= int(s[i-1:i+1]) <= 26:
                curr += prev2

            prev2 = prev1
            prev1 = curr

        return prev1