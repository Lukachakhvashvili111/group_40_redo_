name = ["luka","nugzara","shevardeni"]
list1 = []
for i in name:
    item = ""
    for index in range(1,len(i),2):
        item += i[index]
    list1.append(item)

print(list1)