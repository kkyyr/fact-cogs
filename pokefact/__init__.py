from .pokefact import Pokefact


def setup(bot):
    bot.add_cog(Fact(bot))
