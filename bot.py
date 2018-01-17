import discord
import asyncio

description = "Baylor-Bot"
bot_prefix = "n-"

client = discord.Client()

@client.event
async def on_ready():
	print("Logged in");
	print("Name: " + client.user.name);
	print("ID: " + client.user.id);
	print("\n\n");

@client.event
async def on_message(message):
	if message.content.startswith('n-help'):
		await client.send_message(message.channel, "Bot under construction!")
	if message.content.startswith('n-staff'):
		await client.send_message(message.channel, "**Owner:** *JustinFromMCPE* n\ **Co-Owner:** *TBNRItzDoge*")

client.run("NDAzMDMxMjQ0NTI0MzU1NTg1.DUBYcQ.Cmc_HChwhfkCu1KZyBgcHRfvrcw");
