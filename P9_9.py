# Implement a class ComboLock that works like the combination lock
# in a gym locker, as shown here. The lock is constructed with a
# combination—three numbers between 0 and 39. The reset method
# resets the dial so that it points to 0. The turnLeft and turnRight
# methods turn the dial by a given number of ticks to the left or
# right. The open method attempts to open the lock. The lock opens
# if the user first turned it right to the first number in the combination, then left to the second, and then right to the third.
# class ComboLock :
# def ComboLock(self, secret1, secret2, secret3) :

# def reset(self) :
# . . .
# def turnLeft(self, ticks) :
# . . .
# def turnRight(self, ticks) :
# . . .
# def open(self) :
# . . .



##Public Interface : A Combo GymLock that can be opened by arraning the dial positions to specific rotations

class ComboLock():
    
    def __init__(self,secret1,secret2,secret3):
        #Configure a Combolock to the specifications

        if all(item in range(40) for item in [secret1,secret2,secret3]): #  checks if the ComboLock is configured correctly
            self._secret1 =secret1
            self._secret2 =secret2
            self._secret3 =secret3
            self._dial = 0 # a instance variable to record the current dialPosition
            self._turnOrder = [] # a instance variable to store rotation order
            self._dialPosition = [] # a instance variable to store dialPositions order
        else:
            raise Exception("Not a Valid Lock")
            
    def reset(self):
        self._dial =  0
        self._turnOrder = []
        self._dialPosition = []
    
    def turnLeft (self, ticks):
        no_of_rotations = ticks // 40  # The locks may have the same dial positions even if the dial is rotated more than needed
        for i in range(no_of_rotations + 1):
            self._turnOrder.append("Left")
        self._dial = (self._dial + ticks) % 40 #Setting the dialPosition after the ticks are added
        self._dialPosition.append(self._dial)
        
    def turnRight (self, ticks):
        no_of_rotations = ticks // 40
        for i in range(no_of_rotations + 1):
            self._turnOrder.append("Right")
        self._dial = (self._dial - ticks) % 40
        self._dialPosition.append(self._dial)
        
    def Open(self):
        if self._turnOrder == ["Right","Left","Right"] and  self._dialPosition == [self._secret1,self._secret2,self._secret3]:
            print ("ComboLock is Open")
        else :
            print ("ComboLock cannot be opened")
        
        print(f"Dial combination entered is {self._dialPosition}")
        print(f"Dial order entered is {self._turnOrder}")

        
#### TESTING
Lock1 = ComboLock(1,2,3)
Lock1.reset()
Lock1.turnRight(39) 
Lock1.turnLeft(1)
Lock1.turnRight(39)
Lock1.Open() # Prints the lock is open as expected


print("****************************")

Lock2 = ComboLock(15,13,28)
Lock2.reset()
Lock2.turnRight(25) 
Lock2.turnLeft(78) # more than optimal rotations
Lock2.turnRight(25)
Lock2.Open() # Prints "ComboLock cannot be opened" despite matching secret key as the Dial Order does not match
