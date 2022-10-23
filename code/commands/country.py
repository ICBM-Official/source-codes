@client.command()
async def country(ctx,*,  name : str):
    try:
        country = CountryInfo(name)
        data1 = country.alt_spellings()
        data2 = country.capital()
        data3 = country.currencies()
        data4 = country.languages()
        data5 = country.timezones()
        data6 = country.area()
        data7 = country.borders()
        data8 = country.calling_codes()
        data9 = country.population()
        data10 = country.region()
        data11 = country.subregion()
        data12 = country.wiki()
        content1 = (', '.join(data1))
        content2 = data2
        content3 = (', '.join(data3))
        content4 = (', '.join(data4))
        content5 = (', '.join(data5))
        content6 = data6
        content7 = (', '.join(data7))
        content8 = (', '.join(data8))
        content9 = data9
        content10 = data10
        content11 = data11
        content12 = data12
        if not content1:
            content1 = 'None'
        if not content2:
            content2 = 'None'
        if not content7:
            content7 = 'None'
        if not content3:
            content3 = 'None'
        if not content4:
            content4 = 'None'
        if not content5:
            content6 = 'None'
        if not content7:
            content7 = 'None'
        if not content8:
            content8 = 'None'
        if not content9:
            content9 = 'None'
        if not content10:
            content10 = 'None'
        if not content11:
            content11 = 'None'
        if not content12:
            content12 = 'None'
        embed = discord.Embed(
            colour = (clienthex),
            title = (name),
        )
        embed.add_field(name="Names", value=content1)
        embed.add_field(name="Capital", value=content2)
        embed.add_field(name="Currencies", value=content3)
        embed.add_field(name="Languages", value=content4)
        embed.add_field(name="Timezones", value=content5)
        embed.add_field(name="Area", value=content6)
        embed.add_field(name="Borders", value=content7)
        embed.add_field(name="Calling Codes", value=content8)
        embed.add_field(name="Popolation", value=content9)
        embed.add_field(name="Region", value=content10)
        embed.add_field(name="Subregion ", value=content11)
        embed.add_field(name="Wiki", value=content12)
        await ctx.send(embed=embed)
    except:
        await ctx.send('Country not found')
