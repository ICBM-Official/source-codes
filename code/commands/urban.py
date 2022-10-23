@client.command(name="Urban dictionary",aliases=["urban", "urband"])
async def urbandictionary(ctx, term):
    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"
    querystring = {"term":term}

    headers = {
    'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
    'x-rapidapi-key': "6f97d59d22msh975d545aa225b2ap1220f9jsn7bc3b5c98207"
    }
    async with ClientSession() as session:
        async with session.get(url, headers=headers, params=querystring) as response:
            r = await response.json()
            definition = r['list'][0]['definition']
            embed = discord.Embed(title=f"First result for:{term}", description=None, colour=clienthex)
            embed.add_field(name=term, value=definition, inline=False)
            await ctx.send(embed=embed)
    await session.close()
