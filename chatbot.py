#The chatbot that connect with the 5 servers.

import requests

history = []
servers = {
    "1": "http://localhost:5001/mcp",
    "2": "http://localhost:5002/mcp2",
    "3": "http://localhost:5003/mcp3",
    "4": "http://localhost:5004/mcp4",
    "5": "http://localhost:5005/mcp5"
}

active_server = "1"    #Set Default server as 1


def talk_to_server(message, server_url):     #function for sending message to the servers
    try:
        response = requests.post(server_url, json={"message": message})
        return response.json().get("response", "No response from server.")
    except Exception as e:
        return f"Error: {e}"

print("🤖 Chatbot Started. Type 'exit' to quit.")
print(" Use `/server 1` or `/server 2` or '/server 3' or /server 4' or '/server 5'to switch between servers.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    #To switch Servers
    if user_input.startswith("/server"):
        parts = user_input.strip().split()
        if len(parts) == 2 and parts[1] in servers:
            active_server = parts[1]
            print(f"Switched to Server {active_server}!!!!!!")
        else:
            print("Invalid command. Use: /server 1 or /server 2!!!!!")
        continue  

    #Sends Message to MCP Server
    server_url = servers[active_server]
    reply = talk_to_server(user_input, server_url)
    print(reply)
    history.append((user_input, reply))

#To Maintain Chat History
print("\nChat History: ")
for user, bot in history:
    print(f"You: {user} | Bot: {bot}")
