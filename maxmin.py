def maxmin(filename:str):
    l:list=[]
    file=open(filename, encoding="utf-8")
    for e in file.readlines():
        e=e.replace(","," ")
        e=e.replace("-"," ")
        e=e.split()
        for ee in e:
            l.append(ee)
    sL=sorted(l)
    print("The smallest (min): ",sL[0])
    print("The largest (max): ",sL[-1])
    
# Write a function reads the numbers in file (filename)
# stores them in list (l), finds max and min of the 
# numbers and return the result.
#
# by checkthistape (https://github.com/checkthistape)
