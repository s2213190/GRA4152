### Implement a class address. An address has a house number, a street, an optional apartment number, a city, a state, and a postal code. 
# Define the constructor such that an object can be created in one of two ways: with an apartment number or without. 
# Supply a print method that print the address with the street on one line and the city, the state, and the postal code on the next line. 
# Supply a method def comesBefore(self, other) that tests whether this address comes before other when compared by postal code.


class Address:
    # Constructor created with and without default argument of None to allow for optional input

    def __init__(self, city, street, houseNum, state, postalCode, apartmentNum = None ):
        self._city = city
        self._street = street
        self._houseNum = houseNum
        self._apartmentNum = apartmentNum
        self._state = state
        self._postalCode = postalCode

    # prints the address
    def addressDetail(self): 
        print("The Address is"+ self._street + '\n' + self._city+ " "+ self._state + " " + str(self._postalCode))

    
    def comesBefore(self, other):
        if self._postalCode < other._postalCode:
            print("the address comes before the other")
        else:
            print("the adress comes same or after the other address")


Address_1 = Address("Oslo", "Moldegata", 09, "Østlandet", 0445 , 64) # with apartment num

Address_2 = Address("Oslo", "Hans Nordhal Gate", 01, "Østlandet", 0556) # without apartment num


Address_1.addressDetail()

print(Address_1.comesBefore(Address_2)) # prints True as expected

