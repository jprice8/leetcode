def lengthOfLongestSubstring(s: str) -> int:
    # Approach #1. Brute Force. Naive approach.
    def check(start, end):
        chars = [0] * 128
        for i in range(start, end + 1):
            c = s[i]
            chars[ord(c)] += 1 # unicode point of integer. Same as ASCII value.
            if chars[ord(c)] > 1:
                return False 
        return True 

    n = len(s)

    res = 0
    for i in range(n):
        for j in range(i, n):
            if check(i, j):
                res = max(res, j - i + 1)
    return res


def concise(s):
    ans = 0
    sub = ''
    for char in s:
        if char not in sub:
            sub += char 
            ans = max(ans, len(sub))
        else:
            cut = sub.index(char)
            sub = sub[cut+1:] + char 
    return ans


if __name__ == '__main__':
    print(concise('abcdeafbdgcbb'))