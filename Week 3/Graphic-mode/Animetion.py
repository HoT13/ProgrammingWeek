y = 200        
y_speed = 5     
radius = 25     

def setup():
    size(400, 400)
    fill(0, 150, 255)

def draw():
    global y, y_speed
    
    background(240)
    
    y = y + y_speed
    
    if y > height - radius or y < radius:
        y_speed = y_speed * -1
        
    circle(width / 2, y, radius * 2)