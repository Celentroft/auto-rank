import discord
from discord import app_commands
from discord.ext import commands
from functions import *

class channelConfig(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="channel-config", description="Configurer le channel requis")
    async def ping(self, interaction: discord.Interaction, channel: discord.TextChannel) -> None:
        config = load_json()
        if interaction.user.id not in config['owner']:
            return await interaction.response.send_message("Vous n'êtes pas autorisé à utiliser cette commande.", ephemeral=True)
        
        config["pingchannel"] = channel.id
        json.dump(config, open("config.json", 'w', encoding='utf-8'), indent=4)
        embed = discord.Embed(
            title="`✅`・Salon Modifier",
            description=f"*Le salon de ping est désormais {channel.mention}*",
            color=embed_color()
        )
        return await interaction.response.send_message(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(channelConfig(bot))