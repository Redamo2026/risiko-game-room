import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.environ["BOT_TOKEN"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 Benvenuto nella Risiko Game Room!\n\n"
        "Il gioco è in preparazione.\n\n"
        "Comandi disponibili:\n"
        "/nuova_partita - Crea una nuova partita\n"
        "/unisciti - Unisciti alla partita\n"
        "/inizia - Inizia la partita\n"
        "/stato - Mostra lo stato della partita"
    )


async def nuova_partita(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎲 NUOVA PARTITA\n\n"
        "Redamo ha creato una nuova partita!\n\n"
        "👥 Giocatori: 1/6\n"
        "🟢 Usa /unisciti per partecipare."
    )


async def unisciti(update: Update, context: ContextTypes.DEFAULT_TYPE):
    nome = update.effective_user.first_name

    await update.message.reply_text(
        f"👤 {nome} si è unito alla partita!\n\n"
        "🎲 Giocatori: in preparazione..."
    )


async def inizia(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 LA PARTITA STA PER INIZIARE!\n\n"
        "🎲 Preparazione dei giocatori...\n"
        "🗺️ Preparazione dei territori...\n"
        "🪖 Distribuzione delle armate...\n\n"
        "Questa è la prima versione di prova."
    )


async def stato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📊 STATO PARTITA\n\n"
        "🎲 Partita: non ancora iniziata\n"
        "👥 Giocatori: in preparazione\n"
        "🗺️ Territori: non ancora assegnati"
    )


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("nuova_partita", nuova_partita))
    app.add_handler(CommandHandler("unisciti", unisciti))
    app.add_handler(CommandHandler("inizia", inizia))
    app.add_handler(CommandHandler("stato", stato))

    print("Risiko Game Room avviato!")
    app.run_polling()


if __name__ == "__main__":
    main()
