from discord import Webhook, AsyncWebhookAdapter, File, Embed
import aiohttp
import asyncio

async def foo():
    async with aiohttp.ClientSession() as session:
        image = File("cropped.png")
        webhook = Webhook.from_url('', adapter=AsyncWebhookAdapter(session))
        #message = "@everyone\nGreetings mortals, it is I, Merasmus! Today, I come to you to announce that Creators.TF released their Halloween event, in collaboration with me! Merasmus is glad the team trusted him enough to let him prepare Scream Fortress for them. However, I had to face some unfortunate events.\n\nYou can read more about it here: https://creators.tf/classful.\nPatch notes... are over there! https://creators.tf/updates"
        
        embedMessage = Embed(title="A RARE MESSAGE FROM MERASMUS.")
        embedMessage.add_field(name="IT READS AS FOLLOWS:", 
        value="Greetings mortals, it is I, Merasmus! Today, I come to you to announce that Creators.TF released their Halloween event, in collaboration with me! Merasmus is glad the team trusted him enough to let him prepare Scream Fortress for them. However, I had to face some unfortunate events."
        ,inline=False)
        embedMessage.add_field(name="You can read more about it here:", value="https://creators.tf/barbocabarto", inline=True)
        embedMessage.add_field(name="Patch notes... are over there!", value="https://creators.tf/updates", inline=True)
        embedMessage.add_field(name="And the blog post... is around there!", value="https://creators.tf/post/blog/76", inline=True)
        embedMessage.color = 0x38f3ab
        
        
        #await webhook.send(message, username='MERASMUS!', file=image)
        await webhook.send("@everyone", embed=embedMessage, username='MERASMUS!')
        await webhook.send(file=image)

asyncio.run(foo())