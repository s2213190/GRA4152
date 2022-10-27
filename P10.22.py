from datetime import date

#Implementation of the class Appointment
class Appointment:
    
#Constructor
    def __init__(self,year,month,day,description):
        self._description = description
        self._date = date(year,month,day)

#Getter method for description
    def getDescription (self):
        return self._description

#Defintion of the funtion occursOn
    def occursOn(self,year,month,day):
        return self._date == date(year,month,day)


###################################################

#Implementation of the class Onetime

class Onetime(Appointment):
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)

#occursOn method checks for day, month and year
    def occursOn(self,year,month,day):
        return self._date == date(year,month,day)
    
##################################################

#Implementation of the class Daily

class Daily(Appointment):
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)

#occursOn method always retunrs True       

    def occursOn(self,year,month,day):
        return True

###############################

#Implementation of the class Monthly

class Monthly(Appointment):
    
    def __init__(self,year,month,day,description):
        super().__init__(year,month,day,description)

#occursOn method checks only the day

    def occursOn(self,year,month,day):
        return self._date.day == day

################################


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