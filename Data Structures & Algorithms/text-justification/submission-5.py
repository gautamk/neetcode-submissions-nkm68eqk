class Solution:

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        maxWidth = maxWidth
        lines = []
        current_line = []
        current_line_len = 0
        current_word_count = 0
        can_add_word_to_line = lambda word: current_line_len + current_word_count + len(word) <= maxWidth
        for word in words:
            if can_add_word_to_line(word):
                current_line.append(word)
                current_line_len += len(word)
                current_word_count += 1
            else:
                # the number of empty spaces to be added
                spaces_needed = maxWidth - current_line_len
                # the gaps between words where it can be distributed
                gaps = current_word_count - 1
                
                if gaps == 0 and current_word_count == 1: 
                    # single word pad right
                    lines.append(current_line[0] + (' ' * spaces_needed))
                else:
                    # spaces needed for all words except last, last word doesn't have space suffix
                    # word indices which need extra spaces, extra spaces are distributed greedily
                    # so we distribute spaces to the first X instances (X == extras here) 
                    spaces, extras = divmod(spaces_needed, gaps)
                    line = ''
                    for i, w in enumerate(current_line[:-1]):
                        line += w + ' ' * spaces + (' ' if i < extras else '')
                    
                    # attach the last word not included in the spacing
                    lines.append(line + current_line[-1])

                # We're not adding the current word
                # next line should have the current word
                # resetting for the next line
                current_line = [word]
                current_line_len = len(word)
                current_word_count = len(current_line)
        
        last_line = ' '.join(current_line)
        lines.append(last_line + ' ' * (maxWidth - len(last_line)))

        return lines
            

