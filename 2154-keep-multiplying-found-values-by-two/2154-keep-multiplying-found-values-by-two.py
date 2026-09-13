class Solution(object):
    def findFinalValue(self, nums, original):

        for i in range (len(nums)):
            if original==nums[i]:
                original = original*2 
                return self.findFinalValue(nums, original)
        return original 
            
                
