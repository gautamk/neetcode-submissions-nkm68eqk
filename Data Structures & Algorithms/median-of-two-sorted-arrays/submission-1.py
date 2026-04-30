class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array to minimize iterations.
        small, large = (nums1, nums2) if len(nums1) < len(nums2) else (nums2, nums1)
        total = len(nums1) + len(nums2)
        is_even = total % 2 == 0
        # The left half of the combined sorted array contains `left_half_size` elements.
        left_half_size = total // 2

        # Binary search bounds on small (indices into small for the cut position).
        lo, hi = 0, len(small) - 1

        while True:
            # small_cut is the last index in small included in the left partition (0-based).
            # So we take small_cut+1 elements from small.
            small_cut = (lo + hi) // 2
            # large_cut is the last index in large included in the left partition.
            # left_half_size - (small_cut+1) - 1 = left_half_size - small_cut - 2 elements come from large.
            large_cut = left_half_size - small_cut - 2

            # Edge values: use -inf/+inf when the cut is at the boundary
            # (no elements on that side), so comparisons still work correctly.
            small_left  = small[small_cut]     if small_cut >= 0               else float("-inf")
            small_right = small[small_cut + 1] if small_cut + 1 < len(small)   else float("inf")
            large_left  = large[large_cut]     if large_cut >= 0               else float("-inf")
            large_right = large[large_cut + 1] if large_cut + 1 < len(large)   else float("inf")

            if small_left <= large_right and large_left <= small_right:
                # Valid partition: every left-half element <= every right-half element.
                if is_even:
                    # Median is average of the two middle values:
                    # largest on the left and smallest on the right.
                    return (max(small_left, large_left) + min(small_right, large_right)) / 2
                else:
                    # Median is the smallest element on the right side.
                    return min(small_right, large_right)
            elif small_left > large_right:
                # small's left boundary is too large; move small's cut left.
                hi = small_cut - 1
            elif large_left > small_right:
                # large's left boundary is too large; move small's cut right
                # (which shifts more elements from large to the left partition).
                lo = small_cut + 1
