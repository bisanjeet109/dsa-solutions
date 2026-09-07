class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        new_arr=[]

        for i in range (len(candies)):
            if candies[i] + extraCandies >= max(candies):
                new_arr.append(True)
            else:
                new_arr.append(False)
        return new_arr