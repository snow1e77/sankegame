from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Вставьте ваш токен
TOKEN = "8136222979:AAG7Y2m9LJ9O3h3JiZiswuVqolFa1Cw66dk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправка приветственного сообщения с кнопкой для запуска игры"""
    keyboard = [[InlineKeyboardButton("Играть в змейку 🐍", callback_data="play_snake")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Привет! Нажми на кнопку, чтобы сыграть в змейку!", reply_markup=reply_markup)

async def play_snake(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Отправка ссылки на игру"""
    query = update.callback_query
    await query.answer()
    # Замените ссылку на ваш хостинг с игрой
    game_url = "https://your-domain.com/snake-game.html"
    await query.edit_message_text(f"Нажмите на ссылку, чтобы играть: [Играть в змейку]({game_url})", parse_mode="Markdown")

def main():
    # Создаем приложение
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчики
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(play_snake, pattern="play_snake"))

    # Запуск бота
    application.run_polling()
    print("Бот запущен. Нажмите Ctrl+C для остановки.")

if __name__ == "__main__":
    main()
