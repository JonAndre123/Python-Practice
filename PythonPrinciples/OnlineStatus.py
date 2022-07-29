def online_count(status):
    number = 0
    for i in status.values():
        if i == 'online':
            number+=1
    return number