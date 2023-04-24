def breakN(n:int):
    res:list[int]=[]
    resD:dict={}
    strNumb=str(n)
    for e in strNumb:
        res.append(int(e))
    for el in res:
        if(resD.setdefault(el, 0)!=None):
            g=resD.get(el)
            resD.update({el:g+1})
    print(resD)
    
# Write a function that counts
# the number of instances of 
# each digit in all numbers and
# locates it in a dictionary.
# 
# Example:
# Input:
#   breakN(7777)
# Ouput:
#   {7: 4}
#
# by checkthistape (https://github.com/checkthistape)
