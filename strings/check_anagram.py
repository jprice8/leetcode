import collections


def is_anagram(s1: str, s2: str) -> bool:
    hm1 = {}
    hm2 = {}


    for char in s1:
        if char in hm1.keys():
            hm1[char] += 1
        else:
            hm1[char] = 1

    for char in s2:
        if char in hm2.keys():
            hm2[char] += 1
        else:
            hm2[char] = 1


    if hm1 == hm2:
        return True 
    else:
        return False


def is_anagram_counter(s: str, t: str) -> bool:
    return collections.Counter(s)==collections.Counter(t)


if __name__ == '__main__':
    # print(is_anagram('rat', 'car'))
    print(is_anagram_counter('rat', 'car'))
