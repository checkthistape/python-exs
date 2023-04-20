# inp:str=input("Print your word:")
dictionary:str={}
# in_length:int=len(inp)
x:int = 1
def print_hist(di):
    for key in sorted(di):
        print(key, di[key])        
        
def letters(word):
    d = dict()
    for let in word:
        if let not in d:
            d[let]=1
        else:
            d[let]+=1
    return d    

def histogram_get(word):
    d=dict()
    for let in word:
        d[let]=d.get(let, 0)+1
    return d   


# fordictionary(dictionary, inp)

print("")

letters = letters("wooord")
print(1 in letters)

# print_hist(letters)
    
print("")    
print(letters)

hist_get = histogram_get("daaaaaemn")
print_hist(hist_get)

print("")  