def topFive(a):
    b=[]
    b.append(max(a))
    a.remove(max(a))
    #print('b',b)
    #print('a',a)
    while len(b)<5 and len(a)>0:
        if b[len(b)-1]>max(a):
            b.append(max(a))
            #print('b+',b)
            a.remove(max(a))
            #print('a-',a)
        elif b[len(b)-1]==max(a):
            a.remove(max(a))
            #print('a--',a)
    return b

list1=[2,3,4,5,6,7,2,3,4,5,10]
list2=topFive(list1)
print(list2)
