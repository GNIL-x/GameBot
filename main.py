from bot.commands import *

while __name__ == '__main__':
    try:
        print('__________\n'
              '||||||||||\n'
              'СТАРТ.....\n'
              '||||||||||\n'
              '__________\n')
        bot.polling(none_stop=True, interval=0)
    except:
        pass
