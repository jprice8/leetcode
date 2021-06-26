from typing import List

def singleNumber(nums: List[int]) -> int:
    seen = {} 
    ans = 0

    for num in nums:
        if not seen:
            seen[num] = 1
        else:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

    for key, value in seen.items():
        if value == 1:
            ans = key
            break
    return ans

if __name__ == '__main__':
    print(singleNumber([4,1,2,1,2]))