class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            # len(current_line) = minimum spaces needed (1 per gap including before new word)
            if current_length + len(current_line) + len(word) > maxWidth:
                spaces_needed = maxWidth - current_length
                gaps = len(current_line) - 1

                if gaps == 0:  # single word: pad right
                    lines.append(current_line[0] + ' ' * spaces_needed)
                else:
                    space, extra = divmod(spaces_needed, gaps)
                    line = ''
                    for i, w in enumerate(current_line[:-1]):
                        line += w + ' ' * space + (' ' if i < extra else '')
                    lines.append(line + current_line[-1])

                current_line, current_length = [word], len(word)
            else:
                current_line.append(word)
                current_length += len(word)

        # Last line: left-justified, trailing spaces only
        last = ' '.join(current_line)
        lines.append(last + ' ' * (maxWidth - len(last)))

        return lines