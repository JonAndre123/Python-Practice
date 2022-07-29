vowels = ["a", "e", "i", "o", "u"]
userInput = list(input("please enter a word: "))

def vowelCounter(word):
    count = 0
    for vowel in vowels:
        # count if found the vowels in input character set
        count += userInput.count(vowel)

    print(f"Total number of vowels in {userInput} is {count}")


vowelCounter(userInput)
