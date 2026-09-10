
# kick chat bot

a lightweight chatbot for kick.com livestream chat, built using kickforge, python, and async event handling. 
the bot listens to chat messages, responds to commands, and keeps an in‑memory history of user messages.

**features**
- responds to !ping with pong!
- tracks all non-command chat messages
- provides a !last <username> <n> command to retrieve the last n messages from a user & supports default behaviour when <n> is omitted (returns the last message)
- uses .env for configuration

runs via kickforge’s kickapp

**project structure**
```
kickchatbot/
│
├── venv/
├── .env
├── main.py
```

**installation**

1. clone the repository
```powershell
>> git clone https://github.com/cov2k/kickchatbot.git
>> cd kickchatbot
```
2. create a virtual environment 
```powershell
>> python -m venv venv
```
activate it
```bash
>> venv\scripts\activate
```
3. follow the [kickforge install process](https://pypi.org/project/kickforge/)
4. run the bot
```bash
>> python main.py
```
## how it works
**_message storage_**

the bot stores chat messages in memory:
```py
chat_messages.append((event.sender.username, event.message))
```
commands (messages that begin with !) are not stored

**_message filter (per user)_**
```py
user_messages = [
    msg for user, msg in chat_messages
    if user.lower() == username.lower()
]
```
_**selecting the last x messages**_
```py
last_messages = user_messages[-last_x_messages:]
```
### known limitations
- message history resets when the bot restarts
- command handling is quite strict



