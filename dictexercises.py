#.~~~~~~~~.Task 11.1/Zadanie 11.1.~~~~~~.#
def wordtodict(file):
    filex=open(file, encoding="utf-8")
    keys:list[str]=[]
    for e in filex:
        goodE=e.replace('\n','')
        keys.append(goodE)
    l=dict.fromkeys(keys)
    print(l)

# Write a function that reads the words in
# words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values
# are. Then you can use the in operator as a fast
# way to check whether a string is in the dictionary

#.~~~~~~.Task 11.2/Zadanie 11.2.~~~~~~.#

def invert_dict(d:dict):
    d2:dict={}
    for e in d:
        v=d.get(e)
        d2.setdefault(v,[]).append(e)    
    print(d2)

# Read the documentation of the dictionary
# method setdefault and use it to write a
# more concise version of invert_dict.

#.~~~~~~.Task 11.3/Zadanie 11.3.~~~~~~~~.#
def ack(m:int, n:int):
    result:list[int]=[0]
    if(m==0):
        result[-1]=n+1
        return result
    elif(m>0 and n==0):
        result.insert(0, m-1)
        print("result: ",result)
        return ack(m-1,1)    
    elif(m>0 and n>0):
        n=ack(m,n-1)
        return ack(m-1,n)

print(ack(1,0))

# Memoize the Ackermann function from Exercise 6.2
# and see if memoization makes it possible to
# evaluate the function with bigger arguments.
# Hint: no.
