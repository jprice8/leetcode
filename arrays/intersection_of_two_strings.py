from typing import List

def intersect_of_two_strings(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []
    hashmap = {}

    # instantiate hashmap
    for i in nums1:
        if i in hashmap.keys():
            hashmap[i] += 1
        else:
            hashmap[i] = 1
    
    # iterate through nums 2 for matches and append to result
    for i in nums2:
        if i in hashmap.keys() and hashmap[i] > 0:
            hashmap[i] -= 1
            result.append(i)
        

    return result

if __name__ == '__main__':
    print(intersect_of_two_strings([1,2,1], [3,4,2,1,2]))