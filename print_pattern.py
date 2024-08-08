def print_pat(length):
    for i in range(length):
        for j in range(length):
            print("*", end="")
        print("")

def print_pate(length):
    for i in range(0, (length // 2) + 1):
        for j in range(0, length):
            if j == (length // 2) - i:
                print("*", end="")
            elif i == j == (length // 2):
                print(length, end="")
            elif j == (length // 2) + i:
                print("*", end="")
            else:
                print(" ", end="")
        print("")
    for i in range(0, (length // 2)):
        for j in range(0, length):
            if j == i + 1:
                print("*", end="")
            elif j == (length - 1) - i - 1:
                print("*", end="")
                break
            else:
                print(" ", end="")
        print("")

def print_pattern(length):
    if length < 1:
        return "Enter a length greater than or equal to 1"
    
    if isinstance(length, float) and length > 0:
        return "Enter a positive integer value"

    return print_p(int(length))

def print_p(length):
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

# Main program
for i in range(20):
    print(print_pattern(i))

print(print_pattern(1))

