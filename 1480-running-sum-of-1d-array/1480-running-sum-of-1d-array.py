class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        arr= 0
        for i in range(len(nums)):
            arr += nums[i]
            nums[i]=arr
        return(nums)

        

        