from processing import *

w = 50
h = 100

def draw_L(x, y):
    line(x, y, x, y + h)
    line(x, y + h, x + w, y + h)

def draw_I(x, y):
    line(x + w/2, y, x + w/2, y + h)
    line(x, y, x + w, y)
    line(x, y + h, x + w, y + h)

def draw_N(x, y):
    line(x, y, x, y + h)
    line(x, y, x + w, y + h)
    line(x + w, y, x + w, y + h)

def draw_E(x, y):
    line(x, y, x, y + h)
    line(x, y, x + w, y)
    line(x, y + h/2, x + w, y + h/2)
    line(x, y + h, x + w, y + h)

def setup():
    size(500, 500)
    background(200)
    
    user_word = input("Enter L,N,I or E only!: ")

    user_word = user_word.upper() 
    
    start_x = 50
    start_y = 100
    spacing = 30
    

    for i in range(len(user_word)):
        char = user_word[i] 
        
        current_x = start_x + (i * (w + spacing))

        if char == 'L':
            draw_L(current_x, start_y)
        elif char == 'I':
            draw_I(current_x, start_y)
        elif char == 'N':
            draw_N(current_x, start_y)
        elif char == 'E':
            draw_E(current_x, start_y)

def draw():
    pass

run()