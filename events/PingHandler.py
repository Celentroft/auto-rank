import discord
from discord.ext import commands
from functions import *

class pingHandler(commands.Cog):
    def __init__(self, bot):
        self.bot: commands.Bot = bot
    
    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        config = load_json()
        if message.channel.id == config['pingchannel']: 
            if self.bot.user.mention in message.content:
                if config['tag'] in message.author.display_name:
                    role = message.guild.get_role(config['role'])
                    if role:
                        if role in message.author.roles:
                            
                            embed = discord.Embed(
                                description=f"Tu possède déjà le rôle {role.mention}.",
                                color=embed_color()
                            )
                            return await message.reply(embed=embed)

                        await message.author.add_roles(role)
                    
                        embed = discord.Embed(
                            description=f"Le rôle {role.mention} t'as été ajouté",
                            color=embed_color()
                        )
                        await message.reply(embed=embed)

                else:
                    embed = discord.Embed(
                        description=f"Tu n'as pas le tag {config['tag']} dans ton pseudo.",
                        color=embed_color()
                    )
                    await message.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(pingHandler(bot))