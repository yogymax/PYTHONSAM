


values1 = [10,20,30]
values2 = [11,22,33]
values3 = [22,33,44]

mvalues1 = [values1,values2,values3]

values11 = [1,2,3]
values22 = [4,5,6]
values33 = [7,8,9]

mvalues2 = [values11,values22,values33]


def getvalues(row,col):
    return mvalues2[row][col]

print(mvalues1)
print(mvalues2)

def get_output(op):
    finalarray = []
    for ri,row in enumerate(mvalues1):
        values = []
        for ci,col in enumerate(row):
            #values.append(col+mvalues2[ri,ci])
            #print(col,getvalues(ri,ci))
            values.append(col*getvalues(ri,ci))
        finalarray.append(values)
    return  finalarray

get_output('+')




