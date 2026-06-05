from chat_history import history

def calculate(var_x,var_y,operation,user):
    var_1 = var_x
    var_2 = var_y
    op = operation
    if op == "+":
        reply = var_1+var_2

        history(user,reply)
    elif op == "-":
        reply = var_1-var_2

        history(user,reply)
    elif op == "*":
        reply = var_1*var_2

        history(user,reply)
    elif op == "/":
        if var_2 == 0:
            reply = "Divison by zero error"
    
            history(user,reply)
        else:
             reply= var_1/var_2
        
             history(user,reply)
    elif op == "%":
        reply = var_1%var_2

        history(user,reply)

    else:
        reply = "invalid input!!"

        history(user,reply)

    return reply