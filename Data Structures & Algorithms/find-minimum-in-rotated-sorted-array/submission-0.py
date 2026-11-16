class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < nums[left]:
                right = mid
                continue
            elif nums[mid] > nums[right]:
                left = mid + 1
                continue
            
            return nums[left]
        