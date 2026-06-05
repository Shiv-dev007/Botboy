from chat_history import history
def loadlist(user):
    try:
        new_content = []
        with open("todolist.txt","r") as file:
            content = file.readlines()
            if not content:
                reply = "Botboy: Your To-Do list is empty sir..."
                print(reply)
                history(user,reply)
                return
            reply = "Botboy: Your To-Do list.."
            history(user,reply)

            for task in content:
                print(task.strip())

            task_tobe_done = input("enter the task that to be ticked off sir....\n")

            for task in content:
                if task_tobe_done in task:
                    new_content.appendtask.strip()+"[Done]\n"
                else:
                    new_content.append(task)
            reply = "Botboy: To-Do list has been updated...sir"
            history(user,reply)

            with open("todolist.txt","w") as file:
                file.writelines(new_content)

            reply = "Botboy: new list has been loaded succesfully!!"
            history(user,reply)
    except FileNotFoundError:
        reply = "No such file in memory"
        history(user,reply)

    return reply

        
