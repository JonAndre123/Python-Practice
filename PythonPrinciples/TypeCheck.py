def only_ints(num1, num2):
    if type(num1) == int and type(num2) == int:
        return True
    return False
    
only_ints(1,2)
only_ints(1, "hello")