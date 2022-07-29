def double_letters(str):
    for i in range(len(str)):
        if str[i] == str[i-1]:
            return True
    return False
    
double_letters("hello")
double_letters("world")