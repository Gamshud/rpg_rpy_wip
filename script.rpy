define plr = DynamicCharacter('pc.name', color="#29c44d")
define nch_1 = False
define cur_t = "0"

label start:
    show bg:
        zoom 0.667
    show character:
        pos (-15,150)
        zoom 0.6
    $ pc.face = "neutral"
    menu:
        plr "Обычное меню"
        
        "Что у меня с именем?":
            call name_change
        "Какая странная кнопка" if nch_1:
            call collar
        "Я повелитель времени!!!":
            jump time_c
        "Инвентарь (WIP)":
            show screen interface_inventory

    jump start
    return


label name_change:
    
    $ pc.face = "angry"
    plr "Чёрт! И кто же мне такое дурное имя придумал?"
    plr "Мне действительно нужно будет жить с ним всю жизнь?"
    plr "Да ну его к чёрту! Лучше поменяю на новое!"
    $ pc.name = renpy.input(u"А зовут меня...", default=pc.name, length = 15, allow="ячсмитьбюфывапролджэйцукенгшщзхъ-ЯЧСМИТЬБЮФЫВАПРОЛДЖЭЙЦУКЕНГШЩЗХЪ qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM").strip() or pc.name
    $ pc.face = "happy"
    plr "Так намного лучше!"
    $ pc.face = "neutral"
    $ nch_1 = True
    return

label time_c:
    $ cur_t = time.checktime()
    menu:
        "Сейчас [cur_t] \nНасколько мы хотим прокрутить время?"
        "1 час":
            $ time.minutesadd(60)
        "10 часов":
            $ time.hoursadd(10)
        "24 часа":
            $ time.hoursadd(24)
        "10 дней":
            $ time.minutesadd(14400)
        "Да ну его это время...":
            jump start
    jump time_c
    return
    
label collar:
    $ pc.additem("collar")
    plr "Хммм, странно у меня не понятно откуда появился {a=jump:use_collar}ошейник{/a}"
    plr "Пускай лежит спокойно в инвентаре, до лучших пор..."
    return
    
label use_collar:
    plr "Возможно стоит попробовать его надеть?"
    $ pc.face = "blush"
    $ pc.use_item("collar")
    plr "На удивление, не так и плохо смотрится..."
    plr "Стоит надевать его чаще"
    $ pc.face = "angry"
    plr "Хотя, о чем я вообще думаю?"
    plr "Нужно его снять, и чем быстрее тем лучше!"
    $ pc.face = "blush"
    plr "Или нет..."
    menu:
        "Снять?"
        "Снять, без вариантов!":
            $ pc.unequip_item("collar")
            $ pc.face = "neutral"
            plr "Вот и отлично, осталось только выкинуть его из инветаря..."
            $ pc.face = "angry"
            plr "Но учитывая что даже демка в разработке... это невозможно"

        "Вполне приятно выглядит, пускай останется...":
            $ pc.face = "blush"
            plr "Возможно однажды я смогу привыкнуть к нему"
    jump start
        
    return
    