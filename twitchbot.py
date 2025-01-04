from twitchio.ext import commands
from random import choice
from os import environ
from json import load


class Bot(commands.Bot):

    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        # prefix can be a callable, which returns a list of strings or a string...
        # initial_channels can also be a callable which returns a list of strings...
        super().__init__(token=environ['TOKEN'], client_id=environ['CLIENT_ID'],
                         nick='BonifacioBot',
                         prefix='!', initial_channels=[environ['CHANNELS']])
       

    async def event_ready(self):
        # Notify us when everything is ready!
        # We are logged in and ready to chat and use commands...
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        # Here we have a command hello, we can invoke our command with our prefix and command name
        # e.g ?hello
        # We can also give our commands aliases (different names) to invoke with.

        # Send a hello back!
        # Sending a reply back to the channel is easy... Below is an example.
        with open('redes.json') as f:
            data = load(f)
            discord = data['discord']
        await ctx.channel.send(f'Recuerda nuestra nueva Comunidad de Discord: {discord}!')
    
    @commands.command()
    async def web(self, ctx: commands.Context):
        with open('redes.json') as f:
            data = load(f)
            web = data['web']
        await ctx.channel.send(f'Visita nuestra web: {web}; donde encontrarás ejemplos e información del canal!')

    @commands.command()
    async def horario(self, ctx: commands.Context):
        await ctx.channel.send(f'Nuestro horario es Miércoles a las 17:00 y Viernes a partir de las 16:00 y los especiales los domingos a partir de las 16:30.')
    
    @commands.command()
    async def especial(self, ctx: commands.Context):
        with open('especial.json') as f:
            data = load(f)
            fecha = data['fecha']
            tema = data['tema']
        await ctx.channel.send(f'El próximo especial será el {fecha} y el tema será {tema}')
   
    @commands.command()
    async def redes(self, ctx: commands.Context):
        with open('redes.json') as f:
            data = load(f)
            twitter = data['twitter']
            Bsky = data['Bsky']
            mastodon = data['mastodon']
            discord = data['discord']
        await ctx.channel.send(f'X: {twitter},\n BSky: {Bsky},\n Mastodon: {mastodon},\n Discord: {discord}')
    @commands.command()
    async def sorteo(self, ctx: commands.Context):
       #if(not ctx.author.is_broadcaster):
        with open("sorteo.json") as f:
            data = load(f)
            fecha = data['fecha']
            tema = data['tema']
            descripcion = data['descripcion']
        await ctx.channel.send(f' {descripcion} el {fecha}. No te lo pierdas!')
    
    @commands.command()
    async def r36s(self, ctx: commands.Context):
        if ctx.author.is_broadcaster:
           users= []
           for user in ctx.channel.chatters:
                if(user.is_subscriber and not user.is_broadcaster):
                    users.append(user)
           await ctx.channel.send(f'El ganador del sorteo es {choice(users).display_name}!')
 

bot = Bot()
bot.run()