import telebot
import json
from test_analys import user_result, answer_reducer

bot = telebot.TeleBot('token')

keyboard = telebot.types.InlineKeyboardMarkup()
one = telebot.types.InlineKeyboardButton(text='a', callback_data='А')
two = telebot.types.InlineKeyboardButton(text='b', callback_data='В')
keyboard.add(one, two)

questions_list = []
user_answer = {}


def quest_put():
    with open('questList.json', 'r', encoding='utf-8') as file:
        questions = json.load(file)
        for quest in questions:
            questions_list.append(quest)


@bot.message_handler(commands=['start'])
def hello_bot(message):
    chat_id = message.from_user.id
    text = 'С помощью методики К.Н. Томаса (1973), американского социального психолога, определяются ' \
           'типические способы реагирования на конфликтные ситуации. Можно выявить, насколько воспитатель склонен ' \
           'к соперничеству и сотрудничеству в коллективе, стремится к компромиссам, избегает конфликтов, или, ' \
           'наоборот, старается обострить их, а также оценить адаптации каждого члена коллектива к совместной ' \
           'педагогической деятельности.!\nВведите /continue, что бы начать тест'
    bot.send_message(chat_id, text)


@bot.message_handler(commands=['continue'])
def test_start(message):
    user_id = message.from_user.id
    text = questions_list[0]
    user_answer[user_id] = []
    bot.send_message(user_id, text, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def test_next(call):
    user_id = call.from_user.id
    index = questions_list.index(call.message.text) + 1
    answer = str(index) + call.data
    user_answer[user_id].append(answer)

    if index >= len(questions_list):
        text = 'Тест завершён!'
        bot.send_message(user_id, text)
        result = user_result(user_answer[user_id], answer_reducer)
        bot.send_message(user_id, result)
        return

    text = questions_list[index]
    bot.send_message(user_id, text, reply_markup=keyboard)


if __name__ == '__main__':
    quest_put()
    bot.polling(none_stop=True)
