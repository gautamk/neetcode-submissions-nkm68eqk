class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_dict = {}
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in n_dict:
                return [n_dict[diff][0], i]
            else:
                if n in n_dict:
                    n_dict[n].append(i)
                else:
                    n_dict[n] = [i]
        return []