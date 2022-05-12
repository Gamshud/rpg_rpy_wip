#
define items = {
#Надеваемые шмотки
    "collar": {
        "intel":3,
        "slot":"neck",
        "max_intel":5,
        #Тип
        "type":"equippable", #consumable or equippable 
        #Название Предмета
        "itemn":"collar",
        #Название предмета для игрока
        "itemna":_("Ошейник"),
        #Описание предмета в подсказке
        "desc":_("Просто прикольный ошейник, а вот зачем он тебе - я не знаю..."),
        #Сообщение при надевании предмета
        "notyadd":"+",
        "noty":_("Воу, зачем же надевать на себя ошейник?!"),
        "model":"collar1",
        #Иконка предмета
        "img_i":"images/inventory/collar_idle.png",
        "img_h":"images/inventory/collar_hover.png"
    },
#
#
######
#   
#Применяемые шмотки
    "cookie":{
        #Тип
        "type":"consumable",
        "hp_add":10,
        "mp_add":10,
        #Бонусы здоровья\маны
        "max_hp":0,
        "max_mp":0,
        #Максимальный порог статов
        "max_strength":0,
        "max_intel":0,
        "max_agil":0,
        #Текущие статы
        "strength":0,
        "agil":0,
        "intel":0,
        #Опыт
        "xp_add":0,
        "lvl":0,
        "xp_rate":0,
        #Несовместимые предметы (нельзя это есть )
        "itemincompatibility":["a"],
        #Время действия (минут)
        "timeact":30,
        #Название Предмета
        "itemn":"cookie",
        #Название предмета для игрока
        "itemna":_("Печенька"),
        #Описание предмета в подсказке
        "desc":_("Вкусное печенье."),
        #Сообщение при надевании предмета
        "noty":_("Ты кушаешь вкусную печеньку"),
        #Иконка предмета
        "img_i":"images/inventory/сookie_idle.png",
        "img_h":"images/inventory/сookie_hover.png"
    }
}
