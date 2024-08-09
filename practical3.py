def modulo1(numerator,denominator):
    if denominator==0:
        return "Please enter number greater than zero"
    elif numerator<denominator:
        return numerator
    else:
        while numerator>=denominator:
            numerator-=denominator
        return numerator

def modulo2(numerator,denominator):
    try:
        function_value= divmod(numerator,denominator)
    except:
        return "Please enter number greater than zero"
    return function_value[1]

def modulo3(numerator,denominator):
    if denominator==0:
        return "Please enter number greater than zero"
    elif numerator<denominator:
        return numerator
    else:
        original_denominator=denominator
        while numerator>=denominator:
            denominator+=denominator
        return numerator-(denominator-original_denominator)

def count(string,substring,flag=True):
    count=0
    if len(substring)>len(string):
        return count
    if flag==True:#flag equal to True means repetation is allowed 
        for i in range(len(string)-len(substring)):
            if string[i:i+len(substring)] == substring:
                count+=1
    else:
        i=0
        while i<len(string):
            if string[i:i+len(substring)]==substring:
                count+=1
                i+=len(substring)
            else:
                i+=1
    return count
    
def print_pattern(num):
    # assume user is always entering numeric value
    #if val < 1: enter a number >=1 fun should display
    #else it should say valid num
    ret=''
    s=str(num)
    l=s.partition('.')
    if num<1:
        ret= 'enter a number >=1'
    elif(l[1]=='.') and (int(l[-1])==0):
        num=int(s[0])
    elif(l[1]=='.') and (l[-1]!='0'):
        ret='enter a positive integer number'
        
    display_pattern(num)
    return ret


def display_pattern(length):
    column = (length * 2) + 3
    kite = (length * 2) + 1
    lst_row = length

    # Upper part of the kite
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 2):
            if j == (kite // 2) - i + 1:
                print("*", end="")
            elif j == (kite // 2) + i + 1:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    
    # Middle part with the number
    for i in range(1):
        for j in range(0, kite + 2):
            if j == i + 1:
                print("*", end="")
            elif j == ((kite + 2) // 2):
                print(length, end="")
            elif j == kite:
                print("*", end="")
                break
            else:
                print(" ", end="")
        print("")
    
    # Lower part of the kite
    for i in range(0, (kite // 2) - 1):
        for j in range(0, kite + 1):
            if j == i + 2:
                print("*", end="")
            elif j == (kite + 1) - i - 2:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    
    # Bottom rectangle
    for i in range(0, lst_row):
        for j in range(0, column):
            print("*", end="")
        print("")
    return ""



def display_pattern_q1(length):
    column = (length * 2) + 3
    kite = (length * 2) + 1
    lst_row = length

    # Upper part of the kite 
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 2):
            if j == (kite // 2) - i + 1:
                print("+", end="")
            elif j == (kite // 2) + i + 1:
                print("+", end="")
            else:
                print(" ", end="")
        print("")
    
    # Middle part with the number
    for i in range(1):
        for j in range(0, kite + 2):
            if j == i + 1:
                print("+", end="")
            elif j == kite:
                print("+", end="")
                break
            else:
                print(" ", end="")
        print("")
    
    # Lower part of the kite
    for i in range(0, (kite // 2)-1):
        for j in range(0, kite + 1):
            if j == i + 2:
                print("+", end="")
            elif j == (kite + 1) - i - 2:
                print("+", end="")
            else:
                print(" ", end="")
        print("")
        
    for j in range(0, kite + 1):
   
            if j == (kite + 1) - (kite // 2) - 1:
                print("-", end="")
            else:
                print(" ", end="")
    print("")
    return ""


def display_pattern_q2(length):
    column = (length * 2) + 3
    kite = (length * 2) + 1
    lst_row = length

    # Upper part of the kite 
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 2):
            if j == (kite // 2) - i + 1:
                print("+", end="")
            elif j == (kite // 2) + i + 1:
                print("+", end="")
            else:
                print(" ", end="")
        print("")
    
    # Middle part with the number
    for i in range(1):
        for j in range(0, kite + 2):
            if j == i + 1:
                print("+", end="")
            elif j == kite:
                print("+", end="")
                break
            else:
                print(" ", end="")
        print("")
    
    # Lower part of the kite
    for i in range(0, (kite // 2)):
        for j in range(0, kite + 1):
            if j == i + 2:
                print("-", end="")
            elif j == (kite + 1) - i - 2:
                print("-", end="")
            else:
                print(" ", end="")
        print("")

    
    return ""
    
    
     
    

            
        
            
            

