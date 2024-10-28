# !!! Информация !!!
    # База скрипта - Валерка Ребров, Илья Суворов
    # Разработка скрипта - Мелентий Першин


# -------------------------------------------------------------------------------------------------------------------



# !!! Инструкция !!!
    # Доброго времени суток, уважаемый крутой человек
    # Инструкция по использования данного скрипта:
    # 
    # Для активации вам достаточно запустить его где угодно, хоть в командой строке
    # После активации вам нужно будет заполнить оперделенные поля
    # В случае ошибки - проверьте что все правильно и перезапустите скрипт
    # На данный момент, сайт для использования еще находится в разработке
    # Теперь пройдемся по каждому пункту:
    # 
    # - Введите ник-нейм модератора
    # Указываете никнейм модератора
    # 
    # Введите discordID
    # Указываете дискорд ID модератора
    # 
    # Введите уровень модератора(1-4)
    # Указываете уровень модератора, ОБЯЗАТЕЛЬНО указывать число от 1 до 4
    # в ином случае будет неверный подсчет
    # 
    # Введите количество действий
    # Указываете общее количество действий
    # 
    # Сколько занято категорий в top?
    # Тут важно, смотрите по категориям top сколько человек занял топов
    # после чего это число вводите сюда. Например: модератор занял топ по мутам и по банам
    # вы вписываете число 2
    # 
    # Хотите добавить еще одного модератора? (+/-)
    # "+" это добавить еще одного
    # "-" это закончить список
    # 
    # Умножение зарплаты (1 - оставить как есть)
    # Указывается множетель зп, для обычной зп указывать 1, укажите 0 - будет по нулям всё


# -------------------------------------------------------------------------------------------------------------------


# ОСНОВНОЙ КОД
# ОСНОВНОЙ КОД
# ОСНОВНОЙ КОД


# Норма зарплаты модерации
# Для изменения: 1 число - уровень, 2 число - норма
norms = {1: 20, 2: 15, 3: 10, 4: 5}

