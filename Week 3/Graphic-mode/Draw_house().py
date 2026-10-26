def setup():
    size(400, 400)

def draw():
    background(220)
    draw_house()

def draw_house():
    draw_roof()
    draw_ceiling()
    draw_wall()
    draw_floor()

def draw_roof():
    line(100, 200, 200, 100)
    line(300, 200, 200, 100)

def draw_ceiling():
    line(100, 200, 300, 200)

def draw_wall():
    line(100, 200, 100, 350) 
    line(300, 200, 300, 350) 
    ellipse(200, 275, 50, 50)

def draw_floor():
    line(100, 350, 300, 350)