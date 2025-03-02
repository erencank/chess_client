import asyncio
import json

import chess
import websockets
from chess.engine import PlayResult

from libs.config import logger, settings
from libs.engine import MinimalEngine


async def run_bot(engine: MinimalEngine):
    ws_url = f"{settings.backend_ws_url}/bot?token={settings.bot_token}"
    while True:
        try:
            async with websockets.connect(ws_url, ping_interval=120, ping_timeout=120) as websocket:
                logger.info("Bot connected to backend.")
                while True:
                    msg = await websocket.recv()
                    data = json.loads(msg)
                    if data.get("type") == "request_move":
                        fen = data["fen"]
                        board = chess.Board(fen)
                        play_result: PlayResult = engine.search(board)
                        move = play_result.move.uci() if play_result.move is not None else None
                        await websocket.send(json.dumps({"type": "move", "uci": move}))
                        logger.info(f"Played move: {move}")
                    else:
                        # Handle other message types if needed.
                        pass
            print("Connection closed randomly")
        except websockets.exceptions.ConnectionClosed as e:
            logger.error(f"WebSocket connection closed: {e}. Reconnecting in 25 seconds...")
            try:
                await asyncio.sleep(25)
            except KeyboardInterrupt:
                logger.info("KeyboardInterrupt during reconnection delay. Shutting down bot.")
                break
            continue
        except Exception as e:
            logger.error(f"Unexpected error: {e}. Reconnecting in 25 seconds...")
            try:
                await asyncio.sleep(25)
            except KeyboardInterrupt:
                logger.info("KeyboardInterrupt during reconnection delay. Shutting down bot.")
                break
            continue


def start_bot(engine: MinimalEngine):
    try:
        asyncio.run(run_bot(engine))
    except KeyboardInterrupt:
        logger.info("Bot shutdown via KeyboardInterrupt.")
