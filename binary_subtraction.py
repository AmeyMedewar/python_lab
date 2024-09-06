def binary_solution(bin1: str, bin2: str) -> str:
    # Determine the sign and ensure bin1 is the larger number
    if binary_to_int(bin1) >= binary_to_int(bin2):
        sign = ''
        result = binary_subtract(bin1, bin2)
    else:
        sign = '-'
        result = binary_subtract(bin2, bin1)
    
    # Remove leading zeros in the result
    result = result.lstrip('0') or '0'
    
    return sign + result

def binary_subtract(bin1: str, bin2: str) -> str:
    n1 = list(bin1)
    n2 = list(bin2)
    answer = []
    
    # Pad the shorter number with leading zeros
    max_len = max(len(n1), len(n2))
    n1 = ['0'] * (max_len - len(n1)) + n1
    n2 = ['0'] * (max_len - len(n2)) + n2

    borrow = 0
    for i in range(max_len - 1, -1, -1):
        x1 = int(n1[i])
        x2 = int(n2[i]) + borrow
        
        if x1 < x2:
            borrow = 1
            x1 += 2  # Since we are in binary, adding 2 instead of 10
        else:
            borrow = 0
        
        answer.append(x1 - x2)
    
    # Remove leading zeros in the result and reverse the answer list
    answer = [str(bit) for bit in reversed(answer)]
    return ''.join(answer).lstrip('0') or '0'

def binary_to_int(bin_str: str) -> int:
    return int(bin_str, 2)


