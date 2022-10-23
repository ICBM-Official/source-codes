@client.command()
@commands.has_permissions(manage_messages=True)
async def winner(ctx, id_ : int):
    channel = ctx.message.channel
    try:
        new_msg = await channel.fetch_message(id_)
    except:
        await ctx.send("The ID that was entered was incorrect, make sure you have entered the correct giveaway message ID.")
    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(client.user))

    winner = random.choice(users)

    await channel.send(f"Congratulations to: {winner.mention}. You won!")
    await ctx.message.delete()
