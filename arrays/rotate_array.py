from typing import List

def rotate_array(nums: List[int], k: int) -> None:

    # if k > 0:
    #     tmp = nums[k + 1:]
    #     del nums[k + 1:]
    #     nums = tmp + nums

    # print(nums)

    # speed up the rotation
    k %= len(nums)

    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]

if __name__ == '__main__':
    print(rotate_array([1, 2, 3, 4, 5, 6, 7], 3))