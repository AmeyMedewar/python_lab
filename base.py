def base(text, text_base, output_base):
    def to_decimal(text, base):
        if base < 2 or base > 36:
            raise ValueError('The specified base is invalid')
        
        bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        text = text.upper()
        decimal_value = 0
        power = 0
        
        for char in reversed(text):
            if char not in bases[:base]:
                raise ValueError('Invalid character for the specified base')
            num = bases.index(char)
            decimal_value += num * (base ** power)
            power += 1
        
        return decimal_value

    def from_decimal(number, base):
        if base < 2 or base > 36:
            raise ValueError('The specified base is invalid')

        if number == 0:
            return '0'

        bases = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        result = ''
        
        while number > 0:
            result = bases[number % base] + result
            number //= base
        
        return result

    def to_roman(num):
        if num < 1 or num > 3999:
            raise ValueError('Roman numeral conversion supports numbers from 1 to 3999 only')
        
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
        
        while num > 0:
            count = num // val[i]
            roman_numeral += syms[i] * count
            num -= val[i] * count
            i += 1
        
        return roman_numeral

    if output_base == 'r' or output_base == 'R':
        decimal_number = to_decimal(text, text_base)
        return to_roman(decimal_number)
    else:
        if output_base < 2 or output_base > 36:
            raise ValueError('The specified base is invalid')
        
        decimal_number = to_decimal(text, text_base)
        return from_decimal(decimal_number, output_base)



