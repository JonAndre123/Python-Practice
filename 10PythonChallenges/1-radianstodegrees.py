from cmath import pi
input = float(input("Please enter a number in radians to convert it to degrees: "))

def radtodeg(val):
    ans = (val*180)/pi
    return ans

print(radtodeg(input))
