import os
from kickforge_core import KickApp
from dotenv import load_dotenv

load_dotenv()

app = KickApp()
chat_messages = []

@app.on("chat.message.sent")
async def on_chat(event):
    if not event.message.startswith("!"):
        chat_messages.append((event.sender.username, event.message))
        
    print(chat_messages) # chat_messages = [('kick_username', 'message'), ('kick_user', 'message2')]
    
    if event.message == "!ping":
        print(f"Username: {event.sender.username}, Message: {event.message}")
        await app.say("pong!")
        
    # !last <username> <number_of_messages>
    if event.message.startswith("!last"):
        parts = event.message.split()
        if len(parts) == 3:
            try:
                username = parts[1] # Extract the username from the command
                last_x_messages = int(parts[2]) # Extract the number of messages from the command
                
                print(username)
                
                user_messages = [msg for user, msg in chat_messages if user.lower() == username] # Filter messages by the specified username
                last_messages = user_messages[-last_x_messages:]
                
                print(user_messages, last_messages)
            
                await app.say(f"{username}: " + " ".join(last_messages))
                
            except ValueError:
                await app.say("Invalid number of messages.")
            except IndexError:
                await app.say(f"{username} has fewer than {last_x_messages} messages.")
        elif len(parts) == 2:
            try:
                username = parts[1]
                user_messages = [msg for user, msg in chat_messages if user.lower() == username.lower()]
                last_messages = user_messages[-1:]
                await app.say(f"{username}: " + " ".join(last_messages))
            except IndexError:
                await app.say(f"{username} has no messages.")
        else:
            await app.say("Usage: !last 'username' 'last x messages'")
                
app.run(channel=os.getenv("KICK_CHANNEL"))