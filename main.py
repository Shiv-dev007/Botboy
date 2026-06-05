import time
import re
from chat_history import history
import datetime
import random
from loadlist import loadlist
from jokes import joke
from opentodolist import showlist
from todolist import todolist
from open_website import open_webites
from calculate import calculate
from greeting import greet
from memory import remember_name
running = True


print(r"""
      
██████╗  ██████╗ ████████╗██████╗  ██████╗ ██╗   ██╗
██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔═══██╗╚██╗ ██╔╝
██████╔╝██║   ██║   ██║   ██████╔╝██║   ██║ ╚████╔╝
██╔══██╗██║   ██║   ██║   ██╔══██╗██║   ██║  ╚██╔╝
██████╔╝╚██████╔╝   ██║   ██████╔╝╚██████╔╝   ██║
╚═════╝  ╚═════╝    ╚═╝   ╚═════╝  ╚═════╝    ╚═╝

         Your Personal Assistant
      
Version 1.0
Type 'help' to see available commands.
""")

greet()
while(running):
    user = input("You: ")
    user = user.lower()

    # print(repr(user))

    number = [int(n) for n in re.findall(r'-?\d+', user)] #used regex method to identify numbers , or values in a string.

    if len(number) >= 2:# avoids crash
        var_x, var_y = number[0], number[1]


    if "your name" in user:
        reply = "Botboy: my name is botboy"
        print(reply)
        history(user, reply)

    elif "help" in user:
        reply = "Botboy: Displayed help menu"
        print(reply)
        history(user, reply)
        print("""
====================================
         BOTBOY HELP MENU
====================================

[GENERAL]
- hi
- joke
- time
- what is today's date

[MEMORY]
- my name is <name>
- what is my name
- erase memory file

[TODO LIST]
- to do list
- show list
- mark task done
- clear list

[WEB]
- open youtube
- open google
              
[HISTORY]
-Display History
-Delete History              

[SYSTEM]
- exit
- quit
- bye

====================================
""")

    elif "my name is" in user:
        remember_name(user)
        reply = "Botboy: i have remembered your name"
        print(reply)
        history(user,reply)

    elif "what is my name" in user or "whats my name" in user:
        try:
            with open("memory.txt" , "r") as file:
                Name = file.read()
                if Name == "":
                    reply = "Botboy: No such entry in directory"
                    print(reply)
                    history(user,reply) 
                else:
                    reply = f"Botboy: Your name is {Name}...Sir"
                    print(reply)
                    history(user,reply) 
        except FileNotFoundError:
            reply = "No memory found sir...."
            print(reply)
            history(user,reply)

    elif user in ["erase","remove","remove memoryfile","erase memoryfile","removememoeryfile","remove memory file","erasememoryfile","erase memory file"]:
        with open("memory.txt","w") as file:
            pass

        reply = "Botboy: Memoryfile erased succesfully sir..."
        print(reply)
        history(user,reply) 

    elif user in ["what is todays date","whats todays date","whats is the date","whats the date","what is today's date","whats today's date"]:
        today = datetime.date.today()
        reply = f"Botboy: Today is {today}"
        print(reply)
        history(user,reply) 

    elif "time" in user:
        reply = f"Botboy: It is {time.ctime()} "
        print(reply)
        history(user,reply) 

    elif "joke" in user:
        reply = joke(user)
        print(reply)
         

    elif user in ["hi","hello","hey"]:
       Greet = [
           "hello!",
           "how are you sir...",
           "hey there",
           "hi",
           "its good to see you back again!!..,sir",
           "Glad you're back!",
           "Nice to see you again!"
       ]
       reply = f"Botboy: {random.choice(Greet)}"
       print(reply)
       history(user,reply) 


    elif user in ["to do list","make a to do list","make a to dolist","make a list","todolist","todo list","to dolist","list"]:
        reply = todolist(user)
        print(reply) 

    elif user in ["open list","openlist","show to do list",
              "show todo list","show to dolist",
              "show list","showlist","open to do list"]:
                # print("DEBUG: Reached showlist block")
                reply = showlist(user)
                print(reply)
            
    elif"open" in user:
        reply = open_webites(user)
        if reply:
            print(reply)

    elif user in ["clear list","remove list","delete list"]:
        ch = input("Botboy: Are you sure? (yes/no): ")

        if ch.lower() == "yes":
            with open("todolist.txt","w") as file:
                pass

            reply = "Botboy: To-Do list cleared successfully sir..."
            print(reply)
            history(user,reply)  

        else:
            reply = "Botboy: Operation cancelled."
            print(reply)
            history(user,reply)      

    elif user in ["mark","mark task done","load list and mark it done","mark the list done","mark the task done in to do list","mark the to do list"]:
        reply = loadlist(user)
        print(reply)

    elif "fine" in user:
        reply = "Botboy: Glad to hear that!!"
        print(reply)
        history(user,reply) 

    elif "+" in user or "add" in user or "addition" in user or "sum" in user: 
        if len(number) < 2:
            reply = "Botboy: Please provide suitable value to calculate"
            print(reply)
            history(user,reply) 
        else:
            answer = calculate(var_x,var_y,"+",user)
            reply = f"Botboy: Your answer {answer}"
            print(reply)
            history(user, reply)

    elif "-" in user or "diff" in user or "diffrentiation" in user or "diffrence" in user:
        if len(number) < 2:
                reply = "Botboy: Please provide suitable value to calculate"
                print(reply)
                history(user,reply) 
        else:
            answer = calculate(var_x,var_y,"-",user)
            reply = f"Botboy: Your answer {answer}"
            print(reply)
            history(user, reply)
            

    elif "*" in user or "multiply " in user or "mul" in user or "product" in user or "multiplication" in user:
        if len(number) < 2:
            reply = "Botboy: Please provide suitable value to calculate"
            print(reply)
            history(user,reply) 
        else:
            answer = calculate(var_x,var_y,"*",user)
            reply = f"Botboy: Your answer {answer}"
            print(reply)
            history(user, reply)

    elif "/" in user or "divide" in user or "division" in user:
        if len(number) < 2:
            reply = "Botboy: Please provide suitable value to calculate"
            print(reply)
            history(user,reply) 
        else:
            answer = calculate(var_x,var_y,"/",user)
            reply = f"Botboy: Your answer {answer}"
            print(reply)
            history(user, reply)

    elif "%" in user or "remainder" in user or "modulus" in user:
        if len(number) < 2:
            reply = "Botboy: Please provide suitable value to calculate"
            print(reply)
            history(user,reply) 
        else:
            answer = calculate(var_x,var_y,"%",user)
            reply = f"Botboy: Your answer {answer}"
            print(reply)
            history(user, reply)

    elif "how are you" in user:
        reply = "Botboy: I am fine, What about you?"
        print(reply)
        history(user,reply) 

    elif user in ["good bye","quit","exit","bye bye", "bye","tata"]:
        reply = "Botboy: Had a great time talking to you!, can call me anyime for any help"
        print(reply)
        history(user,reply) 
        running = False 

    elif user in ["show me history", "display history"]:
        try:
            with open("history.txt", "r") as file:
                content = file.readlines()

            reply = "Botboy: Your Chat history Sir...."
            print(reply)

            for l in content:
                print(l.strip())

        except FileNotFoundError:
            reply = "Botboy: File not found!!"
            print(reply)
            history(user, reply)

    elif user in ["delete" , "delete history"]:
        with open("history.txt","w") as file:
            pass

        reply = "Botboy: your Chat history Deleted succesfully"
        print(reply)
        # history(user,reply)

    else:
        reply = "Botboy: Not able to understand right now!!"
        print(reply)
        history(user,reply) 