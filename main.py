# Developed by scarlxrd

import os
import discord
from _colors import Colors
from discord.ext import commands
from functions import load_json

config = load_json()

async def load_commands(bot) -> None:
    for folder in os.listdir('./commands/'):
        for file in os.listdir(f'./commands/{folder}'):
            if file.endswith('.py'):
                try:
                    await bot.load_extension(f"commands.{folder}.{file[:-3]}")
                except Exception as e:
                    print(e)

    for file in os.listdir('./events/'):
        if file.endswith('.py'):
            try:
                await bot.load_extension(f"events.{file[:-3]}")
            except Exception as e:
                print(e)

class MyBot(commands.Bot):
    def __init__(self) -> None:
        self.C = Colors()
        super().__init__(
            command_prefix="noprefix", # you can define a prefix using config['prefix'] (also add it into config.json)
            intents=discord.Intents.all(),
            help_command=None
        )

    async def on_ready(self) -> None:
        print(f"{self.C.YELLOW}[UPDATING] {self.C.WHITE}Loading commands...")
        await load_commands(self)
        print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE}Commands loaded !")
        print(f"{self.C.YELLOW}[UPDATING] {self.C.WHITE}Syncing commands...")
        await self.tree.sync()
        print(f"{self.C.GREEN}[SUCCESS] {self.C.WHITE}Commands synced !")
        print(f"{self.C.BLUE}[LOGGED] {self.C.WHITE}Logged as {self.user.name} | {self.user.id}")
        await self.change_presence(activity=discord.Game(name=".gg/purity-dev"))
        print(f"{self.C.BLUE}[INFO] {self.C.WHITE} Status updated to .gg/purity-dev")

client = MyBot()
client.run(config['token'])