name = ["luka","gela","gigi","gurami","bana"]
def count(word):
    return word.count("g")

print(sorted(name,key = count,reverse = True))

