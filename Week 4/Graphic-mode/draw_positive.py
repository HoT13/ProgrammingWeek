def setup():
    size(600, 600)

def draw():
    background(200)
    for i in range(5):
        x_pos = 60 + (i * 110)
        draw_positive(x_pos, 100)

def draw_positive(x, y):
    s = 20

    rect(x, y, s, s)
    rect(x, y - s, s, s)
    rect(x, y + s, s, s)
    rect(x - s, y, s, s)
    rect(x + s, y, s, s)