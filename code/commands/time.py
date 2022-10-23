@client.command()
async def time(ctx,*,  name : str):
    try:
        country = CountryInfo(name)
        data5 = country.timezones()
        content5 = (', '.join(data5))
        embed = discord.Embed(
            colour = (clienthex),
            title = (name),
        )
        embed.add_field(name="Timezones", value=content5)
        await ctx.send(embed=embed)
    except:
        await ctx.send('Country not found')
