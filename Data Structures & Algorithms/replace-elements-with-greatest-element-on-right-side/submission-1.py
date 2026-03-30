class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        result = [0]*n
        current_max = -1
        for i in range(len(arr)-1, -1, -1):
            result[i] = current_max
            current_max = max(current_max, arr[i])
            

        result[-1] = -1 
        return result
