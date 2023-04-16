#.~~~~~~~~~~.Task 1/Zadanie 1.~~~~~~~~~~.#
def Task1_mod(listt):
    outlist=listt
    index:int=0
    print("Before: ", listt)
    while index<len(listt)-1:
        index+=1
        outlist[index]+=outlist[index-1]
    print("After: ", outlist)  
    
# Funkcja, która jako argument przyjmuje listę liczb i zwraca 
# listę której i-ty element jest sumą wszystkich argumentów
# listy wejściowej do i-tego elementu włącznie, np.
# [2,2,2,2] -> [2,4,6,8]

#.~~~~~~~~~~.Task 2/Zadanie 2.~~~~~~~~~~.#    
def Task2(listt):
    outlist:list[int]=[]
    index:int=0
    print("Before: ", listt)
    for e in listt:
        if(len(outlist)==len(listt)-1):
            break
        else:
            index+=1
            outlist.append(listt[index]+e)
    print("After: ", outlist)
  
# Funkcja, która jako argument przyjmuje listę liczb
# i zwraca listę zawierającą sumę sąsiednich elementów
# listy wejściowej, np. [1,2,3,4] -> [3,5,7] 

#.~~~~~~~~~~.Task 3/Zadanie 3.~~~~~~~~~~.#  
def add(listt):
    index:int=0
    
    print(listt)
    
    for e in listt:
        if(index==len(listt)-1):
            break
        else:
            listt[index]+=listt[index+1]
            index+=1
            print(index, " list: ", listt)
    listt.pop(index)
            
    print(listt)
    
def zeroadding(listt):
    listt.append(0)
    listt.insert(0,0)

def Task3(number:int):
    defaultlist=[0,1,0]
    outlist=[]
    for e in range(number):
        zeroadding(defaultlist)
        add(defaultlist)
        
        outlist.append(defaultlist)
        print("Outlist: ",outlist)
        print("\n\n","Stage ",e+1,": ",defaultlist)
          
    print(outlist)
    
# Funkcja obliczająca trójkąt Pascala o zadanej głębokości
# w postaci listy zagnieżdżonej. Głębokość jest przyjmowana
# jako argument, np. pascal(3) -> [[1],[1,2,1],[1,3,3,1]]

#.~~~~~~~~~~.Task 4/Zadanie 4.~~~~~~~~~~.#

def Task4(listt):    
    horizontalresl:list[int]=[]
    verticalresl:list[int]=[]
    index:int=0
    
    for x in range(0,2):
        horizontalresl.append(0)
        for e in listt[x]:
            horizontalresl[-1]+=e   

    for ee in listt[0]:
        verticalresl.append(ee+listt[1][index])
        index+=1
    print("Result of horizontal adding is: ", horizontalresl)
    print("Result of vertical adding is: ", verticalresl)
        
Task4([[2,7,39,2,67,8],[2,3,6,3,5,6]])

# Funkcja, która jako argument przyjmuje tablicę dwuwymiarową 
# (listę zagnieżdżoną) i zwraca listę zawierającą sumę liczb
# z tablicy wejściowej według wskazanego kierunku, np.
# [[1,2,3],
#  [4,5,6]]
# dla kierunku 0 -> [6,15]
# dla kierunku 1 -> [5,7,9]
