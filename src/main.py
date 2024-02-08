from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from openai import OpenAI

# STEP 0: LOAD OUR TOKEN FROM SOMEWHERE SAFE
load_dotenv()
DISCORD_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
OPENAI_API_KEY: Final[str] = os.getenv('OPENAI_API_KEY')

# STEP 1: BOT SETUP
intents: Intents = Intents.default()
intents.message_content = True  # NOQA
discord_client: Client = Client(intents=intents)

open_ai_client = OpenAI()

chat_log = []

# STEP 2: MESSAGE FUNCTIONALITY
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('(Message was empty because intents were not enabled probably)')
        return

    if is_private := user_message[0] == '.':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, open_ai_client, chat_log)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


# STEP 3: HANDLING THE STARTUP FOR OUR BOT
@discord_client.event
async def on_ready() -> None:
    print(f'{discord_client.user} is now running!')


# STEP 4: HANDLING INCOMING MESSAGES
@discord_client.event
async def on_message(message: Message) -> None:
    if message.author == discord_client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# STEP 5: MAIN ENTRY POINT
def main() -> None:
    discord_client.run(token=DISCORD_TOKEN)


if __name__ == '__main__':
    main()