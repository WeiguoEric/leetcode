class Solution:
    def bubble_sort(self, nums: List[int]) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
        return nums[-1]


    def dominantIndex(self, nums: List[int]) -> int:
        nums_ = list(nums)
        maxi = self.bubble_sort(nums_)
        count = 0
        for i in range(len(nums)):
            if nums[i] * 2 <= maxi:
                count += 1
            if nums[i] == maxi:
                index = i
        if count == len(nums) - 1:
            return index
        else:
            return -1
