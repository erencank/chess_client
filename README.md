# Chess Client Bot Library

This is a simple chess bot client library that connects to a backend WebSocket server to receive move requests and send back moves chosen by a user-defined engine. It’s designed to be user-friendly.

## Requirements

- Python 3.12
- [uv package manager](https://astral.sh/uv/) for dependency management

## Setup

1. **Install uv:**
   Follow the instructions at [https://astral.sh/uv/](https://astral.sh/uv/).

2. **Install Dependencies:**
   Run:

   ```bash
   uv sync
   ```

   to install the required packages.

3. Configuration: Create a .env file (look at .env.example) in the project root with:

```env
BOT_TOKEN="your-bot-token-here"
BACKEND_WS_URL="ws://127.0.0.1:8000"
```

Adjust these values as necessary.

## Running the Bot

To start the bot using the default RandomMove engine, run:

```bash
uv run python homemade.py
```

The bot will connect to the backend, await "request_move" messages, and respond with a move.

## Shutdown Behaviour

- If the backend WebSocket closes, the bot logs the event and stops.
- Press Ctrl+C in the terminal to gracefully shut down the bot.

## VSCode Dev Container (Optional)

For a preconfigured development environment, you can use the included devcontainer:

- Open the project in VS Code.
- When prompted, choose Reopen in Container.
- The dev container will install Python 3.12 and the uv package manager, and run uv sync automatically.
