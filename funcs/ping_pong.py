import pgzrun

WIDTH=800
HEIGHT=500

ball=Rect((WIDTH/2, HEIGHT/2),(20,20))
player=Rect((10,HEIGHT/2),(20,100))
opponent=Rect((WIDTH-30,HEIGHT/2),(20,100))

score=0
ball_x=5
ball_y=5
opp_y=5

def draw():
    screen.clear()
    #screen.blit("background",(0,0))
    screen.draw.filled_rect(ball,"pink")
    screen.draw.filled_rect(player,"blue")
    screen.draw.filled_rect(opponent,"maroon")
    screen.draw.text(str(score),center=(WIDTH/2,20),fontsize=40)

def move_ball():
    global ball_x,ball_y,score
    ball.x+=ball_x
    ball.y+=ball_y
    if ball.top<0 or ball.bottom> HEIGHT:
        ball_y=-ball_y
    if ball.left<0 or ball.right>WIDTH:
        if ball.right>WIDTH:
            score+=1
        elif ball.left<0:
            score-=1
        ball_x=-ball_x
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_x=-ball_x
    if score==-10:
        exit()

def move_player():
    if keyboard.up and not player.top<0:
        player.y-=5
    if keyboard.down and not player.bottom>HEIGHT:
        player.y+=5

def move_opponent():
    global opp_y
    opponent.y+=opp_y
    if opponent.top<0 or opponent.bottom>HEIGHT:
        opp_y=-opp_y

def update():
    move_ball()
    move_player()
    move_opponent()

pgzrun.go()



