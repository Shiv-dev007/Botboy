from chat_history import history
import random
def joke(user):
    jokes = [
    "Why was the math book sad? Because it had too many problems.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call fake spaghetti? An impasta.",
    "Why did the scarecrow get promoted? He was outstanding in his field.",
    "Why did the bicycle fall over? Because it was two-tired.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "Debugging is like being a detective in a movie where you're also the culprit.",
    "My computer sings sometimes. It's probably a Dell.",
    "What do you call a bear with no teeth? A gummy bear.",
    "Why was six afraid of seven? Because seven eight nine."
    ]
   
    reply = "Botboy:",random.choice(jokes)
    print(reply)
    history(user,reply)


    