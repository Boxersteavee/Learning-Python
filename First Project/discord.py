import discord
import os
import random
from discord.ext import commands
from discord.ext import tasks
import asyncio
import traceback
import sys

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="play.pixelpvpnetwork.tk"))
    print('Bot is ready')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Command doesn\'t exist, Did you type it correctly? Try !helppls to get the command list.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('You do not have the permissions for this command.')
    else:
        print(error)

@client.command(aliases=['commands', 'commandlist'])
async def helppls(ctx):
  helpembed = discord.Embed(
      title = 'Commands List',
      description = 'Here is a list of commands.',
      colour = discord.Colour.blue()
    
  )

  helpembed.set_footer(text='This is the best discord bot')
  helpembed.set_author(name='PixelPvP Commands')
  helpembed.add_field(name='!clear', value='Clears the last 10 messages or however many you specify. User must be able to Manage Messages.')
  helpembed.add_field(name='!harlzelive', value='Sends a notification that MrHarlze200 is live. Must be member of the staff team.')
  helpembed.add_field(name='!socials', value='Links to <#694909776932503623>')
  helpembed.add_field(name='streams', value='Links you to <#774312242300452925>')
  helpembed.add_field(name='!shutup', value='STOP ASKING ME TO DO STUFF AND I MIGHT SHUTUP!')
  helpembed.add_field(name='!ip', value='Shows the IP of the server. \n(Duh.\n)')
  helpembed.add_field(name='!8ball', value='Do you dare ask me a question? I have many answers so be wise with your question.')
  helpembed.add_field(name='!commandlist', value='Shows this menu that took way too long for my owner to make. He had to keep waking up and shutting me down!')
  helpembed.add_field(name='!boxerlive', value='Sends a notification that Boxersteavee is live. Must be member of the staff team.')


  await ctx.send(embed=helpembed)

@client.command()
async def ping(ctx):
  await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
  await ctx.channel.purge(limit=amount)
  await asyncio.sleep(3)
  await ctx.send(amount + 'messages deleted')

@client.command()
@commands.has_permissions(manage_messages=True)
async def harlzelive(ctx):
  channel = client.get_channel(706905806943158333)
  await channel.send('Hey! <@&747759082995318805> MrHarlze200 is live! Go see at https://twitch.tv/MrHarlze200')
  await client.change_presence(activity=discord.Streaming(name="MrHarlze200 Is live!", url="https://twitch.tv/mrharlze200"))
  await ctx.send('Okay, Sending the notification, have a good stream! :poggers:')
  

@client.command()
@commands.has_permissions(manage_messages=True)
async def boxerlive(ctx):
  channel = client.get_channel(706905806943158333)
  await channel.send('Hey! <@&747759082995318805> Boxersteavee is live! Go see at https://twitch.tv/Boxersteavee')
  await client.change_presence(activity=discord.Streaming(name="Boxersteavee Is live!", url="https://twitch.tv/boxersteavee"))
  await ctx.send('Okay, Sending the notification, have a good stream! :poggers:')
  
@client.command()
async def socials(ctx):
  await ctx.send('JUST GO TO <#694909776932503623>')

@client.command(aliases=['Streams', 'streaming'])
async def streams(ctx):
  await ctx.send('Any reason you can\'t go to <#774312242300452925>')

@client.command()
async def shutup(ctx):
  await ctx.send('I will shut up if you stop asking me to do stuff! :frowning2:')

@client.command(aliases=['server'])
async def ip(ctx):
  await ctx.send('The server ip for our minecraft server is play.pixelpvpnetwork.tk')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ['It is certain',
              'It is decidedly so.',
               'Without a doubt.',
              'Yes - definitely.',
              'You may rely on it.',
              'As I see it, yes.',
              'Most likely.',
              'Outlook good.',
              'Yes.',
              'Signs point to yes.',
              'Reply hazy, try again.',
              'Ask again later.',
              'Better not tell you now.',
              'Cannot predict now.',
              'Concentrate and ask again.',
              'Don\'t count on it.',
              'My reply is no.',
              'My sources say no.',
              'Outlook not so good.',
              'Very doubtful.']
  await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@_8ball.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please add a question')
        
@client.command()
@commands.has_permissions(manage_messages=True)
async def ended(ctx):
  channel = client.get_channel(706905806943158333)
  await client.change_presence(activity=discord.Game(name="play.pixelpvpnetwork.tk"))
  await ctx.send('Set the status back, hope you had a good stream!')
  await channel.purge(limit=1)
  

client.run('Nzk4MTgwNjU3NTcwMjUwODEz.X_xRqg.uVvUmcrVeeni3bR39p1a9hBORQo')