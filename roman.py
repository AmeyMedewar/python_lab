def rom(text, text_base):
    text = to_decimal(text, text_base)
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    
    roman_numeral = ''
    i = 0
    
    while text > 0:
        count = text // val[i]
        roman_numeral += syms[i] * count
        text -= val[i] * count
        i += 1
    
    return roman_numeral

def to_decimal(text, text_base):
    if text_base < 2 or text_base > 36:
        return 'The specified base is invalid'
    
    bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    text = text.upper()
    sum = 0
    power = 0
    
    for char in reversed(text):
        if char not in bases[:text_base]:
            return 'Invalid character for the specified base'
        num = bases.index(char)
        sum += num * (text_base ** power)
        power += 1
    
    return sum



