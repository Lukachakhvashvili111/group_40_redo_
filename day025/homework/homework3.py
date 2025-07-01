name = ["luka","kela","kiki","kakalik","banani"]
def count(word):
    return word.count("k")

print(sorted(name,key = count,reverse = False))

