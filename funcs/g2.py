import pgzrun
WIDTH=800
HEIGHT=500

square=Rect((400,250),(50,50))
s2=Rect((200,250),(50,50))

b_vx=4 #! global vairable

def draw():
    screen.clear()
    screen.draw.filled_rect(square,'lightblue')
    screen.draw.filled_rect(s2,'green')

def update():
    global b_vx #* this allows us to change the value of b_vx
    #! loop around the screen
    square.x+=2
    if square.x>WIDTH:
        square.x=0
    #! bounce the box
    s2.x+=b_vx
    if s2.right>WIDTH or s2.left<0:
        b_vx=-b_vx #! invert the direction of box

pgzrun.go()