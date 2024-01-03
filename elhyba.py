from config import Config
import os, sys
import requests
import telebot
import time, base64, marshal, zlib, py_compile
	
token = config.TG_BOT_TOKEN
bot = telebot.TeleBot(token)
@bot.message_handler(commands = ['start'])
def start(message):
 
 bot.send_message(message.chat.id,f"""<strong>- ارسل ملفك البايثون ليتم تشفيره 
يتم تشفيره بأكثر من طبقة
⌁ انواع التشفير : 
ـ marshal,base46,zlib ـ</strong>""",parse_mode="html")
 @bot.message_handler(content_types=['document'])
 def send(message):
 	 bot.get_file(message.document.file_id)
 	 #bot.download_file(file_info.file_path)
 	# bot.send_photo(message.chat.id,open("file","rb"))
 	 file_info = bot.get_file(message.document.file_id)
 	 use = bot.download_file(file_info.file_path)
 	 bot.send_message(message.chat.id, f"""<strong>Wait a little please …</strong>""",parse_mode="html")
 	 cv =str("# channel : https://t.me/Source_Ze")
 	 sa = compile(use, 'dg', 'exec')
 	 sb = marshal.dumps(sa)
 	 sc = zlib.compress(sb)
 	 sd = base64.b85encode(sc)
 	 b = '#https://t.me/Source_Ze\nimport marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b85decode(' + repr(sd) + '))))'
 	 d = open('Encoded [@Source_Ze].py', 'w')
 	 d.write(b+'\n'+cv)
 	 d.close()
 	 file = {'document':open('Encoded [@Source_Ze].py','rb')}
 	 tex = ("Done Encryption File")
 	 requests.post(f'https://api.telegram.org/bot{token}/sendDocument?chat_id={message.chat.id}&caption={tex}', files=file)
 	 bot.send_message(message.chat.id, f"[🔱 𝐒𝐎𝐔𝐑𝐂𝐄 • 𝐙𝐄 🔱 .](t.me/Source_Ze)",parse_mode="markdown",disable_web_page_preview="true")
 	 os.system(f'rm -rf Encoded [@Source_Ze].py')
  	
bot.polling(True)