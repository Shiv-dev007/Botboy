def history(user_input, bot_output):
    with open("history.txt", "a") as file:
        file.write(f"User: {user_input}\nBot: {bot_output}\n\n")