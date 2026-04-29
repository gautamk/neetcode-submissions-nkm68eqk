class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = str(x)
        reverse = forward[::-1]
        return forward == reverse
        