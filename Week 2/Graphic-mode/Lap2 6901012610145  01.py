from processing import *
x = 0

def setup():
    size(500, 400)

def draw():
    global x 
    background(240)
    
    ellipse(x, 200, 50, 50)
    
    x = x + 10
    
    if x > width:
        x = 0
run()
