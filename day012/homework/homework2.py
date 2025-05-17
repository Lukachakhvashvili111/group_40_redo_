def filter(user_list):
    result = []
    for i in user_list:
        if type(i) == int:
            result.append(i)
    return result

print(filter(16))