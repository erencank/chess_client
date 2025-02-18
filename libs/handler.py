import asyncio  # noqa: F401
import json

import chess
import websockets
from chess.engine import PlayResult

from libs.config import logger, settings
from libs.engine import MinimalEngine


async def run_bot(engine: MinimalEngine):
    # Connect to backend using the bot token
    ws_url = f"{settings.backend_ws_url}/bot?token={settings.bot_token}"
    async with websockets.connect(ws_url, ping_interval=120, ping_timeout=120) as websocket:
        logger.info("Bot connected to backend.")

        # The bot will wait for "request_move" messages from the server
        # and respond with a "move" message containing a UCI move.
        while True:
            msg = await websocket.recv()
            data = json.loads(msg)
            if data.get("type") == "request_move":
                fen = data["fen"]
                board = chess.Board(fen)
                # We let the engine choose a move
                play_result: PlayResult = engine.search(board)
                move = play_result.move.uci() if play_result.move is not None else play_result.move
                await websocket.send(json.dumps({"type": "move", "uci": move}))
                logger.info(f"Played move: {move}")
            else:
                # Handle other message types if needed
                pass


def start_bot(engine: MinimalEngine):
    # Runs the bot in an asyncio event loop
    asyncio.run(run_bot(engine))
