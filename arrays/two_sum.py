from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
    hashmap = {}

    # iterate through nums array and check if target delta is
    # in hashmap
    for idx, num in enumerate(nums):
        # desired number
        delta = target - num
        if delta not in hashmap:
            hashmap[num] = idx
        else:
            return [hashmap[delta], idx]

    
if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
