init python:
    #Инициализация питона
    def draw_character(st, at):
        #Функция которая принимает в себя параметры частоты обновления (лучше оставить стандартными и не трогать)
        return LiveComposite(
            #Вызов функции LiveComposite
            (591, 1000),
            #Первым кортежем передаем базовое разрешение изображений, в моем случае (591, 1000)
            (0, 0), "images/characters/pc/"+ pc.race +"/body/" + pc.race + "1" + ".png",
            #Тело прорисовываем первым оно будет ниже всего остального
            (0, 0), "images/characters/pc/"+ pc.race +"/tattoo/" + pc.img_acc["face_tat"] + ".png",
            (0, 0), "images/characters/pc/"+ pc.race +"/emotions/" + pc.face + ".png",
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["ring1"] + ".png",
            #В пути мы обязательно должны указать  
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["ring2"] + ".png",
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["bracers"] + ".png",
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["neck"] + ".png",
            #Слой шеи расположен выше чем слой брони или одежды, соответственно если мы будем прорисовывать сперва "колье"
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["body"] + ".png",
            #А потом будем прорисовывать броню, то она будет перекрывать собой часть "колье" или другого украшения которе ближе к телу
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["legs"] + ".png",
            (0, 0), "images/characters/pc/"+ pc.race +"/items/" + pc.img_acc["bots"] + ".png"
            ),.1

init:
    image character = DynamicDisplayable(draw_character)
    #После инициализации объявляем что character это постоянный вызов функции DynamicDisplayable которая соответственно вызывает функцию draw_character без аргументов.
     