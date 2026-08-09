class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        ans = []

        for i, num in enumerate(nums):
            rem = target - num
            if rem in seen:
                ans = [i, seen[rem]]
                return sorted(ans)
            seen[num] = i  