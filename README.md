# 🤖 Chatbot with Multiple MCP Servers Integration

## Project Overview
This project implements a Python chatbot that integrates with **five different MCP servers**, each performing distinct tasks.  
The chatbot supports switching between servers during conversation and keeps a history of interactions.

---------------------------------------------------

## MCP Servers Used and Their Purpose

1. Server 1 (mcp_server.py)
   Reverses the input string or number.

2. Server 2 (mcp_server2.py)
   Converts input strings to uppercase; checks if numeric input is a prime number.

3. Server 3 (mcp_server3.py)  
   Checks if input strings are palindromes; determines if numeric input is positive, negative, or zero.

4. Server 4 (mcp_server4.py)  
   Adds emojis to the input message for engagement.

5. Server 5 (mcp_server5.py)  
   Returns the length of the input message.

----------------------------------------------------

## How the Chatbot Works

- The chatbot runs as a command-line program.
- It sends user messages to the currently active MCP server via HTTP POST requests.
- Users can switch servers anytime with commands like `/server 2`.
- The chatbot maintains and prints the full conversation history at the end of the session.
- Each MCP server handles the input uniquely based on its designed functionality.

----------------------------------------------------

## How to Run

### Prerequisites

- Python 3.6 or higher installed
- Packages: `flask`, `requests`

Install packages using:

pip install flask requests
---------------------------------------------------
## Running the MCP Servers
Open five separate terminals and start each MCP server with:

python mcp_server.py       # Server 1 on port 5001
python mcp_server2.py      # Server 2 on port 5002
python mcp_server3.py      # Server 3 on port 5003
python mcp_server4.py      # Server 4 on port 5004
python mcp_server5.py      # Server 5 on port 5005

## Running the chatbot

python chatbot.py
-------------------------------------------------------------------

