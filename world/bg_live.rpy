init python:
    def draw_bg(st, at): 
        return LiveComposite(
            (1080, 1920),
            (0, 0), "images/" + time.part + ".png"
            ),.1
init:
    image bg = DynamicDisplayable(draw_bg)