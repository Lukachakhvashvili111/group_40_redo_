num = [12,32,1222,35,71]
def numm(ww):
    return(len(str(ww)))
print(sorted(num,key = numm,reverse = True))