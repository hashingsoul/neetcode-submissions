from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # This variable will store the longest common prefix
        res = ""

        # Traverse each character of the first string.
        # We use the first string as a reference because
        # the common prefix cannot be longer than it.
        for i in range(len(strs[0])):

            # Compare the current character with every string
            for s in strs:

                # Case 1:
                # If the current index is equal to the length of a string,
                # it means that string has ended.
                #
                # Example:
                # strs = ["flower", "flow"]
                #
                # At i = 4:
                # "flower"[4] = 'e'
                # "flow" has only indices 0-3.
                #
                # So we return the prefix found so far.

                # Case 2:
                # If the characters do not match,
                # the common prefix ends here.
                #
                # Example:
                # strs = ["flower", "flight"]
                #
                # At i = 2:
                # flower[2] = 'o'
                # flight[2] = 'i'
                #
                # Since 'o' != 'i',
                # return the prefix collected so far.
                if i == len(s) or s[i] != strs[0][i]:
                    return res

            # If all strings have the same character at index i,
            # append that character to the answer.
            res += strs[0][i]

        # If the loop finishes, the first string itself
        # is the longest common prefix.
        return res