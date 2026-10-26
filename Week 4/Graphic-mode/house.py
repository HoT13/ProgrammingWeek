def setup():
    size(400, 400)

def draw():
    background(255)
    draw_house(100, 100)

def draw_house(x, y):
    draw_roof(x, y)
    draw_ceiling(x, y)
    
    draw_multiple_floors(x, y, 2)
    
    draw_floor_at_bottom(x, y, 2)

def draw_roof(x, y):
    line(x, y, x + 100, y - 50)
    line(x + 100, y - 50, x + 200, y)

def draw_ceiling(x, y):
    line(x, y, x + 200, y)

def draw_multiple_floors(x, y, floors):
    for i in range(floors):
        line(x, y + (i * 100), x, y + 100 + (i * 100))
        line(x + 200, y + (i * 100), x + 200, y + 100 + (i * 100))
        line(x, y + 100 + (i * 100), x + 200, y + 100 + (i * 100))

def draw_floor_at_bottom(x, y, floors):
    line(x, y + (floors * 100), x + 200, y + (floors * 100))