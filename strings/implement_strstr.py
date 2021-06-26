def strStr(haystack: str, needle: str) -> int:
    """
    :type haystack: str
    :type needle: str
    :rtype: int 
    """
    # for i in range(len(haystack) - len(needle)+1):
    #     if haystack[i:i+len(needle)] == needle:
    #         return i 

    # return -1

    if needle not in haystack:
        return -1 

    else:
        return haystack.index(needle)


if __name__ == '__main__':
    print(strStr('teststring', 'ests'))
