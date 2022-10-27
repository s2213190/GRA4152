################### P10.22 #########################################

from datetime import date

#Implementation of the class Appointment
class Appointment:

    apptList =[]

#Constructor
    def __init__(self,year,month,day,description):
        self._description = description
        self._date = date(year,month,day)
        self._year = year
        self._month = month
        self._day = day

#Getter method for description
    def getDescription (self):
        return self._description

#Defintion of the funtion occursOn
    def occursOn(self,year,month,day):
        return self._date == date(year,month,day)

################################################### P 10.24 method ##############    
    def saveAppt(self):
        with open('Appt1.txt', 'a') as f:
            f.write(f"{self._year},{self._month},{self._day},{self._description},{self._freq}\n")
            f.close()
            
    @classmethod    # we create a class method to load appointments from the file.
    def loadAppt(cls):
        import pandas as pd
        Appt = pd.read_csv("Appt1.txt", header = None )
        Appt.columns = ["Year", "Month", "Day", "Description", "Freq"]
        Freq = input("Enter the Freq")  # Asking the user which type of assignments to create
        Appt = Appt[Appt["Freq"] == Freq]
        
        for i in range(len(Appt)):
            go = eval(Freq)(Appt.iloc[i,0],Appt.iloc[i,1],Appt.iloc[i,2],Appt.iloc[i,3])
            print(go.getDescription())

###################################################

#Implementation of the class Onetime

class Onetime(Appointment):
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)
        self._freq ="Onetime"

#occursOn method checks for day, month and year
    def occursOn(self,year,month,day):
        return self._date == date(year,month,day)
        
        
##################################################

#Implementation of the class Daily

class Daily(Appointment):
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)
        self._freq ="Daily"

#occursOn method always retunrs True       

    def occursOn(self,year,month,day):
        return True

###############################

#Implementation of the class Monthly

class Monthly(Appointment):
    
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)
        self._freq ="Monthly"


    def occursOn(self,year,month,day):
        return self._date.day == day

  
###############################################################################


#create a list of appointments using subclasses of Onetime, Daily, and Monthly

apptList = []
apptList.append(Daily(2013, 1, 1, "Go to Gym"))
apptList.append(Daily(2013, 1, 15, "Take a Walk"))
apptList.append(Monthly(2012, 11, 1, "Pay your rent"))
apptList.append(Monthly(2022, 1, 15, "Half Way through the month"))
apptList.append(Onetime(2022, 5, 17, "Happy Constitution Day"))
apptList.append(Onetime(1987, 10, 23, "Happy Birthday"))



#Prompt and read day form the user
day = int(input("Enter the day (0 to quit): "))


while bool(day) :
#Prompt and read year,month form the user
    month = int(input("Enter the month: "))
    year = int(input("Enter the year: "))
    for appt in apptList :
        if appt.occursOn(year,month,day) :
            print(appt.getDescription())

            
#Prompt and read day form the user
    day = int(input("Enter the day (0 to quit): "))
    
 
################### P10.23 ################### NOT A PART OF ASYNCH ASSIGNMENT #######################

def addAppt(year,month,day,description,apptType):
    return apptList.append(apptType(year,month,day,description))
    
addAppt(2022,10,10,"test",Monthly)   ############ P10.23 ###############

################### P10.24 ############################################

appt1 = Monthly(2022, 1, 1, "Pay your rent")
appt1.saveAppt()
appt2 = Daily(2022, 2, 1, "Go to Gym")
appt2.saveAppt()
appt3 = Onetime(2022, 5, 17, "Constitution Day")
appt3.saveAppt()
appt4 = Onetime(1987, 10, 23, "Happy Birthday")
appt4.saveAppt()


Appointment.loadAppt()