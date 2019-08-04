# 15. 3Sum
#
# Description:
#
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum
# of zero.
#
# Example:
# Input: [-1, 0, 1, 2, -1, -4]
# Output:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
# Note:
# The solution set must not contain duplicate triplets.
from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()

        sol = set()

        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue

            d = {}

            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                else:
                    sol.add((v, x, -v - x))
        return list(sol)


def main():
    sol_input = [-1, 0, 1, 2, -1, -4]
    expect_output = [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
    sol_output = Solution().threeSum(sol_input)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    # assert set(sol_output) == set(expect_output)


main()
