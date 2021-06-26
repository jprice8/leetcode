def length_of_longest_sub(s):
    # check if s not in string
    # if true then add to string
    # if false then 

    sub = {}
    cur_sub_start = 0
    cur_len = 0
    longest = 0

    for idx, letter in enumerate(s):

        if letter in sub and sub[letter] >= cur_sub_start:
            # letter has been seen before so update its newest index
            cur_sub_start = sub[letter] + 1
            # now we have to update the current length
            cur_len = idx - sub[letter]
            # update that index for letter
            sub[letter] = idx
        
        else:
            # if not in sub, add to sub
            sub[letter] = idx
            cur_len += 1
            if cur_len > longest:
                longest = cur_len

    return longest


print(length_of_longest_sub('pwwkew'))