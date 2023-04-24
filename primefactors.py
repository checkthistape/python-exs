def distrib(n:int):
    res:list[int]=[]
    rep:dict[int]={}
    while(n>1):
        if(n%2==0):
            n=n/2
            res.append(2)
        if(n%3==0):
            n=n/3
            res.append(3)
        if(n%5==0):
            n=n/5
            res.append(5)
        if(n%7==0):
            n=n/7
            res.append(7)
        if(n%n==0):
            res.append(int(n))
            break
    for e in res:
        if(rep.setdefault(e, 0)!=None):
            g=rep.get(e)
            rep.update({e:g+1})
    return sorted(res), rep

# Write a function that distributes the number
# to the first factors and returns a dictionary
# containing the number of occurrences of each
# factor. Find what factor appears most often.
#
# Example:
# Input:
#   print(distrib(12))
# Ouput:
#   ([2, 2, 3], {2: 2, 3: 1})
#  * ^          ^---all number of the occurences
#    [__results of the dividing in steps
#
# by checkthistape (https://github.com/checkthistape)
