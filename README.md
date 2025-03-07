# Chess Client Bot Library

This is a simple chess bot client library that connects to a backend WebSocket server to receive move requests and send back moves chosen by a user-defined engine. It’s designed to be user-friendly.
This client is meant to be used on the [ChessBeez platform](https://chess-frontend-4916.onrender.com/)

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
BACKEND_WS_URL="wss://chess-backend-ssn3.onrender.com/ws"
```

Adjust these values as necessary. You can get the bot token by going to the frontend, creating a bot, and copying the token under actions.

## Running the Bot

To start the bot using the default RandomMove engine, run:

```bash
uv run homemade.py
```

The bot will connect to the backend, await "request_move" messages, and respond with a move.

## Shutdown Behaviour

- If the backend WebSocket closes, the bot logs the event and stops.
- Press Ctrl+C in the terminal to gracefully shut down the bot.

## VSCode Dev Container (Optional)

For a preconfigured development environment, you can use the included devcontainer (Needs Docker locally):

- Open the project in VS Code.
- When prompted, choose Reopen in Container.
- The dev container will install Python 3.12 and the uv package manager, and run uv sync automatically.
- In the container you can start your bot the same way as before using `uv run homemade.py`.

## Some helpful tips:

There are a few approaches on how to tackle this Hackathon.

One of them might be to simply ask ChatGPT and hope it gives you a correct answer given the board, or `import stockfish` and call it a day :)

Another simple approach is to loop through all available legal moves and see if there is one that would capture a piece of the opponent and play that move. You can improve this by only taking pieces if yours is worth less.

There are a few (non machine learning) algorithms for chess engines based on [minimax](https://en.wikipedia.org/wiki/Minimax) and [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). There's also the Monte Carlo Tree Search which probably is too complex for a single Hackathon day. If you want to try something fun, I suggest building a chess engine based on these algorithms. For some additional help on these algorithms, you can google some implementations.

What might also be good it to hard-code a few opening moves (first moves of the game) that you think would be good. You can look at a [database](https://www.365chess.com/opening.php) of openings.

# Notes for the hackathon!

This platform is a MVP and there are some things missing (such as a match history). One of the big things is that everyone can start a match with everyone. There is no accepting or declining a match. This means that once you're online you can be dragged in a match with someone who challenged you and win or lose. Make of that what you will, this is a hackathon after all ;)

And for good sportsmanship, lets try to make some fun chess bots! If you have a stockfish bot that can play like a 2800 rated player in an hour, create a second bot and try to improve that based on purely your own programming for example.
