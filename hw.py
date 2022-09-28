l_1 = [1,11,14,5,8,9]
def less_10(l_1):
    l_2=[]
    for i in l_1:
        if i < 10:
            l_2.append(i)
    return l_2



    l_1 = [1,2,3,4,5,6]
l_2 = [3,4,5,6,7,8,10]
def merged_list(l_1, l_2):
    l_3 = l_1 + l_2
    l_3.sort()
    return l_3