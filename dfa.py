def ends_with_b(text):
    if q0(text):
        return "Accepted"
    else:
        return "Rejected"
def q0(text):#b
    if text[0] =='b':
        if len(text) ==1:
            return True
        else:
            return q0(text[1:])
    elif text[0] =='a':
        if len(text) ==1:
            return False
        else:
            return q1(text[1:])
    else:
        return False

def q1(text):#a
    if text[0] =='a':
        if len(text) ==1:
            return False
        else:
            return q1(text[1:])
    elif text[0] =='b':
        if len(text) ==1:
            return True
        else:
            return q0(text[1:])
    else:
        return False

print(ends_with_b("bababaabbaba"))
print(ends_with_b("abababab"))

    
