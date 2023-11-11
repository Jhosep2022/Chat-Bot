from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters

token = "6053341612:AAFma57Nkmqydr4Ft5PLlfRRoTM96ua2gPU"
user_name = "tonyclass_bot"
# Comandos
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hoola, soy un bot como estas andi")

async def help_command(update: Update, context: CallbackContext):
    await update.message.reply_text("Que necesitas andrea?")

# Esto ahora es un manejador de mensajes generales, no un comando.
async def handle_response(update: Update, context: CallbackContext):
    text = update.message.text.lower()

    if 'hola' in text:
        await update.message.reply_text("Hola andrea")
    elif 'como estas' in text:
        await update.message.reply_text("Bien y tu?")
    elif 'bien' in text:
        await update.message.reply_text("Me alegro")
    elif 'mal' in text:
        await update.message.reply_text("Que te pasa?")
    elif 'nada' in text:
        await update.message.reply_text("Ok")
    elif 'adios' in text:
        await update.message.reply_text("Adios andrea")
    else:
        await update.message.reply_text("No te entiendo andrea")

# Manejador de errores
async def error(update: Update, context: CallbackContext):
    print(f"Update {update} caused error {context.error}")
    await update.message.reply_text("Ha ocurrido un error")

# Main
if __name__ == '__main__':
    print("Bot iniciando")

    # Inicializa el bot con tu token
    app = Application.builder().token(token).build()

    # Registra los comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    # Registra el manejador de mensajes para procesar texto general
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response))

    # Registra el manejador de errores
    app.add_error_handler(error)

    # Inicia el bot
    print("Bot iniciado")
    app.run_polling()
