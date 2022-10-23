@client.command(name="dailyfact")
async def dailyfact(context):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://uselessfacts.jsph.pl/random.json?language=en") as request:
            if request.status == 200:
                data = await request.json()
                embed = discord.Embed(description=data["text"], color=clienthex)
                await context.send(embed=embed)
            else:
                embed = discord.Embed(
                    title="Error!",
                    description="There is something wrong with the API, please try again later",
                    color=clienthex
                )
                await context.send(embed=embed)
                dailyfact.reset_cooldown(context)
