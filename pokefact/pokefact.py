import json
import random

import discord
from redbot.core import cog_manager, commands


class Pokefact(commands.Cog):
    """Sends a random Pokémon fact."""

    __author__ = ["ha?m"]
    __version__ = "1.0"

    def __init__(self, bot):
        self.bot = bot

    def format_help_for_context(self, ctx: commands.Context) -> str:
        """???"""
        pre_processed = super().format_help_for_context(ctx)
        return f"{pre_processed}\n\nAuthors: {', '.join(self.__author__)}\nCog Version: {self.__version__}"

    @commands.command()
    async def pokefact(self, ctx):
        cm = cog_manager.CogManager()
        ipath = str(await cm.install_path())
        facts = json.load(open(ipath + "/pokefact/facts.json", "r", encoding="utf-8"))
        bfint = random.randint(0, 49)
        try:
            await ctx.reply(facts[bfint], mention_author=False)
        except discord.HTTPException:
            await ctx.send(facts[bfint])
