import math

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

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

with open('input.txt', "r") as file:

    total = 0
    for row in file.readlines():
        equation = row.split(":")
        result = int(equation[0])
        items = equation[1].split()

        bit = 0

        for i in range (0, int(math.pow(2,len(items)-1))):      
            checkSum = int(items[0])
            for j in range (1,len(items)):
                if ( extract_bits(bit, 1, j) == 0 ):
                    checkSum += int(items[j])
                else:
                    checkSum = checkSum * int(items[j])
   
            if (result == checkSum):
                total += checkSum
                break

            bit += 1
    print (total)