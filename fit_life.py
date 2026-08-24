# Проект FitLife - MVP версия 1.0

#Запрос имени пользователя
user_name = input('Здравствуйте, введите ваше имя:')

#Запрос возраста пользователя
user_age = int(input('Введите ваш возраст:'))

#Запрс веса пользователя в кг.
user_weight = float(input('Введите ваш вес в кг.:'))

#Запрос роста пользователя в метрах
user_height = float(input('Введите ваш рост в метрах используя точку:'))

#Расчет индекса массы тела
bmi = round(user_weight / (user_height ** 2), 1)

WATER_PER_KG = 30
#расчет потребленя воды в мл.
water_ml = user_weight * WATER_PER_KG

#Переводим мл. в литры
water_l = round(water_ml / 1000, 1)

print(f'Отчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi}')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print()
print("Расчет окончен. Будьте здоровы!")