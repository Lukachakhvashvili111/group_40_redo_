list1 = ["luka",12,32.44,"ummm"]
list2 = []
def strangle(list1,list2):
    for i in list1:
        if type(i) == str:
            list2.append(i)
    return list2