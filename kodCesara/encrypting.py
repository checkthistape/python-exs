alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_uppercase=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alphabet_polish=['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']
alphabet_polish_uppercase=['A', 'Ą', 'B', 'C', 'Ć', 'D', 'E', 'Ę', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'Ł', 'M', 'N', 'Ń', 'O', 'Ó', 'P', 'R', 'S', 'Ś', 'T', 'U', 'W', 'Y', 'Z', 'Ź', 'Ż']

def language():
        print("")
        print(".~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.")
        print("")
        print("			  Hello, select your language:				")
        print("")
        print("			  1 -- ENG, 2 -- POL, 3 -- UKR								")
        print("")

def cin():
    
    language()
    lang=input()
        
    while(lang=='' or lang=="" or lang!="3" or lang!="1" or lang!="2"):    
        if(lang=='1'):
            print("You have selected English")
            break
        elif(lang=='2'):
            print("You have selected Polish")
            break
        elif(lang=='3'):
            print("You have selected Ukranian")
            break
        elif(lang==''):
            print("You have no selected language, please try again")
            lang=input()
        elif(lang=="exit"):
            end()
            exit()
            break
        else:
            print("Undefined language, please try again")
            lang=input()
    
    print("")
    
    print("Select action encrypt -- 1 or decrypt -- 2:  ")
    enc_or_dec=int(input())
    
    if(enc_or_dec==1):
            stroke=input("Please write your word or sentence(s) here: ")
            szyfr_num=int(input("Please write your right shift in number(s): "))
            
            line_arr=list(stroke)
            
            print("")
            
            encrypt(line_arr, szyfr_num, stroke)            
    
    
    if(enc_or_dec==2):
            stroke=input("Please write your word or sentence(s) here: ")
            szyfr_num=int(input("Please write your right shift in number(s): "))
            
            line_arr=list(stroke)
            
            print("")
            decrypt(line_arr, szyfr_num, stroke)
        
    
def end():
    print("")
    print("")
    print("				Good evening, bye bye!)")
    print(".~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~.")
    
def again():
    next_step:int = 0
    print("")
    while(next_step==0):
        print("Would you like to start program again?")
        answer=input('YES -- y and NO -- n:  ')
        if(answer=='y' or answer=='yes' or answer=='1'):
            cin()
            next_step=1
            
        elif(answer=="n" or answer=="no" or answer == "0"):
            end()
            next_step=1



def encrypt(line_arr, szyfr_num, stroke):
    s:str=""
    x:int=0
    size_line=len(line_arr)
    
    while(x<size_line):
        if(x>size_line):
            break
        
        match line_arr[x]:
            case 'a':  
                line_arr[x]=alphabet[(0+szyfr_num)%26]
            case 'ą':  
                line_arr[x]=alphabet_polish[1+szyfr_num%33]    
            case 'b':
                line_arr[x]=alphabet[(1+szyfr_num)%26]
            case 'c':
                line_arr[x]=alphabet[(2+szyfr_num)%26]
            case 'ć':
                line_arr[x]=alphabet_polish[5%33]    
            case 'd':
                line_arr[x]=alphabet[(3+szyfr_num)%26]
            case 'e':
                line_arr[x]=alphabet[(4+szyfr_num)%26]
            case 'ę':
                line_arr[x]=alphabet_polish[8%26]    
            case 'f':
                line_arr[x]=alphabet[(5+szyfr_num)%26]
            case 'g':
                line_arr[x]=alphabet[(6+szyfr_num)%26]
            case 'h':
                line_arr[x]=alphabet[(7+szyfr_num)%26]
            case 'i':
                line_arr[x]=alphabet[(8+szyfr_num)%26]
            case 'j':
                line_arr[x]=alphabet[(9+szyfr_num)%26]
            case 'k':
                line_arr[x]=alphabet[(10+szyfr_num)%26]
            case 'l':
                line_arr[x]=alphabet[(11+szyfr_num)%26]
            case 'ł':
                line_arr[x]=alphabet_polish[16+szyfr_num]    
            case 'm':
                line_arr[x]=alphabet[(12+szyfr_num)%26]
            case 'n':
                line_arr[x]=alphabet[(13+szyfr_num)%26]
            case 'ń':
                line_arr[x]=alphabet_polish[19+szyfr_num]    
            case 'o':
                line_arr[x]=alphabet[(14+szyfr_num)%26]
            case 'ó':
                line_arr[x]=alphabet_polish[21+szyfr_num]    
            case 'p':
                line_arr[x]=alphabet[(15+szyfr_num)%26]
            case 'q':
                line_arr[x]=alphabet[(16+szyfr_num)%26]
            case 'r':
                line_arr[x]=alphabet[(17+szyfr_num)%26]
            case 's':
                line_arr[x]=alphabet[(18+szyfr_num)%26]
            case 'ś':
                line_arr[x]=alphabet_polish[25+szyfr_num]    
            case 't':
                line_arr[x]=alphabet[(19+szyfr_num)%26]
            case 'u':
                line_arr[x]=alphabet[(20+szyfr_num)%26]
            case 'v':
                line_arr[x]=alphabet[(21+szyfr_num)%26]
            case 'w':
                line_arr[x]=alphabet[(22+szyfr_num)%26]
            case 'x':
                line_arr[x]=alphabet[(23+szyfr_num)%26]
            case 'y':
                line_arr[x]=alphabet[(24+szyfr_num)%26]
            case 'z':
                line_arr[x]=alphabet[(25+szyfr_num)%26]
            case 'ź':
                line_arr[x]=alphabet_polish[(30+szyfr_num)%32]
            case 'ż':
                line_arr[x]=alphabet_polish[(31+szyfr_num)%32]     
            case _:
                print(" ") 
        x=x+1
    
    print("Your default text: ", stroke)
    encrypted:str=s.join(line_arr)
    print("Your decrypted text: ", encrypted)
    again()
    
