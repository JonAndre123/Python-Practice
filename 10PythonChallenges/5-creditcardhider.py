userInput = input("Please enter your credit card number: ")

def creditCardHider(cc):
    return '*'*(len(cc)-4) + cc[-4:]

print("Hidden CC #: ", creditCardHider(userInput))



