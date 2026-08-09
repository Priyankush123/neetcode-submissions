class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for val in freq.values():
            if val > 1:
                return True
        return False        