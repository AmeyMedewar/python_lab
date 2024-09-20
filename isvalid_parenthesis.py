def conj(sym):
    symbols = [']', '}', '>', ')']
    conjugates = ['[', '{', '<', '(']
    i = symbols.index(sym)
    return conjugates[i]
    
def check_validity1(text):
    valid_symbols = ['(', '<', '{', '[', ']', '}', '>', ')']
    stack1 =[]
    stack2 =[]
    for symbol in text:
        if symbol not in valid_symbols:
            return "Invalid text : invalid symbol Used"
        if symbol in valid_symbols[:4]:
            stack1.append(symbol)
        else:
            stack2.append(symbol)
            conjugate = conj(symbol)
            for i in range(len(stack1)-1,-1,-1):
                if stack1[i] == conjugate:
                    stack1.pop()
                    stack2.pop()
                    break
                else:
                    stack1.pop()
    if len(stack1)==0 and len(stack2)==0:
        return "Valid text"
    else:
        return "Invalid text : Imbalanced brackets"




def check_validity2(text):
    conjugates = {']':'[', '>':'<', '}':'{', ')':'('}
    valid_symbols = ['(', '<', '{', '[', ']', '}', '>', ')']
    stack =[]
    for symbol in text:
        if symbol not in valid_symbols:
            return "Invalid text : invalid symbol Used"
        if symbol in valid_symbols[:4]:
            stack.append(symbol)
        else:
            if len(stack)>0:
            
                if stack[-1] == conjugates.get(symbol):
                    stack.pop()
                else:
                    return  "Invalid text : Imbalanced brackets"
    if len(stack)==0:
        return "Valid text"
    else:
        return "Invalid text : Imbalanced brackets"
    
            



print(check_validity1('()'))
print(check_validity2('(>)>'))
print(check_validity1('([](}){)'))
print(check_validity2(')('))
print(check_validity1('(j)'))
print(check_validity2('(<(<>){}>)'))              
            
