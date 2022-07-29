userInput = input("Please enter a word: ")
def XOCounter(str):
    xCount = str.count("x")
    oCount = str.count("o")
    if(xCount==oCount):
        return True
    return False

print(XOCounter(userInput))

