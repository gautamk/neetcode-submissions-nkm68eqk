class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        update_index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[update_index] = nums[i]
                update_index+=1
        return update_index