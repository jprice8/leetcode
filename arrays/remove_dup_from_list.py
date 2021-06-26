from typing import List

def removeDuplicates(nums: List[int]) -> int:
    seen = []

    for idx, num in enumerate(nums):
        if num in seen:
            nums.pop(idx)
        
        # add to numbers to seen
        seen.append(num)

    ans = len(nums)
    return ans

if __name__ == '__main__':
    print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3]))