class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test_dict = {}
        for num in nums:
            if test_dict.get(num):
                return True
            else:
                test_dict[num] = True
        return False