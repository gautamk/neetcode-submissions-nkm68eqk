class Solution:
    def longestPalindrome(self, s: str) -> str:
        # transformed string
        # will always have odd number of characters
        # odd number of characters makes this computation simpler
        t = "#" + "#".join(s) + "#" 
        n = len(t)
        # length of palindromes at each index
        P = [0] * n
        # C_idx = center of the palindrome that pushed R_idx furthest right
        # R_idx = rightmost boundary reached so far (high watermark)
        C_idx, R_idx = 0, 0

        for i in range(n):
            mirror_idx = 2 * C_idx - i

            # if i is inside the coverage window ?
            if i < R_idx:
                # use the mirror value, 
                # but make sure it doesn't exceed the left boundary
                P[i] = min(R_idx - i, P[mirror_idx])
            
            while ( 
                # right expansion bounded by n
                (i + P[i] + 1) < n
                and 
                # left expansion bounded by 0
                (i - P[i] - 1) >= 0
                and 
                # left expansion t equals right expansion t
                t[(i + P[i] + 1)] == t[(i - P[i] - 1)]
            ):
                # then increment the palindrome size
                P[i] += 1
            
            # if i + P[i] is outside the coverage window
            if i + P[i] > R_idx:
                # update the coverage window
                C_idx = i
                R_idx = i + P[i]

        # find the index with the largest palindrome
        center_idx = max(range(n), key=lambda i: P[i])
        radius = P[center_idx]
        start_idx = (center_idx - radius) // 2 
        return s[start_idx: start_idx + radius]

