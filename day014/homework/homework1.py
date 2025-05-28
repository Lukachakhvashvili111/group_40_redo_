def odd(name):
    final__star=''
    for i in range(len(name)):
        if i % 2 == 0:
            final__star += name[i]
    return final__star
print(odd('luka'))