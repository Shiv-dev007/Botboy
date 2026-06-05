from chat_history import history
memory = {}
def remember_name(user):
        try:
                name = user.replace("my name is","").strip()
                with open("memory.txt","w") as file:
                        file.write(name)
        except FileNotFoundError:
             print("No such file in memory")

        