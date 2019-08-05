# 26. Remove Duplicates from Sorted Array
#
# Description:
#
# Given a sorted array nums, remove the duplicates in-place such that each
# element appear only once and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying
# the input array in-place with O(1) extra memory.
#
# Example 1:
# Given nums = [1,1,2],
#
# Your function should return length = 2, with the first two
# elements of nums being 1 and 2 respectively.
#
# It doesn't matter what you leave beyond the returned length.
#
# Example 2:
#
# Given nums = [0,0,1,1,1,2,2,3,3,4],
#
# Your function should return length = 5, with the first five
# elements of nums being modified to 0, 1, 2, 3, and 4 respectively.
#
# It doesn't matter what values are set beyond the returned length.
from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        last = 0
        for i in range(0, len(nums)):
            if nums[last] != nums[i]:
                last = last + 1
                nums[last] = nums[i]

        return last + 1


def main():
    sol_input = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expect_output = [0, 1, 2, 3, 4]
    sol_output = Solution().removeDuplicates(sol_input)

    print(f'Your input:\t{sol_input}')
    print(f'Output: \t{sol_output}')
    print(f'Expected: \t{expect_output}')

    assert sol_input[:sol_output] == expect_output


main()
