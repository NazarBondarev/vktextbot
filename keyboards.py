from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboard




def general_keyb():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Хочу промо-код', color=VkKeyboardColor.POSITIVE)
    keyboard.add_button('Персональный купон', color=VkKeyboardColor.POSITIVE) 
    keyboard.add_line() 
    keyboard.add_button('Часто задаваемые вопросы', color=VkKeyboardColor.POSITIVE)
    keyboard.add_line() 
    keyboard.add_button('Связь с тех поддержкой', color=VkKeyboardColor.POSITIVE)

    return keyboard

def personal_cupon():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Как получить персональный купон?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line() 
    keyboard.add_button('Я уже долго жду купон. Когда он придет?', color=VkKeyboardColor.PRIMARY) 
    keyboard.add_line() 
    keyboard.add_button('Можно ускорить выдачу купона?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line() 
    keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)

    return keyboard

def faq():
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('У меня не выводится скин!', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line() 
    keyboard.add_button('Почему скин сам продался из инвентаря?', color=VkKeyboardColor.PRIMARY) 
    keyboard.add_line() 
    keyboard.add_button('У меня трейд-бан. Что делать?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line() 
    keyboard.add_button('Можно ли с Вами сотрудничать?', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line() 
    keyboard.add_button('Меню', color=VkKeyboardColor.NEGATIVE)

    return keyboard