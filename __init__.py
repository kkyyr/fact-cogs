from .fact import Fact


def setup(bot):
    bot.add_cog(Fact(bot))
