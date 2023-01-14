import pgzrun
class Robot(Actor):
    def __init__(self, imglist, **kwargs):
        super().__init__(imglist[0])
        self.imglist=imglist
    def walk(self):
        self.imglist=self.imglist[self.frame]
        print((self.frame +1)% len(self.imglist))
        self.frame=((self.frame+1)%len(self.imglist))
        if self.

HEIGHT=400
WIDTH=600

r=Robot(['w1','w2','w3','w4','w5','w6','w7'],center=(100,100))
def draw():
    screen.clear()
    r.draw()
def update():
    r.walk()
pgzrun.go()