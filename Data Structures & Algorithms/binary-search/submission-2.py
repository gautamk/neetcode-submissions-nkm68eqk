class Solution:
    def search(self, nums: List[int], target: int) -> int:
        li, ri = 0, len(nums) - 1
        while li <= ri and ri < len(nums):
            mid = li + (ri - li) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                li = mid + 1
            elif nums[mid] > target:
                ri = mid - 1
        return -1 
        