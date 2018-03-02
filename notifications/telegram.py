from .main import Notification
import telepot

class TelegramNotification(Notification)

    def __init__(self):
        super(Notification, self).__init__()
        self.bot = telepot.Bot('546527388:AAEARF_Cw9EfTv-z99ZMYtPZOquRI7wyXFU')
        self.chat_id = "365077439"

    def notify(self, string):
        print("*****"+string+"*****")
        bot.sendMessage(self.chat_id, "NOT: "+string)
