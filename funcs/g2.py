import pgzrun
WIDTH=800
HEIGHT=500

#! Taking block size on screen(800*500)
square=Rect((400,250),(50,50))
s2=Rect((200,250),(50,50))

b_vx=4 #! global vairable
#* b_vx is variable for speed... 4 is the speed of b_vx.

def draw():
    screen.clear()
    screen.draw.filled_rect(square,'lightblue')
    screen.draw.filled_rect(s2,'green')

def update():
    global b_vx #* this allows us to change the value of b_vx
    
    #! loop around the screen
    square.x+=2 #* square variable will add 2(speed) or called the speed on x axis.
    if square.x>WIDTH: #* square variable on x axis is greater than width i.e., 800
        #* when the condition is true do this -->
        square.x=0
    
    #! bounce the box
    s2.x+=b_vx
    if s2.right>WIDTH or s2.left<0:
        b_vx=-b_vx #! invert the direction of box

pgzrun.go()