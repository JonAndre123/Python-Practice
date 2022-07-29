def consecutive_zeros(str):
    result = 0
    count = 0
    for i in str:
        if i == "0":
            count += 1
        else: 
            count = 0 
        result = max(result,count)
    return result

print(consecutive_zeros("100100001001110"))