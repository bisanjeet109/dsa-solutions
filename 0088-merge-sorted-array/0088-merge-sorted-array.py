class Solution(object):
    def merge(self, nums1, m, nums2, n):
        ans = []

        for i in range (m):
            ans.append(nums1[i])



        for j in range (n):
            ans.append(nums2[j])

        
        
        ans.sort()

        for i in range (m+n):
            nums1[i] = ans[i]
