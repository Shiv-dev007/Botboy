from chat_history import history
def todolist(user):
    with open("todolist.txt","a") as file:
            count = 1
            while(True):
                task = input("Botboy: enter a task to list sir.....\n")
                # print(repr(task))
                file.write(f"{count}.{task} [ ]\n")
                count+=1
                # print("Debug: written task")
                ch = input("Botboy: Want to add more tasks...sir(in No only if not continuing or in yes only if continuing..)\n")
                try:
                    if ch.lower() == "no":
                        break
                except:
                    reply = "Invalid input sir...."
                    history(user,reply)
                    break
            reply = "Botboy: Tasks Added to To-do list Succesfully"
            history(user,reply)
    return reply
    
