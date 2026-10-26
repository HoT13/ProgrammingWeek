from processing import *
x = 0

def setup():
    size(500, 400)

def draw():
    global x 
    background(240)
    
    ellipse(x, 200, 50, 50)
    line(x, 225, x, 300)
    line(x, 225, 20+x, 250)
    line(x, 225, -20+x, 250)
    line(x, 300, 20+x, 350)
    line(x, 300, -20+x, 350)
    
    x = x + 2
    
    if x > width:
        x = 0
run()
