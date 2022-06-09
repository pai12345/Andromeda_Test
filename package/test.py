import aiohttp

# Class for ping test
class Ping():
    # Method for ping test
    async def fetch(self, request):
        try:
            async with aiohttp.ClientSession() as session:
                pokemon_url = request
                async with session.get(pokemon_url) as resp:
                    pokemon = await resp.json()
                    return(pokemon['name'])
        except BaseException as error:
            return error

ping = Ping()