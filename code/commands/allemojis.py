@client.command()
@commands.has_permissions(manage_emojis=True)
async def allemojis(ctx, *, page: int = 1):
    emoji_list = []

    await ctx.message.delete()
    for emoji in ctx.message.guild.emojis:
        emoji_list.append(emoji)
    if len(emoji_list) == 0:
        embed = (discord.Embed(description='No emojis in this server'))
        return await ctx.send(embed=embed)
    items_per_page = 10
    pages = math.ceil(len(emoji_list) / items_per_page)

    start = (page - 1) * items_per_page
    end = start + items_per_page

    bmembers = ''
    for n, i in enumerate(emoji_list[start:end], start=start):
        bmembers += (f'{n+1}, {i}\n')

    embed = (discord.Embed(description='**{} Emojis:**\n\n{}'.format(len(emoji_list), bmembers))
             .set_footer(text='Viewing page {}/{}'.format(page, pages)))
    message = await ctx.send(embed=embed)
    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await client.wait_for("reaction_add", timeout=60, check=check)
            if str(reaction.emoji) == "▶️" and page != pages:
                page += 1
                start = (page - 1) * items_per_page
                end = start + items_per_page
                bmembers = ''
                for n, i in enumerate(emoji_list[start:end], start=start):
                    bmembers += (f'{n+1}, {i}\n')
                newembed = (discord.Embed(description='**{} Emojis:**\n\n{}'.format(len(emoji_list), bmembers)))
                newembed.set_footer(text='Viewing page {}/{}'.format(page, pages))
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and page > 1:
                page -= 1
                start = (page - 1) * items_per_page
                end = start + items_per_page
                bmembers = ''
                for n, i in enumerate(emoji_list[start:end], start=start):
                    bmembers += (f'{n+1}, {i}\n')
                newembed = (discord.Embed(description='**{} Emojis:**\n\n{}'.format(len(emoji_list), bmembers)))
                newembed.set_footer(text='Viewing page {}/{}'.format(page, pages))
                await message.edit(embed=newembed)
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)
        except asyncio.TimeoutError:
            await message.delete()
            break
