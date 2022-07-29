def add_dots(str):
    return ".".join(str)
    
def remove_dots(str):
    for i in range(len(str)):
        str = str.replace(".", '')
    return str
    
print(add_dots("hello"))
print(remove_dots("h.e.l.l.o"))
print(remove_dots(add_dots("hello")))