import telebot
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException


# Конфигурационные данные
telegram_token = 'YOUR_TELEGRAM_TOKEN'
bitcoin_rpc_user = 'YOUR_BITCOIN_RPC_USERNAME'
bitcoin_rpc_password = 'YOUR_BITCOIN_RPC_PASSWORD'
bitcoin_rpc_ip = '127.0.0.1'  # IP-адрес вашего узла Bitcoin
bitcoin_rpc_port = '8332'  # Порт JSON-RPC вашего узла Bitcoin

# Инициализация Telegram бота
bot = telebot.TeleBot(telegram_token)

# Инициализация Bitcoin RPC
bitcoin_rpc_url = f'http://{bitcoin_rpc_user}:{bitcoin_rpc_password}@{bitcoin_rpc_ip}:{bitcoin_rpc_port}'
bitcoin_rpc = AuthServiceProxy(bitcoin_rpc_url)

# Обработчик команды /getnewaddress
@bot.message_handler(commands=['getnewaddress'])
def get_new_address(message):
    try:
        new_address = bitcoin_rpc.getnewaddress()
        bot.reply_to(message, f'Новый адрес: {new_address}')
    except JSONRPCException as e:
        bot.reply_to(message, f'Ошибка при генерации нового адреса: {e}')

# Обработчик команды /getbalance
@bot.message_handler(commands=['getbalance'])
def get_balance(message):
    try:
        balance = bitcoin_rpc.getbalance()
        bot.reply_to(message, f'Баланс кошелька: {balance} BTC')
    except JSONRPCException as e:
        bot.reply_to(message, f'Ошибка при получении баланса: {e}')

# Запуск бота
if __name__ == '__main__':
    bot.infinity_polling()
