# 14. Add Two Numbers
#
# Description:
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
# Example:
# Input: ["flower","flow","flight"]
# Output: "fl"
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
# Note:
# All given inputs are in lowercase letters a-z.
import os
from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        return os.path.commonprefix(strs)


def sol_1():
    sol_input = ["flower", "flow", "flight"]
    expect_output = "fl"
    sol_output = Solution().longestCommonPrefix(sol_input)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    assert sol_output == expect_output


def sol_2():
    sol_input = ["dog", "racecar", "car"]
    expect_output = ""
    sol_output = Solution().longestCommonPrefix(sol_input)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    assert sol_output == expect_output


def main():
    sol_1()
    sol_2()


main()
