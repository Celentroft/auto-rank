import discord
from discord import app_commands
from discord.ext import commands
from functions import *

class tagConfig(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="tag-config", description="Configurer le tag requis")
    async def ping(self, interaction: discord.Interaction, tag: str) -> None:
        config = load_json()
        if interaction.user.id not in config['owner']:
            return await interaction.response.send_message("Vous n'êtes pas autorisé à utiliser cette commande.", ephemeral=True)
        
        config["tag"] = tag
        json.dump(config, open("config.json", 'w', encoding='utf-8'), indent=4)
        embed = discord.Embed(
            title="`✅`・Tag Modifier",
            description=f"*Le nouveau tag requis pour obtenir le role est `{tag}`.*",
            color=embed_color()
        )
        return await interaction.response.send_message(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(tagConfig(bot))