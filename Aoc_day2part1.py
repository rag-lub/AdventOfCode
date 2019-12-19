lst1 = []
def Intcode(ls):
    for i in range(0,len(ls),4):
        if ls[i]==1:
            ls[ls[i+3]]=ls[ls[i+1]]+ls[ls[i+2]]
        elif ls[i]==2:
            ls[ls[i+3]]=ls[ls[i+1]]*ls[ls[i+2]]
        elif ls[i]==99:
            break  
        else:
            print('Unexpected')
    return ls
print(Intcode(lst1))

    