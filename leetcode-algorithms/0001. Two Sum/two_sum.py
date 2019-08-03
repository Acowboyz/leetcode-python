# 1. Two Sum
#
# Description:
#
# Given an array of integers, return indices of the two numbers such that
# they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and
# you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}
        for index, num in enumerate(nums):
            if target - num in _dict:
                return [_dict[target - num], index]
            _dict[num] = index


def main():
    sol_input = [2, 7, 11, 15], 9
    expect_output = [0, 1]
    sol_output = Solution().twoSum([2, 7, 11, 15], 9)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    assert sol_output == expect_output


main()
