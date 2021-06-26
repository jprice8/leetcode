from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    shortest = min(strs, key=len)
    pf = []
    ans = []

    if not strs or strs == '':
        return str('') 
    for idx, val in enumerate(shortest):
        for i in strs:
            if i[idx] != val:
                return i[:idx]


print(longestCommonPrefix(['']))