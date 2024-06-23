class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker_sum = {}
        for i in range(len(nums)):
            if (nums[i] in tracker_sum):
                return [tracker_sum[nums[i]],i]
            else:
                tracker_sum[target-nums[i]] = i
                