from typing import List

def plusOne(digits: List[int]) -> List[int]:
    n = len(digits)

    # move along the input array starting from the end
    for i in range(n):
        idx = n - 1 - i 
        # set all the nines at the of the array to zero
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits

    return [1] + digits


if __name__ == '__main__':
    print(plusOne([4,9,9,9]))