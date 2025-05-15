
# Ваши данные в виде словаря для удобного доступа
MENU_DATA = {

    "1": [
        {"text": "Куклы", "callback_data": "levl_1.1", "photo": "media/photo_levl_1.1.jpg","caption": 'Раздел "Куклы":'},
        {"text": "Машинки", "callback_data": "levl_1.2", "photo": "media/photo_levl_1.2.jpg","caption": 'Раздел "Машинки":'},
        {"text": "Лего", "callback_data": "levl_1.3", "photo": "media/photo_levl_1.3.jpg","caption": 'Раздел "Лего":'}
    ],
    "1.1": [
        {"text": "Барби", "callback_data": "levl_1.1.1", "photo": "media/photo_levl_1.1.1.jpg","caption": "Выберите:"},
        {"text": "Брац", "callback_data": "levl_1.1.2", "photo": "media/photo_levl_1.1.2.jpg","caption": "Выберите:"},
        {"text": "Винкс", "callback_data": "levl_1.1.3", "photo": "media/photo_levl_1.1.3.jpg","caption": "Выберите:"}
    ],
    "1.2": [
        {"text": "Трасформеры", "callback_data": "levl_1.2.1","photo": "media/photo_levl_1.2.1.jpg","caption": "Выберите:"},
        {"text": "Форсаж", "callback_data": "levl_1.2.2","photo": "media/photo_levl_1.2.2.jpg","caption": 'Набор машинок "Форсаж" - 2000 рублей.'},
        {"text": "Тачки", "callback_data": "levl_1.2.3","photo": "media/photo_levl_1.2.3.jpg","caption": 'Набор машинок "Тачки 2" - 1999 рублей. '},
        {"text": "ХотВилс", "callback_data": "levl_1.2.4","photo": "media/photo_levl_1.2.4.jpg","caption": 'ХотВилс'},

    ],
    "1.3": [
        {"text": "Лего Гарри Поттер", "callback_data": "levl_1.3.1","photo": "media/photo_levl_1.3.1.jpg","caption": 'Набор Лего "Гарри Поттер - Хогвардс" - 5999 рублей'},
        {"text": "Лего Бэтмен", "callback_data": "levl_1.3.2","photo": "media/photo_levl_1.3.2.jpg","caption": 'Набор Лего "Бэтмен - Бэтвинг" - 4999 рублей.'},
        {"text": "Лего Марвел", "callback_data": "levl_1.3.3", "photo": "media/photo_levl_1.3.3.jpg","caption": 'Марвел'},
    ],

    # Уровень 3 (Конкретные товары)
    "1.1.1": [
        {"text": "Барби", "callback_data": "levl_1.1.1.1","photo": "media/photo_levl_1.1.1.1.jpg","caption": "Кукла Барби - 2999 рублей"},
        {"text": "Кен", "callback_data": "levl_1.1.1.2","photo": "media/photo_levl_1.1.1.2.jpg","caption": "Кукла Кен - 1990 рублей. "},
        {"text": "Барби Экстра", "callback_data": "levl_1.1.1.3","photo": "media/photo_levl_1.1.1.3.jpg","caption": "Барби Экстра- 1990 рублей."},
        {"text": "Барби Эксклюзивная", "callback_data": "levl_1.1.1.4","photo": "media/photo_levl_1.1.1.4.jpg","caption": "Барби Эксклюзивная- 1990 рублей."}
    ],
    "1.1.2": [
        {"text": "Хлоя", "callback_data": "levl_1.1.2.1","photo": "media/photo_levl_1.1.2.1.jpg","caption": "Кукла Хлоя - 2200 рублей."},
        {"text": "Даша", "callback_data": "levl_1.1.2.2","photo": "media/photo_levl_1.1.2.2.jpg","caption": "Кукла Дана - 2200 рублей. "},
        {"text": "Саша", "callback_data": "levl_1.1.2.3","photo": "media/photo_levl_1.1.2.3.jpg","caption": "Кукла Саша - 3330 рублей. "},
        {"text": "Ясмин", "callback_data": "levl_1.1.2.4", "photo": "media/photo_levl_1.1.2.4.jpg","caption": "Ясмин - 2200 рублей."},
        {"text": "Анжела", "callback_data": "levl_1.1.2.5", "photo": "media/photo_levl_1.1.2.5.jpg","caption": "Анжела - 2200 рублей."},

    ],
    "1.1.3": [
        {"text": "Блум", "callback_data": "levl_1.1.3.1", "photo": "media/photo_levl_1.1.3.1.jpg",
         "caption": "Кукла блум - 3200 рублей. "},
        {"text": "Флора", "callback_data": "levl_1.1.3.2", "photo": "media/photo_levl_1.1.3.2.jpg",
         "caption": "Кукла Флора - 3330 рублей."},
        {"text": "Текна", "callback_data": "levl_1.1.3.3", "photo": "media/photo_levl_1.1.3.3.jpg",
         "caption": "Кукла Текна - 2500 рублей. "},
        {"text": "Муза", "callback_data": "levl_1.1.3.4", "photo": "media/photo_levl_1.1.3.4.jpg",
         "caption": "Кукла Муза - 3200 рублей "},
        {"text": "Стелла", "callback_data": "levl_1.1.3.5", "photo": "media/photo_levl_1.1.3.5.jpg",
         "caption": "Кукла Стелла - 2200 рублей "},
    ],
# Уровень 3 (Конкретные товары)
    "1.2.1": [
        {"text": "Бамблби", "callback_data": "levl_1.2.1.1","photo": "media/photo_levl_1.2.1.1.jpg","caption": 'Машинка-трансформер "Бамблби" - 2999 рублей.'},
        {"text": "Оптимус Прайм", "callback_data": "levl_1.2.1.2","photo": "media/photo_levl_1.2.1.2.jpg","caption": 'Машинка-трансформер "Оптимус Прайм" - 2999 рублей.'},
        {"text": "Мегатрон", "callback_data": "levl_1.2.1.3","photo": "media/photo_levl_1.2.1.3.jpg","caption": 'Машинка-трансформер "Мегатрон" - 2999 рублей.'}
    ],
    "1.2.4": [
        {"text": "Набор 32 машинки", "callback_data": "levl_1.2.4.1","photo": "media/photo_levl_1.2.4.1.jpg","caption": 'Набор 32 машинки - 2999 рублей.'},
        {"text": "Набор 5 машинок", "callback_data": "levl_1.2.4.2","photo": "media/photo_levl_1.2.4.2.jpg","caption": 'Набор 5 машинок" - 2999 рублей.'},
        {"text": "Машинка Hot Garage", "callback_data": "levl_1.2.4.3","photo": "media/photo_levl_1.2.4.3.jpg","caption": 'Машинка Hot Garage" - 2999 рублей.'},
        {"text": "Машинка Couple Clip", "callback_data": "levl_1.2.4.4","photo": "media/photo_levl_1.2.4.4.jpg","caption": 'Машинка Couple Clip" - 2999 рублей.'}
    ],
    "1.3.3": [
        {"text": "Набор Лего Thor vs. Sathur", "callback_data": "levl_1.3.3.1", "photo": "media/photo_levl_1.3.3.1.jpg",
         "caption": 'Набор Лего Thor vs. Sathur'},
        {"text": "Набор Лего Геликарриер", "callback_data": "levl_1.3.3.2", "photo": "media/photo_levl_1.3.3.2.jpg",
         "caption": 'Набор Лего Геликарриер" - 2999 рублей.'},
        {"text": "Лаборатория Железного Человека", "callback_data": "levl_1.3.3.3", "photo": "media/photo_levl_1.3.3.jpg",
         "caption": 'Набор Лего "Марвел. Лаборатория Железного Человека" - 7999 рублей. '}
    ]
}