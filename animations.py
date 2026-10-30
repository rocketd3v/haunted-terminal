import random
from cerebras.cloud.sdk import AsyncCerebras
import os
import asyncio


ghosts = ["watcher", "phantom"] 

class ghost:
    def __init__(self, name):
        self.name = name
        self.history = [ # referring to chat history
        ]
        self.personality = f"You are the {name}, You speak in a spooky / cryptic way. dont make your responses too long, you live within the users terminal, never claim to actually be able to access / manage then users files"
        self.client = AsyncCerebras(api_key=os.getenv("CEREBRAS_API_KEY"))
        self.model = "qwen-3.8-27b"
    
    async def reply(self, message):
        self.history.append({"role": "user", "content": message})

        messages = [
            {"role": "system", "content": self.personality},
        ] + self.history

        response = await self.client.chat.completions.create(model=self.model, messages=messages)
        answer = response.choices[0].message.content

        self.history.append({"role": "assistant", "content": answer})
        return answer
        

    def reset(self):
        self.history.clear()

ghost = ghost(random.choice(ghosts)) # pick a random name for the ghost.

async def main():
    while True:
        message = input("message: ")
        ghost.history.append({"role": "user", "content": message}) # roles are user and assistant

        if message[0] == "/":
            if message == "/help":
                print("")
            elif message == "/reset" or message == "/clear":
                ghost.reset()
            elif message == "/quit":
                print("You have escaped me. for now...")
                break
        else:
            await ghost.reply(message)

asyncio.run(main())
