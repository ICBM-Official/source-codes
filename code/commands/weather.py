key_features = {
    'temp' : 'Temperature',
    'feels_like' : 'Feels Like',
    'temp_min' : 'Minimum Temperature',
    'temp_max' : 'Maximum Temperature'
}

@client.command()
async def weather(ctx, *, location: str):
    def parse_data(data):
        del data['humidity']
        del data['pressure']
        return data

    def weather_message(data, location):
        location = location.title()
        message = discord.Embed(
            title=f'{location} Weather',
            description=f'Here is the weather in {location}.',
            colour=clienthex
        )
        for key in data:
            message.add_field(
                name=key_features[key],
                value=str((data[key] -32) * 5/9),
                inline=False
            )
        return message

    def error_message(location):
        location = location.title()
        return discord.Embed(
            title='Error',
            description=f'There was an error retrieving weather data for {location}.',
            colour=clienthex
        )
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid=&units=imperial'
    try:
        data = parse_data(json.loads(requests.get(url).content)['main'])
        print(data)
        await ctx.message.channel.send(embed=weather_message(data, location))
    except KeyError:
        await ctx.send(embed=error_message(location))
