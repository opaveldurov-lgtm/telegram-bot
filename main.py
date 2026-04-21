import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8769931246:AAGFUfyV6QujcMkh-SMmuXyOY_eDmLI2vxU"

users = {}

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Referral tekshirish
    if context.args:
        ref_id = int(context.args[0])
        if ref_id != user_id:
            users.setdefault(ref_id, {"refs": 0})
            users[ref_id]["refs"] += 1

    users.setdefault(user_id, {"refs": 0})

    text = f"""
👋 Salom!

🎯 Signal olish uchun /signal bosing
👥 Referallaringiz: {users[user_id]["refs"]}

🔗 Sizning linkingiz:
https://t.me/{context.bot.username}?start={user_id}
"""

    await update.message.reply_text(text)

# Signal komandasi
async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    coef = round(random.uniform(1.1, 3.0), 2)

    if coef < 1.5:
        msg = f"🔴 Past signal: {coef}x gacha"
    elif coef < 2.0:
        msg = f"🟡 O‘rtacha signal: {coef}x gacha"
    else:
        msg = f"🟢 Kuchli signal: {coef}x gacha"

    await update.message.reply_text(msg)

# Botni ishga tushirish
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("signal", signal))

print("Bot ishlayapti...")
app.run_polling()
