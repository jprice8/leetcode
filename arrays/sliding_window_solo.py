def sliding_window_hashset(s: str) -> int:
    chars = [0] * 128
    left = right = 0
    longest = 0
    while right < len(s):
        r = s[right]
        chars[ord(r)] += 1

        while chars[ord(r)] > 1:
            l = s[left]
            chars[ord(l)] -= 1
            left += 1

        longest = max(longest, right - left + 1)

        right += 1
    return longest

def sliding_window_hashmap(s: str) -> int:
    n = len(s)
    ans = 0
    mp = {}

    i = 0
    for j in range(n):
        if s[j] in mp:
            i = max(mp[s[j]], i)

        ans = max(ans, j - i + 1)
        mp[s[j]] = j + 1

    return ans

def sliding_window_hashmap_table(s: str) -> int:
    # Direct Address Table
    chars = [0] * 128
    left = right = 0
    longest = 0

    while right < len(s):
        r = s[right]

        index = chars[ord(r)]
        if index != None and index >= left and index < right:
            left = index + 1

        longest = max(longest, right - left + 1)

        chars[ord(r)] = right 
        right += 1

    return longest

if __name__ == '__main__':
    # print(sliding_window_hashset('pwwkew'))
    print(sliding_window_hashmap_table('au'))