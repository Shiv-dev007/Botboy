from chat_history import history
def showlist(user):
    try:
        with open("todolist.txt","r") as file:
            content = file.readlines()
            if not content:
                reply = "Botboy: Your To-Do list is empty sir..."
                history(user,reply)
                return
            reply = "Botboy: Your To-Do list.."
            history(user,reply)
            for task in content:
                print(task.strip())
    except FileNotFoundError:
        reply = "No such file in memory"
        history(user,reply)
        return reply

