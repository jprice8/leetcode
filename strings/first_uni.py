# return index of first unique char in string. Else return -1
# e.x. input = 'leetcode'. output = 0

def return_first_uni(s: str) -> int:
    hashmap = {}
    ans = -1

    # create hashmap of unique chars with their index
    for idx, char in enumerate(s):
        if char in hashmap.keys():
            hashmap[char] = 'del'
        else:
            hashmap[char] = idx 


    for key, value in hashmap.items():
        if value != 'del':
            ans = value 
            return ans

    return ans

    
if __name__ == '__main__':
    print(return_first_uni('loveleetcode'))
