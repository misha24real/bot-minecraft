from javascript import require, On, Once, AsyncTask, once, off
import openai
import os
import time
 
mineflayer = require('mineflayer')
 
BOT_USERNAME = 'BOT'
Password = "gbth90124"
openai.api_key = "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"
model_engine = "text-davinci-003"
max_tokens = 128
 
bot = mineflayer.createBot({ 'host': 'openpc.ru-mc.ru', 'username': '{BOT_USERNAME}', 'hideErrors': False })
 
time.sleep(5)
bot.chat(f'/register {Password} {Password}')
bot.chat(f'/login {Password}')
 
@On(bot, 'chat')
def onChat(this, user, message, *rest):
  dfl = "."
  if not message.startswith(dfl): 
    return
 
 
  completion = openai.Completion.create(
      engine=model_engine,
      prompt=message.replace(".", "", 1),
      max_tokens=512,
      temperature=0.5,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
  )
 
  bot.chat(completion.choices[0].text)
