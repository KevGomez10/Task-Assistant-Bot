from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 🟢 Token de tu bot (copiar desde BotFather)
TOKEN = "8208737555:AAFyJFmYdgV3hKTkcC39oFzLwgwa0C2fcbU"

# 📌 Lista de tareas en memoria (por ahora temporal)
tareas = []

# 👋 Comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("¡Hola! Soy tu Task Bot 🤖. Escríbeme tus pendientes y yo los guardaré.")

# 📝 Agregar tareas al escribir cualquier texto
async def add_task(update: Update, context: ContextTypes.DEFAULT_TYPE):
    tarea = update.message.text
    tareas.append(tarea)
    await update.message.reply_text(f"✅ Tarea añadida: {tarea}")

# 📋 Ver tareas guardadas
async def list_tasks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if tareas:
        mensaje = "📋 Tus tareas pendientes:\n" + "\n".join([f"- {t}" for t in tareas])
    else:
        mensaje = "No tienes tareas pendientes 🙌"
    await update.message.reply_text(mensaje)

# 🚀 Función principal
def main():
    app = Application.builder().token(TOKEN).build()

    # Comandos
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("tareas", list_tasks))

    # Mensajes normales (agregar tareas)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, add_task))

    print("🤖 Bot en marcha...")
    app.run_polling()

if __name__ == "__main__":
    main()
