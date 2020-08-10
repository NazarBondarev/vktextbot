# -*- coding: utf-8 -*-


import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.longpoll import VkLongPoll, VkEventType
from keyboards import general_keyb, personal_cupon, faq
from settings import s as settings
from settings import letters, admins
import vk_api.exceptions
import time
from vk_api.upload import VkUpload
import json


token = "TOKEN"



vk_session = vk_api.VkApi(token=token)

vk = vk_session.get_api()

longpoll = VkLongPoll(vk_session)

def upload_photo(upload, photo):
	response = upload.photo_messages(photo)[0]
	owner_id = response['owner_id']
	photo_id = response['id']
	access_key = response['access_key']

	return owner_id, photo_id, access_key

def send_photo(vk, user_id, owner_id, photo_id, access_key, message):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        user_id=user_id,
        attachment=attachment,
        message = message
    )



def update_users_list():
	with open('./data/data.json', 'r', encoding = 'UTF-8') as read_users:
		users = json.load(read_users)
		return users

def write_new_user(users_list):
	with open('./data/data.json', 'w', encoding = 'UTF-8') as write_users:
		json.dump(users_list, write_users, ensure_ascii=False, indent=4)


if __name__ == "__main__":
	users_list = update_users_list()
	upload = VkUpload(vk)
	while True:
		for event in longpoll.listen():
			if event.type == VkEventType.MESSAGE_NEW and event.to_me:
				if event.user_id not in users_list:
					users_list.append(event.user_id)
					write_new_user(users_list)

				if event.text == 'Привет' or event.text == "привет":
					user_id = event.user_id
					print(user_id)
					name = vk.users.get(user_id=user_id)[0]['first_name']
					
					vk.messages.send(
					user_id = event.user_id,
					message = f"Привет, {name}. Я - Case-Battle Бот. Могу попробовать ответить на самые часто-задаваемые вопросы 😉",
					random_id = get_random_id(),
					keyboard = general_keyb().get_keyboard(),
					)

				elif event.text == 'Персональный купон':
					vk.messages.send(
					user_id = event.user_id,
					message = "Меню персонального купона",
					random_id = get_random_id(),
					keyboard = personal_cupon().get_keyboard(),
					)

				elif event.text == 'Меню':
					vk.messages.send(
					user_id = event.user_id,
					message = "Меню бота",
					random_id = get_random_id(),
					keyboard = general_keyb().get_keyboard(),
					)

				elif event.text == 'Часто задаваемые вопросы':
					vk.messages.send(
					user_id = event.user_id,
					message = "Посмотрите список самых часто задаваемых вопросов:",
					random_id = get_random_id(),
					keyboard = faq().get_keyboard(),
					)

				elif event.text == 'У меня не выводится скин!':
					message = """Если прошло более 15-ти минут, то обратитесь, пожалуйста, в техподдержку на сайте. 
					Они посмотрят, в чем может быть причина и обязательно помогут 😏
					P.S. Кнопка чата находится в правом нижнем углу на всех страницах нашего сайта ⬇"""
					send_photo(vk, event.user_id, *upload_photo(upload, './src/tech_support.jpg'), message)

				elif event.text == 'Почему скин сам продался из инвентаря?':
					message = """Мы даем на вывод предмета - 12 часов. 
					По истечении этого времени предмет автоматически продается, и деньги за предмет начисляются на ваш баланс. 
					Если Ваш скин сам продался, Вы хотите его обратно и ❗еще не потратили деньги с баланса❗, то мы можем попробовать Вам его вернуть. Для этого обратитесь, пожалуйста, в техподдержку на сайте. P.S. 
					Кнопка чата находится в правом нижнем углу на всех страницах нашего сайта ⬇"""
					send_photo(vk, event.user_id, *upload_photo(upload, './src/tech_support.jpg'), message)

				elif event.text == 'У меня трейд-бан. Что делать?':
					message = """Если на Вашем Steam аккаунте трейд-бан, то мы можем отключить Вам авто-продажу предметов на срок до 15-ти дней. 
					Для этого обратитесь, пожалуйста, в техподдержку на сайте и сообщите им, до какого числа нужно отменить авто-продажу.
					P.S. Кнопка чата находится в правом нижнем углу на всех страницах нашего сайта ⬇"""
					send_photo(vk, event.user_id, *upload_photo(upload, './src/tech_support.jpg'), message)

				elif event.text == 'Можно ли с Вами сотрудничать?':
					message = \
					"""Вы можете отправить предложение о сотрудничестве на email partner@case-battle.net или в личные сообщения менеджера по рекламе https://vk.com/id558492278. 
					Для быстрого ответа указывайте какого рода сотрудничество вы предлагаете. Спасибо."""

					vk.messages.send(
					user_id = event.user_id,
					message = message,
					random_id = get_random_id())
																			


				elif event.text == 'Хочу промо-код':
					vk.messages.send(
					user_id = event.user_id,
					message = f"Самый свежий промо - {settings['promocode']} который дает +{settings['percent']}% к пополнению."\
					"Также Вы можете посмотреть промо в шапке сайта, возможно он круче",
					random_id = get_random_id())

				elif event.text == 'Связь с тех поддержкой':
					send_photo(vk, event.user_id, *upload_photo(upload, './src/tech_support.jpg'), 
						"Для связи с операторами техподдержки Вы всегда можете использовать чат на сайте."\
        				"Кнопка чата находится в правом нижнем углу на всех страницах нашего сайта." \
        				"Время работы с 10:00 до 22:00 МСК."\
        				"В нерабочее время Вы также можете оставить там свой вопрос, мы ответим как можно быстрее в рабочие часы 😉")

				elif event.text == 'Как получить персональный купон?':
					vk.messages.send(
					user_id = event.user_id,
					message = """Для того, чтобы получить персональный купон укажите свою почту в профиле на сайте.
					📬Больше никаких действий для получения промокода не требуется 🙂""",
					random_id = get_random_id())

				elif event.text == 'Я уже долго жду купон. Когда он придет?':
					vk.messages.send(
					user_id = event.user_id,
					random_id = get_random_id(),
					message= """Купоны рассылаются системой автоматически и, к сожалению, мы не знаем точной даты, когда и кому он придет. 
					Купонов меньше, чем пользователей. Поэтому остается только ждать 😞""")


				elif event.text == 'Можно ускорить выдачу купона?':
					vk.messages.send(
					user_id = event.user_id,
					random_id = get_random_id(),
					message= """К сожалению, у нас нет возможности ускорить выдачу персонального купона, т.к. они рассылаются системой автоматически 😞""")

				elif event.text not in letters and not event.text.startswith('/setpromo') and not event.text.startswith('/m'):
					message = """Я не понимаю твоей команды😕Сейчас покажу тебе все доступные команды"""
					vk.messages.send(
					user_id = event.user_id,
					random_id = get_random_id(),
					keyboard = general_keyb().get_keyboard(),
					message = message
					)

				elif event.text.startswith("/setpromo") and len(event.text) > 9 and event.user_id in admins:
					new_promo = event.text.split(' ')
					settings['promocode'] = new_promo[1]
					settings['percent'] = new_promo[2]
					message = f"""Установлен новый промокод - {new_promo[1]}. Процент {new_promo[2]}"""
					vk.messages.send(
					user_id = event.user_id,
					random_id = get_random_id(),
					keyboard = general_keyb().get_keyboard(),
					message = message
					)

				elif event.text.startswith('/m') and event.user_id in admins:
					message_for_malling = event.text.replace('/m', '')

					try:

						for users in users_list:
							vk.messages.send(
							user_id = users,
							random_id = get_random_id(),
							message = message_for_malling
						)

					except Exception:
						pass

			
		time.sleep(1)

