from typing import List


class Solution:
    def move_zeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lastNonZeroIndex = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroIndex] = nums[i]
                lastNonZeroIndex += 1

        for j in range(len(nums)-1, lastNonZeroIndex - 1, -1):
            nums[j] = 0

if __name__ == '__main__':
    Solution().move_zeroes([5,0,3,2,0,1])
