def reverse(num):
    x = 0

    while num > 0:
        rem = num % 10
        x = (x * 10) + rem 
        num = num // 10

    return x
    
if __name__ == '__main__':
    print(reverse(321))
