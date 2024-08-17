import telebot

from config import TOKEN,API_TOKEN, SEKRET_KEY 

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message, 'Напиши мне prompt, чтобы я отправил сгенерированную картинку')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text

    api = Text2ImageAPI('https://api-key.fusionbrain.ai/', API_TOKEN, SEKRET_KEY)
    model_id = api.get_model()
    uuid = api.generate("prompt", model_id)
    images = api.check_generation(uuid)[0]

    api.save_image(images, 'decoded_image.jpg')

    with open('decoded_image.jpg', 'rb')as photo:
        bot.send_photo(message.chat.id, photo)

bot.infinity_polling()