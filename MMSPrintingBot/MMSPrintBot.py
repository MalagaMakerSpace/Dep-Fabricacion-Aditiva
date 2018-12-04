import telebot
import pandas as pd

bot = telebot.TeleBot("")
users = pd.read_pickle('usrs.pk')

def check_membership(id):
    if id in users.index:
        return True
    bot.send_message(id, 'Parece que no estás autorizado para usar las impresoras. Contacta con el Director del departamento para solucionar cualquier problema.')
    return False

@bot.message_handler(commands=['getid'])
def get_id(message):
    bot.reply_to(message, message.chat.id)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    id = message.chat.id
    if check_membership(id):
        bot.send_message(id, '¡Hola! Soy el bot del Málaga MakerSpace para gestionar las impresoras.\n\n'
                             'Tienes los siguientes comandos a tu disposición:\n'
                             '/help Esta ayuda\n'
                             '/printers Disponibilidad de impresoras'
                             '/print Envía el archivo que quieres imprimir\n'
                             '/status Comprobar el estado de la impresión\n'
                             '/pause Pausa la impresión\n'
                             '/resume Reanuda la impresión'
                         )
        if users['role'][id] == 'admin':
            bot.send_message(id, 'Los comandos de administrador son:\n'
                                 '/adduser'
                             )

@bot.message_handler(commands=['print'])
def print(message):
    id = message.chat.id
    if check_membership(id):
        bot.send_message(id, '')


if __name__ == '__main__':
    bot.polling(True)
