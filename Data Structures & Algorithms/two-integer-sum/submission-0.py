class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        test_dict = {}
        for i,num in enumerate(nums):
            diff = target - num
            if diff in test_dict:
                return [test_dict[diff],i]
            test_dict[num] = i

