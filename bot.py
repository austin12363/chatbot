import os
import telegram
from transformers import AutoModelForCausalLM, AutoTokenizer

bot = telegram.Bot(token=os.environ["TELEGRAM_TOKEN"])
model_name = "microsoft/DialoGPT-large"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

def generate_response(message):
    input_ids = tokenizer.encode(message + tokenizer.eos_token, return_tensors='pt')
    output = model.generate(input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)
    return tokenizer.decode(output[0], skip_special_tokens=True)

def echo(update, context):
    message = update.message.text
    response = generate_response(message)
    context.bot.send_message(chat_id=update.message.chat_id, text=response)

from telegram.ext import Updater, MessageHandler, Filters
updater = Updater(token=os.environ["TELEGRAM_TOKEN"], use_context=True)
dispatcher = updater.dispatcher

dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

updater.start_polling()
