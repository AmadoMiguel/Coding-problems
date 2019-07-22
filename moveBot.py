class robot():
    posx = 0
    posy = 0
    totalDistance = 0
    totalSteps = 0
    # Constructor method
    def __init__(self,initx,inity):
        self.posx = initx
        self.posy = inity
        
    def move(self,direction,nSteps):
        if direction == "up":
            self.posy += nSteps   
            self.totalDistance += self.posy 
        if direction == "down":
            self.posy -= nSteps   
            self.totalDistance -= self.posy 
        if direction == "right":
            self.posx += nSteps   
            self.totalDistance += self.posx
        if direction == "left":
            self.posx -= nSteps   
            self.totalDistance -= self.posx
        self.totalSteps += nSteps
    def status(self):
        print("Current location:","x:",self.posx,"y:",self.posy)    
        print("Distance traveled:",self.totalDistance)            
        print("Total steps given:",self.totalSteps)

# Instance of the robot class
newBot = robot(0,0)
newBot.move("right",5)
newBot.move("up",2)
newBot.move("down",4)
newBot.move("left",2)
newBot.move("up",1)

newBot.status()