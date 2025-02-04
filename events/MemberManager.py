import discord
from discord.ext import commands
from functions import *

class MemberManager(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before: discord.Member, after: discord.Member):
        config = load_json()
        if before.display_name != after.display_name:
            if config['tag'] not in after.display_name:
                guild: discord.Guild = self.bot.get_guild(config['guildId'])
                role: discord.Role = guild.get_role(config['role'])
                if role:
                    await after.remove_roles(role)
                
async def setup(bot):
    await bot.add_cog(MemberManager(bot))