# Рассчет зарплаты ( !! НЕ ТРОГАТЬ !! )
def calculate_salary(level, actions):

    norm = norms.get(level, 0)

    # Фиксированная зарплата модерации
    # Для изменения: 1 число - уровень, 2 число - зарплата
    pearls = {1: 45, 2: 40, 3: 35, 4: 35}

    # Рассчитываение выдачи бонуса ( !! НЕ ТРОГАТЬ ЕСЛИ НЕ ЗНАЕШЬ !! )
    bonus = 0
    if actions > norm:
        over_performance = actions - norm
        bonus = 5 * (over_performance // 5)

    return {"pearls": pearls.get(level, 0), "bonus": bonus}

# Форматирование информации ( !! НЕ ТРОГАТЬ !! )
def format_salary_info(nickname, level, actions, is_top_performer=False):


    result = calculate_salary(level, actions)
    norm = norms.get(level, 0)
    over_performance = actions - norm

    # Проверка на выполнение нормы
    warning = ""
    if actions < norm:
        warning = f">> ⚠️  {nickname} получает выговор - невыполнение еженедельной нормы!\n"  # Отступ в одну строку

    # Дополнительные жемчужины и бонусы для лидера
    if is_top_performer:
        result['pearls'] += 30
        result['bonus'] += 30
        warning = f">> 💎 Дополнительно: 30 бонусов и 30 жемчужин за лучшего модератора недели по действиям.\n" + warning  # Отступ в одну строку

    # Сама информация ( !! Изменять можно только текст в ковычках и все !! )
    return {
        "info": f"🚹 | Уровень {level}: {nickname}\n"
                f"📔 | Всего действий: {actions}\n"
                f"📋 | Недельная норма: {norm}\n"
                f"🍀 | Перевыполнение: {over_performance}\n"
                f"💰 | Зарплата: {result['pearls'] * more2 - 30 * (more2 - 1)} жемчужин\n"
                f"🎁 | Бонусы: {result['bonus'] * more2 - 30 * (more2 - 1)} бонусов\n"
                + warning,
        "pearls": result['pearls'],
        "bonus": result['bonus']
    }

# Ввод основных данных ( !! Изменять можно только текст в ковычках и все !! )
moderators = []
while True:
    nickname = input("Введите ник-нейм модератора: ")
    discordid = int(input("Введите discordID: "))
    level = int(input("Введите уровень модератора(1-4): "))
    actions = int(input("Введите количество действий: "))
    
    # Сохраняем данные модератора
    moderators.append((nickname, level, actions, discordid))
    
    # Спрашиваем, хотите ли вы ввести данные для еще одного модератора
    # !! ВСЕ ЧТО НИЖЕ НЕ ТРОГАТЬ БЕЗ ЗНАНИЯ ПИТОНА !!
    # !! ВСЕ ЧТО НИЖЕ НЕ ТРОГАТЬ БЕЗ ЗНАНИЯ ПИТОНА !!
    # !! ВСЕ ЧТО НИЖЕ НЕ ТРОГАТЬ БЕЗ ЗНАНИЯ ПИТОНА !!
    top = int(input('Сколько занято категорий в top? (0 если нисколько): '))
    more = input("Хотите добавить еще одного модератора? (+/-): ").strip().lower()
    if more != '+':
        more2 = int(input("Умножение зарплаты (1 - оставить как есть): ").strip().lower())
        if more2 == '1':
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            # Определяем модератора с наибольшим количеством действий
            top_performer = max(moderators, key=lambda x: x[2])

            # Определяем модератора с наименьшим количеством действий
            bottom_performer = min(moderators, key=lambda x: x[2])

            # Сортируем модераторов по убыванию количества действий
            moderators.sort(key=lambda x: x[2], reverse=True)

            # Вывод информации для всех модераторов
            for nickname, level, actions, discordid in moderators:
                is_top_performer = (nickname == top_performer[0] and actions == top_performer[2])
                is_bottom_performer = (nickname == bottom_performer[0] and actions == bottom_performer[2])
                result = format_salary_info(nickname, level, actions, is_top_performer)
                print(result['info'])
                if not is_bottom_performer:
                    print("__________________________________________________")  # Замена разделителя
                    print("") # Добавляем пустую строку для отступа

            # Вывод команд для выдачи жемчужин и бонусов
            for nickname, level, actions, discordid in moderators:
                result = format_salary_info(nickname, level, actions)
                
                # Вычисляем бонусы и жемчужины с учетом дополнительных бонусов для лучшего модератора
                bonus_with_extra = result['bonus']
                pearls_with_extra = result['pearls']
                if nickname == top_performer[0]:
                    bonus_with_extra += 30
                    pearls_with_extra += 30

                print(f"💰 | Вылача зарплаты модератору: {nickname}")
                print(f"/mcoins action-type:Добавить коины target:{discordid} amount:{pearls_with_extra}")
                print(f"!addbonus <@{discordid}> {bonus_with_extra}")
                print(f" ")
        else:
            print(" ")
            print(" ")
            print(" ")
            print(" ")
            print(" ")
                        # Определяем модератора с наибольшим количеством действий
            top_performer = max(moderators, key=lambda x: x[2])

            # Определяем модератора с наименьшим количеством действий
            bottom_performer = min(moderators, key=lambda x: x[2])

            # Сортируем модераторов по убыванию количества действий
            moderators.sort(key=lambda x: x[2], reverse=True)

            # Вывод информации для всех модераторов
            for nickname, level, actions, discordid in moderators:
                is_top_performer = (nickname == top_performer[0] and actions == top_performer[2])
                is_bottom_performer = (nickname == bottom_performer[0] and actions == bottom_performer[2])
                result = format_salary_info(nickname, level, actions, is_top_performer)
                print(result['info'])
                if not is_bottom_performer:
                    print("__________________________________________________")  # Замена разделителя
                    print("") # Добавляем пустую строку для отступа

            # Вывод команд для выдачи жемчужин и бонусов
            for nickname, level, actions, discordid in moderators:
                result = format_salary_info(nickname, level, actions)
                
                # Вычисляем бонусы и жемчужины с учетом дополнительных бонусов для лучшего модератора
                bonus_with_extra = result['bonus']
                pearls_with_extra = result['pearls']
                if nickname == top_performer[0]:
                    bonus_with_extra += 30
                    pearls_with_extra += 30
                if top == 0:
                    print(f"💰 | Вылача зарплаты модератору:", nickname)
                    print(f"/mcoins action-type:Добавить коины target:{discordid} amount:{pearls_with_extra * more2 - 30 * (more2 - 1)}")
                    print(f"!addbonus <@{discordid}>", bonus_with_extra * more2 - 30 * (more2 - 1))
                    print(f" ")
                else:
                    print(f"💰 | Вылача зарплаты модератору:", nickname)
                    print(f"/mcoins action-type:Добавить коины target:{discordid} amount:{pearls_with_extra * more2 - 30 * (more2 - 1) + 5 * top}")
                    print(f"!addbonus <@{discordid}>", bonus_with_extra * more2 - 30 * (more2 - 1) + 5 * top)
                    print(f" ") 
        break