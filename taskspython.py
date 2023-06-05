# 1. Napisz funkcję, która jako pierwszy argument przyjmuje
# listę liczb całkowitych a jako drugi argument pojedynczą
# liczbę. Funkcja powinna zwracać wszystkie liczby z listy
# które są podzielne przez drugi argument.
# Przykład: funkcja([1, 2, 3, 4, 5, 6], 2) --> [2, 4, 6]

def div(l:list[int], i:int):
    res:list[int]=[]
    for e in l:
        if(e%i==0):
            res.append(e)
    print(res)
# Input: div([1, 2, 3, 4, 5, 6], 2) Output: [2, 4, 6]
# Input: div([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], 2) Output: [2, 4, 6, 8, 10, 12]
  
# 2. Napisz funkcję, która usuwa ze zdania wybrane słowo.
# Pierwszym argumentem funkcji jest zdanie a drugim numer
# słowa do usunięcia.
# Przykład: funkcja("To jest zdanie", 1) --> "To zdanie"

def remove(s:str, i:int):
    sArr=s.split()
    if(len(sArr)>=i and i>=0):
        sArr.pop(i)
        for e in sArr:
            print(e, end=" ")     
    else:
        print("Sorry, your number is not valid!\n")
        return 1
# Input: remove("To jest zdanie", 1) Output: To zdanie
# Input: remove("Let's eat grandma", 2) Output: Let's eat 

# 3. Napisz funkcję, ktróra jako argumenty przyjmuje dwie
# listy liczb całkowitych i zwraca listę liczb które występują
# w pierwszej liście a nie występują w drugiej. Jeśli jakaś
# liczba występuje w pierwszej liście dwa razy a w drugiej
# tylko raz, też się liczy.
# Przykład: funkcja([1, 2, 2, 3, 4], [1, 2, 3]) --> [2,4]

def count(l1:list[int], l2:[list]):
    resD:dict={}
    l:list[int]=[]
    for el in l1:
        if(resD.setdefault(el, 0)!=None):
            g=resD.get(el)
            resD.update({el:g+1})
            if(resD.get(el)==2):
                l.append(el)
    for e in resD:
        if(resD.get(e)==1):
            for ee in l2:
                if(e==ee):
                    break
                if(ee==l2[-1] and e!=ee):
                    l.append(e)           
    print("Result:",l)
# Input: count([1, 2, 2, 3, 4], [1, 2, 3]) Output: [2, 4]
# Input: count([1, 2, 2, 3, 4, 4, 8, 3, 5, 2], [1, 2, 3]) Output: [2, 4, 3, 8, 5]   

# 4. Napisz funkcję, która jako argument przyjmuje listę liczb i
# na jej podstawie tworzy nową listę według poniższych zasad:
# 	- do nowej listy wstaw pierwszy i ostatni element listy wejściowej
# 	- odwróć kolejność pozostałych elementów w liście wejściowej
# 	- do nowej listy wstaw pierwszy i ostatni element zmodyfikowanej listy
# 	- powtarzaj operacje aż wszystkie elementy zotaną wykorzystane
# Po wykonaniu funkcji lista wejściowa powinna być nie zmodyfikowana.
# Przykład:
# S = [1,2,3,4,5,6]
# T = []
# 
# S = [2,3,4,5] => [5,4,3,2]
# T = [1,6]
# 
# S = [4,3] => [3,4]
# T = [1,6,5,2]
# 
# S = []
# T = [1,6,5,2,3,4]

def magic(l:list[int]):
    lR:list[int]=[]
    lCopy=l.copy()
    lSize=len(l)
    if(lSize%2!=0):
         lSize+=1
    for e in range(0, int(lSize/2)):
        lR.append(lCopy[0])
        lCopy.pop(0)
        if(len(lCopy)==0):
            break
        lR.append(lCopy[-1])
        lCopy.pop(-1)
        lCopy.reverse()   
    print(lR)
# Input: magic([1,2,3,4,5,6]) Output: [1, 6, 5, 2, 3, 4]
# Input: magic([1,2,3,4,5,6,7,8,9]) Output: [1, 9, 8, 2, 3, 7, 6, 4, 5]
    
# 5. Mamy ciąg znaków: '>' oznacza samochód jadący w prawo,
# '<' samochod jadący w lewo, '.' fotoradar. Jeśli samochód
# jedzie w kierunku fotoradaru zostanie zrobione zdjęcie.
# Proszę napisać funkcję, która policzy ilość zrobionych
# zdjęć dla danego ciągu. Przykład: funkcja(".><.>>.<<") --> 11

def cars(s:str):
    dots:int=0
    sList=list(s)
    for e in range(0, len(sList)):
        if(sList[e]=='>'):
            for ee in sList[e:]:
                if(ee=='.'):
                    dots+=1
        if(sList[e]=='<'):
            for ee in sList[:e]:
                if(ee=='.'):
                    dots+=1
    print(dots)
# Input: cars(".><.>>.<<") Output: 11       
# Input: cars(".><.>>.<<.<>.") Output: 22
