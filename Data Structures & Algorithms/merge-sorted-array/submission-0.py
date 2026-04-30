class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        n1 = [x for x in nums1]
        n2 = nums2

        i, j = m - 1, n - 1
        idx = m + n - 1

        while i >= 0 and j >= 0:
            if n1[i] > n2[j]:
                nums1[idx] = n1[i]
                i -= 1
            else:
                nums1[idx] = n2[j]
                j-=1
            idx -= 1
        
        while i >= 0 and idx >= 0:
            nums1[idx] = n1[i]
            i-=1
            idx-=1

        while j >= 0 and idx >= 0:
            nums1[idx] = n2[j]
            j-=1
            idx-=1
                



