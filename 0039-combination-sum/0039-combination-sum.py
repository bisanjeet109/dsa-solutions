class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(index, path, total):
            if total == target:
                ans.append(path[:])
                return

            if total > target or index == len(candidates):
                return

            # Take current number
            path.append(candidates[index])
            backtrack(index, path, total + candidates[index])
            path.pop()

            # Skip current number
            backtrack(index + 1, path, total)

        backtrack(0, [], 0)
        return ans