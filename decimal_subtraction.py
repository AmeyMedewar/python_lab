def solution(num1: str, num2: str) -> str:
    # Determine the sign and ensure num1 is the larger number
    if myint(num1) >= myint(num2):
        sign = ''
        result = subtract(num1, num2)
    else:
        sign = '-'
        result = subtract(num2, num1)
    
    # Remove leading zeros in the result
    result = result.lstrip('0') or '0'
    
    return sign + result

def subtract(num1: str, num2: str) -> str:
    n1 = list(num1)
    n2 = list(num2)
    answer = []
    
    # Pad the shorter number with leading zeros
    max_len = max(len(n1), len(n2))
    n1 = ['0'] * (max_len - len(n1)) + n1
    n2 = ['0'] * (max_len - len(n2)) + n2

    carry = 0
    for i in range(max_len - 1, -1, -1):
        x1 = myint(n1[i])
        x2 = myint(n2[i]) + carry
        
        if x1 < x2:
            carry = 1
            x1 += 10
        else:
            carry = 0
        
        answer.append(x1 - x2)
    
    # Remove leading zeros in the result and reverse the answer list
    answer = [str(digit) for digit in reversed(answer)]
    return ''.join(answer).lstrip('0') or '0'

def myint(str_number: str) -> int:
    return int(str_number)


