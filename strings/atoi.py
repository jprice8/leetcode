import re 

def myAtoi(s: str) -> int:
    if len(s) == 0: return 0
    ls = list(s.strip())

    sign = -1 if ls[0] == '-' else 0
    if ls[0] in ['-', '+'] : del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret*10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2**31, min(sign * ret,2**31-1))


# Use this one in interview
def googleRegexAnswer(s: str) -> int:
    """
    :type str:str
    :rtype: int
    """
    s = s.strip()
    s = re.findall('^[+\-]?\d+', s)

    try:
        res = int(''.join(s))
        MAX = 2147483647
        MIN = -2147483648

        if res > MAX:
            return MAX
        if res < MIN:
            return MIN
        return res 

    except:
        return 0

if __name__ == '__main__':
    print(googleRegexAnswer('-90234'))