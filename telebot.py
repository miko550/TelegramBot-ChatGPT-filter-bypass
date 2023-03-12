import requests
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Set up the ChatGPT API endpoint and API key
api_endpoint = 'https://api.openai.com/v1/completions'
api_key = 'YOUR_API_KEY'

# Set up the Telegram bot
bot_token = 'YOUR_BOT_TOKEN'
bot = telegram.Bot(bot_token)
updater = Updater(token=bot_token, use_context=True)

# Define a function to get a response from the ChatGPT API using curl
def get_chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }
    data = {
        'model': 'text-davinci-003',
        'prompt': prompt,
        'max_tokens': 4000,
        'temperature': 1.0,
    }
    response = requests.post(api_endpoint, headers=headers, json=data)
    response_data = response.json()
    return response_data['choices'][0]['text']

# Define a function to handle incoming messages
def handle_message(update, context):
    message_text = update.message.text
    chat_id = update.effective_chat.id
    response_text = get_chatgpt_response(message_text)
    bot.send_message(chat_id=chat_id, text=response_text)

# Set up the message handler
message_handler = MessageHandler(Filters.text & ~Filters.command, handle_message)
updater.dispatcher.add_handler(message_handler)

# Start the bot
updater.start_polling()
updater.idle()