def decrypt(line_arr, szyfr_num, stroke):
    s:str=""
    x:int=0
    size_line=len(line_arr)
    
    while(x<size_line):
        if(x>size_line):
            break
        
        match line_arr[x]:
            case 'a':  
                line_arr[x]=alphabet[(26-szyfr_num)%26]
            case 'ą':  
                line_arr[x]=alphabet_polish[1+szyfr_num%33]    
            case 'b':
                line_arr[x]=alphabet[(27-szyfr_num)%26]
            case 'c':
                line_arr[x]=alphabet[(28-szyfr_num)%26]
            case 'ć':
                line_arr[x]=alphabet_polish[5%33]    
            case 'd':
                line_arr[x]=alphabet[(29-szyfr_num)%26]
            case 'e':
                line_arr[x]=alphabet[(30-szyfr_num)%26]
            case 'ę':
                line_arr[x]=alphabet_polish[8%26]    
            case 'f':
                line_arr[x]=alphabet[(31-szyfr_num)%26]
            case 'g':
                line_arr[x]=alphabet[(32-szyfr_num)%26]
            case 'h':
                line_arr[x]=alphabet[(33-szyfr_num)%26]
            case 'i':
                line_arr[x]=alphabet[(34-szyfr_num)%26]
            case 'j':
                line_arr[x]=alphabet[(35-szyfr_num)%26]
            case 'k':
                line_arr[x]=alphabet[(36-szyfr_num)%26]
            case 'l':
                line_arr[x]=alphabet[(37-szyfr_num)%26]
            case 'ł':
                line_arr[x]=alphabet_polish[16+szyfr_num]    
            case 'm':
                line_arr[x]=alphabet[(38-szyfr_num)%26]
            case 'n':
                line_arr[x]=alphabet[(39-szyfr_num)%26]
            case 'ń':
                line_arr[x]=alphabet_polish[19+szyfr_num]    
            case 'o':
                line_arr[x]=alphabet[(40-szyfr_num)%26]
            case 'ó':
                line_arr[x]=alphabet_polish[21+szyfr_num]    
            case 'p':
                line_arr[x]=alphabet[(41-szyfr_num)%26]
            case 'q':
                line_arr[x]=alphabet[(42-szyfr_num)%26]
            case 'r':
                line_arr[x]=alphabet[(43-szyfr_num)%26]
            case 's':
                line_arr[x]=alphabet[(44-szyfr_num)%26]
            case 'ś':
                line_arr[x]=alphabet_polish[25+szyfr_num]    
            case 't':
                line_arr[x]=alphabet[(45-szyfr_num)%26]
            case 'u':
                line_arr[x]=alphabet[(46-szyfr_num)%26]
            case 'v':
                line_arr[x]=alphabet[(47-szyfr_num)%26]
            case 'w':
                line_arr[x]=alphabet[(48-szyfr_num)%26]
            case 'x':
                line_arr[x]=alphabet[(49-szyfr_num)%26]
            case 'y':
                line_arr[x]=alphabet[(50-szyfr_num)%26]
            case 'z':
                line_arr[x]=alphabet[(51-szyfr_num)%26]
            case 'ź':
                line_arr[x]=alphabet_polish[(30+szyfr_num)%32]
            case 'ż':
                line_arr[x]=alphabet_polish[(31+szyfr_num)%32]     
            case _:
                print(" ") 
        x=x+1
    
    print("Your default text: ", stroke)
    print("Your encrypted text: ", s.join(line_arr))
    again()


cin()
