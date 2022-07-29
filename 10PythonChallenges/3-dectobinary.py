#Write a function in Python that accepts a decimal number and returns the equivalent binary number. 
#To make this simple, the decimal number will always be less than 1,024, 
#so the binary number returned will always be less than ten digits long.

def decimalToBinary(val):
    return "{0:b}".format(int(val))

if __name__ == '__main__':
    print(decimalToBinary(8))
    print(decimalToBinary(18))
    print(decimalToBinary(7))