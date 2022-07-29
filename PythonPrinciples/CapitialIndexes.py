def capital_indexes(str):
    list = []
    for i in range(len (str)):
        if str[i].isupper():
            list.append(i)
    return list