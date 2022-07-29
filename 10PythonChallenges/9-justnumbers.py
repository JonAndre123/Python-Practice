def l_int(l):
    fl=[]
    for i,e in enumerate(l):
        j=str(e)
    if j.startswith('-') and j[1:].isdigit():
        fl.append(e)
    elif j.isdigit():
        fl.append(e)
    return(fl)
li=['-1','a', 8,'b','2',6]
print(l_int(li))