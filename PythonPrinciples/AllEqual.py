def all_equal(l):
    for char in l:
        if l[0] != char:
            return False
    return True