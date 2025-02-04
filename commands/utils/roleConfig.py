import discord
from discord import app_commands
from discord.ext import commands
from functions import *

class roleConfig(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="role-config", description="Configurer le role requis")
    async def ping(self, interaction: discord.Interaction, role: discord.Role) -> None:
        config = load_json()
        if interaction.user.id not in config['owner']:
            return await interaction.response.send_message("Vous n'êtes pas autorisé à utiliser cette commande.", ephemeral=True)
        
        config["role"] = role.id
        json.dump(config, open("config.json", 'w', encoding='utf-8'), indent=4)
        embed = discord.Embed(
            title="`✅`・Role Modifier",
            description=f"*Le rôle ajouté est désormais {role.mention}*",
            color=embed_color()
        )
        return await interaction.response.send_message(embed=embed)

async def setup(bot) -> None:
    await bot.add_cog(roleConfig(bot))