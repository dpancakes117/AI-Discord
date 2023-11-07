#!/usr/bin/env python
'''
Jobs for humanity discord bot for diversity, equity and inclusion in the workplace using PaLM
2023
Author: DeQwon Bentley
'''

import discord
import random
import os
from dotenv import load_dotenv
import google.generativeai as palm
from datetime import datetime
import re

#load .env values
load_dotenv()
DISCORD_TOKEN = 'MTE1MzcxNjY0MDkyMDM5MTcxMA.G_uurt.2gfMbg-H7bGxbXdwX-T6JD17d1L_ym84xt2Dh0'
BARD_TOKEN = ' cQilbwTvJHMGvsRBYJwI3--BTsG7UqekYHAAvemer-TpTD-0CdyfDPayfMjecuFQGL1bTg.'
PALM_KEY = 'AIzaSyDbSifLXjB03SKc6zzmpj4vvmge9BKMK8c'

#max characters that discord allows per message
DISCORD_MAX_CHARS = 2000
TOKEN_LIMIT = 8000 * 4

#initialize classes
client = discord.Client(intents=discord.Intents.default())
#bard = Bard(token = BARD_TOKEN)

palm.configure(api_key=PALM_KEY)

#PROMPT ENGINEERING STRING:

palm_prompt_header = "##INSTRUCTION## Your role is to aid recruitors in understanding. \
diversity, equity, and inclusion in the workplace. \
you answer questions related to diversity, equality and inclusivity. \
You should answer as concisely as possible. Keep all responses under 600 characters.\
If you are asked a question about something other diversity, equality and inclusivity you should not answer. \
First read the text files provided to you and pull out facts and important notes. If anything helps in answering a quesion, use that information. \
You can givee suggestions based on the text files provided or other knowledge you have. \
Give the response as if you are having a conversation. That is to say, in a way that people can understand.\
If the question seems like it is a follow up look at prevous questions to gain context and answer to the best of your ability. \
    Use this link to a text file to understand returning citizens: https://jfh.s3.us-east-2.amazonaws.com/transcribedText/Introduction+to+Returning+Citizens(Complete).txt "


#footer strings:
palm_prompt_footer = "```"

#logging info:
file_name = "bot-log.txt"
log_file = open(file_name, "a")


def get_palm_response(prompt):
    try:
        response = palm.generate_text(
            model='models/text-bison-001',
            prompt=prompt,
            temperature=0
        )
        print(response)
        return response.result
    except Exception as err:
        return err

#DISCORD CONNECTION:

#connect to discord:
@client.event 
async def on_ready():
    print(f'{client.user.name} has connnected to Discord')

#on message recieve 
@client.event
async def on_message(message):

    #dont respond to own messages or empty messages
    if message.author == client.user or not message.content:
        return
    
    print(message.content)

    ##PALM##

    await message.channel.send("Begin Palm Response")
    prompt = palm_prompt_header + message.content + palm_prompt_footer
    print(prompt)
    await message.channel.send(get_palm_response(prompt))
    await message.channel.send("End Palm Response")

client.run(DISCORD_TOKEN)