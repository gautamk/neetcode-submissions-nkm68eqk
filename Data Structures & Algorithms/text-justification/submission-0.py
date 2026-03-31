class Solution:


    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current_line, current_line_char_count = [], 0
        lines = []
        i = 0
        while i < len(words):
            # current_line is complete
            spaces_between_words = len(current_line) # word_count
            word_count = spaces_between_words
            new_word = words[i]
            if current_line_char_count + spaces_between_words + len(new_word) <= maxWidth:
                current_line.append(words[i])
                current_line_char_count += len(words[i])
                i += 1
            else:
                extra_space = maxWidth - current_line_char_count
                spaces = extra_space // max(1, word_count - 1)
                remaining_spaces = extra_space % max(1, word_count - 1)
                
                for j in range(max(1, word_count - 1)):
                    current_line[j] += " " * spaces
                    if remaining_spaces > 0:
                        current_line[j] += " "
                        remaining_spaces -= 1
                lines.append("".join(current_line))
                current_line, current_line_char_count = [], 0 # reset
            
        last_line = " ".join(current_line)
        trail_space = maxWidth - len(last_line)
        lines.append(last_line + (" " * trail_space))
        
        return lines