import random as r
import os

# Clear console function
clear = lambda: os.system('clear')   

class openTheChests():
    # Where user stores what he/she has found
    bag = {}
    # Chests status (opened/closed)
    chests = {}
    # Number of chests in the game
    N = 0
    # Keys info
    keysToUse = []
    initialKeys = []
    # Define the boolean for the end of the game
    allChestsOpened = None
    def __init__(self,N):
        self.N = N
        # All chests initially closed
        self.chests = {"ch%d"%(i,):"closed" for i in range(1,self.N+1)}
        # Starts with 1 random key
        initialKeys = [i for i in range(1,self.N+1)]
        # Random key to start
        rKeyStart = r.randint(1,4)
        self.bag["k%d"%(rKeyStart,)] = 1
        # Other key types set initially to 0
        initialKeys.remove(rKeyStart)
        for k in initialKeys:
            self.bag["k%d"%(k,)] = 0
        # Types of keys available according to opened/closed chests
        self.keysToUse = [i for i in range(1,self.N+1)]
        # Game end control
        self.allChestsOpened = False
    def reqUsrAct(self):
        # Ask the user to prompt in the next chest to open (if closed)
        chToOpen = input("Which treasure would you like to open next? (n): ")
        self.openChest(chToOpen)
    def openChest(self,nChest):
        # Open the chest if it is closed
        if self.chests['ch%d'%(nChest,)] == "opened":
            print("Selected chest was already opened. Select another one.")
        else:
            # Check if the user has at least 1 key to open the requested chest
            if self.bag['k%d'%(nChest,)] >= 1:
                # The chest is opened
                self.chests['ch%d'%(nChest,)] = "opened"  
                # Check if all chests were opened
                self.allChestsOpened = self.checkGameStatus()
                if not self.allChestsOpened:  
                    # If not...
                    # Delete all keys of that chest type
                    del self.bag['k%d'%(nChest,)]
                    # Check for found keys (if any) and store in bag
                    self.randKeyGen(nChest)
                else:
                    # If so, game finishes
                    print("Game ends.") 
                
    def randKeyGen(self,keyUsed):
        # Determine how many different keys will the opened chest contain
        # It could contain from 0 keys to N keys of any type
        nKeys = r.randint(0,self.N)
        # Stores the information about the found keys
        keysFound = {}
        if nKeys != 0:
            # Remove the already used key type
            self.keysToUse.remove(keyUsed)
            # First determine how many different (random) type of keys
            keyTypes = r.randint(1,len(self.keysToUse))
            for _ in range(keyTypes):
                keyFound = r.choice(self.keysToUse)
                # Store random type of key and how many keys of the type found
                keysFound["k%d"%(keyFound,)] = keysFound.get("k%d"%(keyFound,),0) + 1
            # Store found keys in bag
            for k,v in keysFound.items():
                self.bag[k] = v
    # Show game stats            
    def showInfo(self):
        # Show chests info
        print(self.chests)
        # Show elements in bag         
        print(self.bag)               
    # Check if all treasures were opened
    def checkGameStatus(self):    
        c = 0
        for i in self.chests.values():
            if i == "opened":
                c += 1
        if c == 4:
            return True
        else:
            return False   
                 

test = openTheChests(4)

# Game test script
while not test.allChestsOpened:
    # Clear console
    clear()
    if test.allChestsOpened:
        break
    test.showInfo()
    test.reqUsrAct()

# Print final game message    
if test.allChestsOpened:
    print("Congratulations, you opened all chests!")