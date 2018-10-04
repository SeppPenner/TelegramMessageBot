import requests

telegramBaseUrl = 'https://api.telegram.org/bot'
botToken = 'YourBotToken' # Change to your bot token
chatId = '12345' # Change to your chat id

def sendTelegramMessage(message: str):
	"Sends a Telegram message"
	totalConnectionString = telegramBaseUrl + botToken + '/sendMessage?chat_id=' + chatId + '&text=' + message
	print('Connection string: ' + totalConnectionString)
	response = requests.get(totalConnectionString)
	print(response)

sendTelegramMessage('Hello!')