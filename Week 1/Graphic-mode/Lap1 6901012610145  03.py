from processing import *

def setup():
    size(650, 400)

def draw():
    background(230) 
    
    stroke(150)
    strokeWeight(3)
    line(50, 270, 600, 270)
    stroke(0)       
    strokeWeight(2) 
    line(100, 245, 100, 210)
    line(100, 210, 130, 185)
    line(130, 185, 230, 175)
    line(230, 175, 290, 125)
    line(290, 125, 370, 125)
    line(370, 125, 460, 185)
    
    line(460, 185, 500, 185)
    line(500, 185, 500, 245)
    line(100, 245, 150, 245)
    line(210, 245, 390, 245) 
    line(450, 245, 500, 245) 
    line(250, 170, 295, 135)
    line(295, 135, 365, 135)
    line(365, 135, 420, 170)
    line(250, 170, 420, 170)

    fill(50) 
    ellipse(180, 240, 60, 60)

    fill(50)
    ellipse(420, 240, 60, 60)

    

run()