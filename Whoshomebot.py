from telegram.ext import Updater, InlineQueryHandler, CommandHandler, Filters #importing the needed libraries
import re
import os
import subprocess


os.system("ping -c 1 192.168.1.112")
os.system("ping -c 1 192.168.1.111")
os.system("ping -c 1 192.168.1.147")
os.system("ping -c 1 192.168.1.171")
os.system("ping -c 1 192.168.1.172")



devices= ["c8:3c:85:21:cf:0b","f8:4e:73:22:b7:6a","12:53:03:0b:96:12","c0:a6:00:e3:c8:d5","7c:a1:ae:39:e0:d4"]
famDevs= {
    "f8:4e:73:22:b7:6a":"JE",
    "7c:a1:ae:39:e0:d4":"AE",
    "c0:a6:00:e3:c8:d5":"NE",
    "c8:3c:85:21:cf:0b":"DS",
    "12:53:03:0b:96:12":"SE"
}
def checkIP(bot, update):
    message=[]
    devicesList=subprocess.run(['arp', '-a'], stdout=subprocess.PIPE).stdout.decode('utf-8')
    devicesList=str(devicesList)
    for i in devices:
        i=str(i)
        f=re.findall(i, devicesList)
        f=bool(f)
        if f:
            p=famDevs.get(i)
            msg=p+" esta en casa!"
            message.append(msg)
    message=str(message)
    update.message.reply_text(message)
updater = Updater('1315283050:AAF_Wm_gJIPdeaI54kZCflGzNjkkZJ7-oUI')
updater.dispatcher.add_handler(CommandHandler('casa', checkIP))
updater.start_polling()
updater.idle()
