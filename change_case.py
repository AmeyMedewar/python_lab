
def convert_to_capital_case(text):
    new_text = ''
    for character in text:
        if ord(character) in range(97,123):
            new_text += chr(ord(character)-32)
        else:
            new_text += character
    return new_text
    
def convert_to_small_case(text):
    new_text = ''
    for character in text:
        if ord(character) in range(65,91):
            new_text += chr(ord(character)+32)
        else:
            new_text += character
    return new_text
    
    
def convert_to_reverse_case(text):
    new_text = ''
    for character in text:
        if ord(character) in range(97,123):
            new_text += convert_to_capital_case(character)
        elif ord(character) in range(65,90):
            new_text += convert_to_small_case(character)
        else:
            new_text += character
    return new_text
    
def convert_to_zizag_case(text):
    text = list(text)
    if text[0] == convert_to_capital_case(text[0]):
        for i in range(0,len(text),2):
            text[i]=convert_to_capital_case(text[i]) 
        for i in range(1,len(text),2):
            text[i]=convert_to_small_case(text[i]) 

    else:
        for i in range(1,len(text),2):
            text[i]=convert_to_capital_case(text[i]) 
        for i in range(0,len(text),2):
            text[i]=convert_to_small_case(text[i]) 

    return ''.join(text)

def change_case( text , style ):
    if style in ['c','C']:
        return convert_to_capital_case(text)
    elif style in ['s','S']:
        return convert_to_small_case(text)
    elif style in ['r','R']:
        return convert_to_reverse_case(text)
    elif style in ['z','Z']:
        return convert_to_zizag_case(text)
    else:
        return 'ValueError:Enter a valid style'


print(change_case('sggsNED' , 'c'))
print(change_case('sggsNED' , 'S'))
print(change_case('sggsNED' , 'r'))
print(change_case('sggsNED' , 'Z'))
print(change_case('sggsNED' , 'o'))
print(change_case('SggsNED' , 'Z'))
    
