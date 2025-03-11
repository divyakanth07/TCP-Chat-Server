# TCP Chat Server

This project implements a basic TCP chat server and client using Python's socket and threading modules. The server accepts multiple client connections, allows clients to send messages to each other, and broadcasts messages to all connected clients.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
  - [Server](#server)
  - [Client](#client)
- [Features](#features)
- [License](#license)

## Overview

This is a simple chat application with two main components:

1. **Server**: The server listens for incoming client connections and handles the broadcasting of messages between clients.
2. **Client**: The client connects to the server, sends messages, and listens for incoming messages from other clients.

Messages are encoded using base64 to prevent issues with transmitting non-text data.

## Requirements

To run the server and client, you'll need Python installed on your machine.

- Python 3.x
- No external libraries required (uses built-in libraries: `socket`, `threading`, `base64`)

## Setup and Installation

### 1. Clone the repository or download the files.

```bash
git clone <repository-url>
```

### 2. Navigate to the project folder.

```bash
cd <project-folder>
```

### 3. Ensure Python 3 is installed on your machine.

You can check this by running the following:

```bash
python --version
```

## Usage

### Server

1. To start the server, run the `server.py` file:

```bash
python server.py
```

The server will start listening on IP `127.0.0.1` (localhost) and port `4545`.

2. When clients connect, the server will print the client's address and a message about their username.

### Client

1. Run the `client.py` file to start the client.

```bash
python client.py
```

2. The client will prompt you to enter a username, and then it will connect to the server. Once connected, you can start sending and receiving messages.

3. The client interface allows you to type messages, which will be broadcast to all connected clients.

### Example

#### Server Output:
```
127.0.0.1 made a pact with the devil and sold their soul!!!
Username is Alice
Alice joined!
```

#### Client Output:
```
> What would you like being called : Alice
> Alice: Hello, world!
> Alice: How's everyone doing?
```

### Exiting the Program

To exit the chat, simply close the client window or press `Ctrl + C` in the terminal where the server is running. The server will automatically remove disconnected clients and broadcast the event to all other clients.

## Features

- **Multiple Clients**: The server supports multiple client connections at once.
- **Message Broadcasting**: All messages sent by clients are broadcast to all other clients connected to the server.
- **Base64 Encoding**: Messages are base64-encoded for transmission, ensuring compatibility with non-text data.
- **Client Identification**: Each client must provide a username upon connection.

## License

This project is open-source and free to use under the MIT license. See the LICENSE file for more details.

---
