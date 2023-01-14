from random import randint, choice
import pgzrun

WIDTH=800
HEIGHT=500

box1=Rect((100,100),(50,50))
box2=Rect((WIDTH-100,100),(50,50))
box3=Rect((randint(100,700),randint(100,400)),(20,90))
#! box3-> randint one is x pos and one is y pos



b1x=2
b2x=4 #! SPEED 
b3y=3
def draw():
    screen.clear()
    screen.draw.filled_rect(box1,"olive")
    screen.draw.filled_rect(box2,"light blue")
    screen.draw.filled_rect(box3,"pink")
    screen.draw.text(f'box1{box1.x}| box2{box2.x}',(10,10),color="blue")
    

#^ we can read the global variable inside a function but cant be changed
#! but we can use the global keyword to access the global variable directly

def check_boundary(box,speed):
    if box.right>WIDTH or box.left<0:
        sounds.metal.play()
        return -speed
    if box.top<0 or box.bottom>HEIGHT:
        sounds.metal.play()
        return -speed
    return speed



def update():
    global b1x,b2x,b3y
    box1.x+= b1x #! movement and x is x axis
    box2.x+= b2x #! movement
    box3.y+= b3y #! error bcoz check_boundary will only work with x axis not for y axis
    #if box2.right>WIDTH or box2.left<0:
        #sounds.metal.play()
        #b2x=-b2x
    #if box1.right>WIDTH or box1.left<0:
        #sounds.metal.play()
        #b1x=-b1x  
    #! we are using function instead of lengthy code like if-else
    b1x=check_boundary(box1,b1x)
    b2x=check_boundary(box2,b2x)
    b3y=check_boundary(box3,b3y)
    if box1.colliderect(box2):
        b1x,b2x=-b1x,-b2x
    if box1.colliderect(box3):
        b1x=-b1x
    if box2.colliderect(box3):
        b2x=-b2x


    
pgzrun.go()