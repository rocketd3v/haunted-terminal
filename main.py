import random

ghosts = ["watcher", "phantom"]     

class ghost:
    def __init__(self, name):
        self.name = name
        self.history = [ # referring to chat history
        ]
        self.responses = [ #fix this properly later
            "I have been waiting for you...",
            "You shouldn't have come here.",
            "Interesting... tell me more.",
            "I see you.",
            "The darkness remembers everything."
            ]
        
        self.empty_responses = [
            "Silence won't save you",
            "Speak louder, mortal.",
            "Did you hear that?"
        ]
        
        self.quit_responses = [
            "You have escaped me. for now...",
            "I shall return"
        ]
  
    def reply(self, message):
        self.history.append({"role": "user", "content": message})

        if len(message) == 0: # empty messages
            answer = random.choice(self.empty_responses)
        elif message == "/quit": 
            answer = random.choice(self.quit_responses)
        else: # normal message
            answer = random.choice(self.responses)

        self.history.append({"role": "ghost", "content": answer})
        print(f"{self.name}: {answer}")
        

    def reset(self):
        self.history.clear()

ghost = ghost(random.choice(ghosts)) # pick a random name for the ghost.

def main():
    while True:
        message = input("message: ")

        if message.startswith("/"):
            if message == "/help":
                print("Commands:\n/help - displays a list of available commands\n/reset or /clear - resets conversation history\n/quit - ends program")
            elif message == "/reset" or message == "/clear":
                ghost.reset()
            elif message == "/quit":
                ghost.reply(message)
                break
            else:
                print("Invalid command.")
        else:
            ghost.reply(message)

if __name__ == "__main__":
    main()
