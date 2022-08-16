


#first program is reference to private method in encapulation

class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__udpateSoftware() not accesible from object


#second program Is to display a private encapulation

class Vehicle:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Vehicle()
redcar.drive()
redcar.__maxspeed = 10 # will not change variable because its private
redcar.drive()

                              
