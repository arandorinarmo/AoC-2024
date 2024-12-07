import math

def primeFactors(n):
    primeFactors = []
     
    # Print the number of two's that divide n
    while n % 2 == 0:
        primeFactors.append(2)
        n = n // 2
         
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3,int(math.sqrt(n))+1,2):
         
        # while i divides n , print i ad divide n
        while n % i== 0:
            primeFactors.append(i)
            n = n // i
    if n > 2:
        primeFactors.append(n)
    
    return primeFactors


def refreshProgressBar(current, max, displayDetail = False):
    percent = (100 * current) // max

    bar = '█' * percent + ' ' * (100-percent)
    
    if (percent < 100):
        print (bar, percent, '%', " ({}/{})".format(current,max) if displayDetail else "", end='\r')
    else:
        print (bar, percent, '%', " ({}/{})".format(current,max) if displayDetail else "",)


def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def extract_bits(number, k, p):
    # Right shift the number by p-1 bits to get the desired bits at the rightmost end of the number
    shifted_number = number >> (p-1)
 
    # Mask the rightmost k bits to get rid of any additional bits on the left
    mask = (1 << k) - 1
    extracted_bits = shifted_number & mask
 
    # Convert the extracted bits to decimal
    extracted_number = bin(extracted_bits)[2:]
    decimal_value = int(extracted_number, 2)
 
    return decimal_value