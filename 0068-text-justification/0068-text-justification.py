class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            line_len = len(words[i])
            j = i + 1

            # Find words that fit in the current line
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1

            num_words = j - i

            # Last line or only one word
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                total_chars = sum(len(word) for word in words[i:j])
                total_spaces = maxWidth - total_chars
                gaps = num_words - 1

                space_each = total_spaces // gaps
                extra = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += words[i + k]
                    line += " " * (space_each + (1 if k < extra else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result