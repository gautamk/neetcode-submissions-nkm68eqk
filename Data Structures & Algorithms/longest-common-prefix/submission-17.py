class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        longest_prefix = ""
        for i in range(200):
            current_char = ""
            matching = True
            for string in strs:
                if i > len(string) - 1:
                    return longest_prefix
                elif not current_char:
                    current_char = string[i]
                else:
                    matching = (current_char == string[i])
                    if not matching:
                        return longest_prefix

            if matching and current_char:
                longest_prefix += current_char
                continue
            else:
                break
        return longest_prefix