def countAndSay(n: int) -> str:
    # The first char of our reselt is 1 so init the result
    s = '1'

    # As we have taken care of case 1 with n == 1 we start from 2
    while n > 1:

        i = 0
        # Create new string every iteration and assign it to our res
        ns = ''
        while i < len(s):
            #As we already included the first char so count = 1
            count = 1
            # Check if the prev char is same as next and keep count
            while i + 1 < len(s) and s[i] == s[i+1]:
                i += 1
                count += 1
            # Finally make the new string
            ns += str(count) + s[i]
            i += 1
        # Assign the newly made string for next iteration to s
        s = ns 
        n -= 1
    return s


print(countAndSay(4))