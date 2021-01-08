import pygame

from color import *



class Interface:

    def __init__(self):

        self.up_group = Group(line_weight = 4, text_scale_multiplier = 1.15, text_y_offset = -5)
        up_group.append(Widget(                 weight = 4, text = "Уровень 1", clickable = False))
        up_group.append("\n")
        up_group.append(Widget( weight = 4, text = "Шаги: "))
        up_group.append("\n")
        up_group.append(Widget( weight = 4, text = "Лучший результат: "))

        self.square_group = Group(line_weight = 4, gap = 2, square_buttons = True)
        square_group.append(Widget(id = "square 1" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 2"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 3"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 4", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append(Widget(id = "square 5"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 6", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")
        square_group.append(Widget(id = "square 7" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 8"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 9"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 10", weight = 1, color_pack = list(GREY_LT_PACKK)   , text = "" ))
        square_group.append(Widget(id = "square 11"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 12", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")
        square_group.append(Widget(id = "square 13" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 14"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 15"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 16", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append(Widget(id = "square 17"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 18", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")
        square_group.append(Widget(id = "square 19" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 20"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 21"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 22", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append(Widget(id = "square 23"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 24", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")
        square_group.append(Widget(id = "square 25" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 26"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 27"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 28", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append(Widget(id = "square 29"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 30", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")
        square_group.append(Widget(id = "square 31" , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 32"   , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 33"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 34", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append(Widget(id = "square 35"  , weight = 1, color_pack = list(GREY_LT_PACK)    , text = ""))
        square_group.append(Widget(id = "square 36", weight = 1, color_pack = list(GREY_LT_PACK)   , text = "" ))
        square_group.append("\n")

    def draw(self, surface):
        width, height = surface.get_size()

    """    pygame.draw.rect(surface, (0, 0, 255), [width//2 - 100,
                                               height//2 - 100,
                                               width //4,
                                               height//4])
"""

#надо смотреть на вывод и писать, я тупая
    def recalculate(window_size):
        """
        Перерасчет положения и размеров групп при изменении размера окна. Позволяет интерфейсу масштабироваться.
        Изменение параметров групп заставит их пересчитать свои widgets
        """
        groups = self.groups()
        UP_group    = groups[0]
        square_group = groups[1]

    """    window_gap    = 10
        menu_x        = window_gap
        menu_y        = (window_size[0]-window_gap*2)*0.2+window_gap
        menu_width    = (window_size[0] - window_gap*2)
        menu_height   = (window_size[1] - window_gap*2) * 0.2
        menu_gap      = menu_width * 0.11
        group_width   = menu_width - menu_gap * 2

        group_x         = menu_x + menu_gap * 1.25
        up_group_y    = menu_y + menu_gap * 0.5
        square_group_y = menu_y + menu_gap + menu_height * 0.10

        up_group   .set_pos([group_x, algo_group_y   ])
        square_group.set_pos([group_x, square_group_y])

        up_group.width     = group_width
        square_group.width  = group_width

        self.groups = [up_group, square_group]

"""
    def update():
        for group in Interface.groups:
            group.update()

    def click(pos):
        for group in Interface.groups:
            if group.click(pos):
             # click() возвращает true, если Ты попал на какуето кнопку.
             # Если мы уже попали, то рассматривать другие кнопки не нужно и break
                break
