import pgzrun

HEIGHT=600
WIDTH=800
#! rect with 100*100 size and 0,0 coordinates
rect=Rect((0,0),(100,100))
rect2=Rect((250,250),(50,100))

def draw():
    screen.fill('white')
    screen.draw.filled_rect(rect,'red')
    screen.draw.filled_rect(rect2,'green')

pgzrun.go()