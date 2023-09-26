from telegram import Update, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardButton,InlineKeyboardMarkup
from telegram.ext import CallbackContext
from db import UserDB, SmartphoneDB
from currency import converter


userdb = UserDB('users.json')
smartphonedb = SmartphoneDB('smartphones.json')


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    keyboards = [
        [KeyboardButton('Valyuta'), KeyboardButton('Hisoblash')],
        [KeyboardButton('📝 About')]
    ]

    if userdb.is_user(user.id):
        update.message.reply_html(
            text="""Assalomu alaykum yana bir bor! qaytganingizdan xursandmiz.""",
            reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
        )
        return 

    userdb.add_user(chat_id=user.id, first_name=user.first_name, last_name=user.last_name, username=user.username)

    update.message.reply_html(
        text=f"""Assalomu alaykum <b>{user.full_name}</b>! Valyuta kursiga xush kelibsiz.""",
        reply_markup=ReplyKeyboardMarkup(keyboard=keyboards, resize_keyboard=True)
    )
    

def valyuta(update: Update, context: CallbackContext) -> None:
    USD=converter("USD",["UZS"])['data']['UZS']['value']
    EUR=converter("EUR",["UZS"])['data']['UZS']['value']
    RUB=converter("RUB",["UZS"])['data']['UZS']['value']
    update.message.reply_html(
        f"Valyutalarni Uzbek sumiga nisbattan qiymati quydagicha...\n\n1 AQSH dollari  {USD} sum\n1 Yevro  {EUR} sum\n1 Rubl  {RUB} sum\n Tashkil qiladi"
    )
    

# def hisoblash(update: Update, context: CallbackContext) -> None:
#     dollar=InlineKeyboardButton(text="DOLLAR", callback_data=f'DOLLAR')
#     yevro=InlineKeyboardButton(text="YEVRO", callback_data=f'YEVRO')
#     rubl=InlineKeyboardButton(text="RUBL", callback_data=f'RUBL')
    

#     close = InlineKeyboardButton(text='Close', callback_data='close')
#     keyboard=InlineKeyboardMarkup([[dollar,yevro,rubl],[close]])
   
#     update.message.reply_html(
#         text="Bulimlardan birini tanlang!!!",
#         reply_markup=keyboard
#     )
    
def hisoblash(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="Hisoblash summasini kiriting!!!",
    )

def hisobla(update: Update, context: CallbackContext) -> None:
    son=int(update.message.text)
    print(son)
    USD=float(converter("USD",["UZS"])['data']['UZS']['value'])
    EUR=float(converter("EUR",["UZS"])['data']['UZS']['value'])
    RUB=float(converter("RUB",["UZS"])['data']['UZS']['value'])
    update.message.reply_html(
        f"Valyutalarni Uzbek sumiga nisbattan qiymati quydagicha...\n\n{son} AQSH dollari  {son*USD} sum\n{son} Yevro  {son*EUR} sum\n{son} Rubl  {son*RUB} sum\n Tashkil qiladi"
    )

def about(update: Update, context: CallbackContext) -> None:
    update.message.reply_html(
        text="about"
    )