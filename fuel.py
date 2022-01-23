class Car:
    def __init__(self, fuel_efficiency, fuel_capacity):
        self.__fuel_efficiency = fuel_efficiency
        self.__fuel_capacity = fuel_capacity # setting this to 0
        self.fuel_level = 0

    # def tank(self, fuel):
    #     fuel_level = 0
    #     fuel_level += fuel
    #     return fuel_level

    def drive(self, miles):
        self.fuel_level = self.get_gas_level() - miles / self.__fuel_efficiency
        print(self.fuel_level)
        return self.fuel_level

    def add_gas(self, gallons):
        print(f"{self.__fuel_capacity} fuel_capacity")
        print(f"{self.fuel_level} current fuel level")
        print(f"{gallons} gallons filling the tank")
        
        #However, an error should be printed if attempting to add more gas than the gas tank's capacity will allow.
        if self.__fuel_capacity >= gallons:
            self.fuel_level += gallons
            #update = get_gas_level() + gallons
        else:
            print('cannot fill it up as tank capacity is lower than what one is adding to it')
        return self.fuel_level

    def get_gas_level(self):
        return self.fuel_level
       
    def __str__(self):
        return (f"{self.fuel_level} gallons of gas remain") #12 gallons of gas remain


myHybrid = Car(50, 20) #50 mpg, 20 gallons capacity
#print(myHybrid.fuel_level) ##get initial fuel_level
myHybrid.add_gas(14) #Tank now has 14 gallons of gas; try with more than 20 -- it should print out error message on line 
print(myHybrid)
# print(myHybrid.fuel_level) ##get fule_level after add_gas(14)
print(myHybrid.get_gas_level())
myHybrid.drive(100) #Drive 100 miles
myHybrid.add_gas(1)
print(myHybrid)
# print(myHybrid.get_gas_level(), "gallon(s) of gas remain")

